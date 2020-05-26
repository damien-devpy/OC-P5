# coding: utf-8
"""ORM looking like, manage and interact with database."""

from mysql import connector
from configuration import (DATABASE,
                           DATABASE_NAME,
                           CREDENTIALS,
                           )
from model.keyworderror import KeywordError


class Manager:
    """In charge of managing data base."""

    def __init__(self):
        """Init attributes of manager objects.

        Attributes:
            self._cnx (connect object): Init connection to database
            self._cursor (cursor object): Interact with database (CRUD)

        """
        self._cnx = connector.connect(**CREDENTIALS)
        self._cursor = self._cnx.cursor()

    def create_db(self):
        """Create the database from a sql file."""
        with open(DATABASE, mode='r', encoding='utf-8') as sql_file:
            for line in sql_file:
                self._cursor.execute(line)

    def set_db(self):
        """Set to current data base."""
        self._cursor.execute(f"USE {DATABASE_NAME}")

    def is_there_db(self):
        """Check if database exist.

        Return:
            bool: True if database exist, False otherwise

        """
        self._cursor.execute(f"SHOW DATABASES LIKE '{DATABASE_NAME}'")
        self._cursor.fetchall()

        # If self._cursor contain a result, database exist, return True
        return bool(self._cursor.rowcount)


    def insert_all(self, list_of_objects):
        """In charge of create part of CRUD, for a massive insert.

        Args:
            list_of_objects (list): A list of objects to insert in DB

        """
        # Before inserting data in DB, checking if objects contains
        # a relation to any liaison table
        if self._is_there_relation(list_of_objects[0]):
		
            for an_object in list_of_objects:
                # Filling table with the current object
                self._insert(an_object)

                data_liaison_table = self._get_liaison_data(an_object)

                # Filling table for every objects in data_liaison_table
                for liaison_object in data_liaison_table:
                    self._insert(liaison_object)

                # After inserting every objects in their proper tables
                # Filling the liaison table
                self._filling_liaison_table(an_object, data_liaison_table)
				
        else:

            for an_object in list_of_objects:
                self._insert(an_object)

        self._cnx.commit()

    def insert_one_at_a_time(self, object_to_insert):
        """In charge of create part of CRUD, for inserting data in DB.

        Args:
            object_to_insert (model object): Model object to insert in database

        """
        self._insert(object_to_insert)
        self._cnx.commit()

    def select(self, an_object, column=None, **kwargs):
        """In charge of read part of CRUD, for selecting data in DB.

        Args:
            an_object (class reference / model object) : If select query is
				for a column or a table, an_object is a class reference
				for the table in database. For a specific row an_object will
				be a model object

            column (str): Default to None. Otherwise, meaning method has to
                look for a specific column in the table DB

            **kwargs (dict): Keyword argument for looking a specific row

        """
        self._cursor.execute("START TRANSACTION")

        # If a specific column is asked
        if column:
			# Calling private method select_column
			# with a class reference and a column name as arguments
            return self._select_column(an_object, column)

        # Elif, a specific row is asked
        elif kwargs:
			# Calling private method select_row
			# with a model object and a keyword to look for as arguments
            self._select_row(an_object, **kwargs)

        # Else, an entire table is asked
        else:
			# Calling private method select_table
			# witth a classe reference as argument
            return self._select_table(an_object)

        self._cnx.commit()

    def select_through_join(self,
                            class_ref_starting,
                            **kwargs,
                            ):
        """Specific method to select data in DB through a table liaison."""
		# Get name of the table in DB represent by the class reference
        starting_table = class_ref_starting.TABLE_NAME
		# Same here, through the class reference contain in attribute liaison_table
        ending_table = class_ref_starting().liaison_table().TABLE_NAME

        key, value = self._get_where_clause(**kwargs)

        # Get columns of the ending table, represent by attributes of the
        # class reference contain in attribute liaison_table
        ending_columns = ", ".join(class_ref_starting().liaison_table().attrs()
                                   )

        # Using query join, table name is needed with columns
        # in order to not being ambiguous
        ending_table_columns = ", ".join(f"{ending_table}.{c}"
                                         for c in ending_columns.split(", ")
                                         )

		# Build up the liaison table name with each table name
        liaison_table_name = sorted([starting_table, ending_table])
        liaison_table_name = (liaison_table_name[0] +
                              "_" +
                              liaison_table_name[1]
                              )

        query = (f'SELECT {ending_table_columns} FROM {ending_table} '
                 f'INNER JOIN {liaison_table_name} '
                 f'ON {ending_table}.id = '
                 f'{liaison_table_name}.{ending_table}_id '
                 f'INNER JOIN {starting_table} '
                 f'ON {starting_table}.id = '
                 f'{liaison_table_name}.{starting_table}_id '
                 f'WHERE {starting_table}.{key} = "{value}"'
                 )

        self._cursor.execute(query)

        tmp_list = list()
		
		# Filling a list with all results
        for value in self._cursor.fetchall():
            tmp_object = class_ref_starting().liaison_table()

            for i, c in enumerate(tuple(ending_columns.split(', '))):
                setattr(tmp_object, c, value[i])

            tmp_list.append(tmp_object)

        return tmp_list

    def substitution(self, product_object, chosen_category):
        """Specifically in charge for looking a product substitution.

        Substitution occur IN PLACE.

        Args:
            product_object (model object): Product choosed by user for looking
                to a substitute
            chosen_category (str): Category choosed by user for
                looking for a product to substitute

        """
		# Get all products from the category choose by user
        list_of_products = self.select_through_join(product_object.liaison_table,
													name=chosen_category,
													)

        # Sort the list of products by nutrition grade
        list_of_products.sort(key=(lambda product: product.nutrition_grade))

        # Get the first one of the list, i.e. product with best nutrition grade
        for attr, value in zip(product_object.attrs(),
                               list_of_products[0].values(),
                               ):
            setattr(product_object, attr, value)

    def _insert(self, object_to_insert):
        """In charge of create part of CRUD.

        Insert method without commit, for a massive insert

        Args:
            object_to_insert (model object): Model object to insert in database

        """
        table = object_to_insert.TABLE_NAME
        columns = ", ".join(object_to_insert.attrs())
        values = tuple(object_to_insert.values())
        replacement = self._get_placeholders(len(values))

        # If there is a duplicate key
        if object_to_insert.duplicate_key:

            duplicate_key = 'ON DUPLICATE KEY UPDATE id = LAST_INSERT_ID(id)'
            query = (f'INSERT INTO {table} ({columns})'
                     f'VALUES ({replacement}) {duplicate_key}'
                     )
        # Elif there is a ignore attribute
        elif object_to_insert.ignore:

            query = (f'INSERT IGNORE INTO {table} ({columns})'
                     f'VALUES ({replacement})'
                     )
        else:

            query = f'INSERT INTO {table} ({columns}) VALUES ({replacement})'

        self._cursor.execute(query, values)

        fresh_id = self._get_back_id()
        setattr(object_to_insert, 'id', fresh_id)

    def _select_column(self, class_ref, column):
        """Private method for reading a specific column in DB.

        Args:
            class_ref (class reference): Reference to the class model
				representing a table in database, on which the search has to be
				done
            columns (str): Specific column to look for in the table

        """
        table = class_ref.TABLE_NAME
        self._cursor.execute(f"SELECT {column} FROM {table}")
        tmp_list = list()

        for value in self._cursor.fetchall():

            tmp_object = class_ref()
            setattr(tmp_object, column, value[0])
            tmp_list.append(tmp_object)

        return tmp_list

    def _select_row(self, object_to_read, **kwargs):
        """Private method for getting a specific row in DB.

        Args:
            object_to_read (model object): Model object used to select table to
            read, and filled with information of the specific row
            kwargs (dict): Keyword argument for a specific row

        """
        table = object_to_read.TABLE_NAME
        columns = ", ".join(object_to_read.attrs())

        key, value = self._get_where_clause(**kwargs)

        query = f"SELECT {columns} FROM {table} WHERE {key}='{value}'"
        self._cursor.execute(query)
        # Getting the result of the query
        result = self._cursor.fetchone()

        # If keyword asked doesn't exist in database
        try:
            if not self._cursor.rowcount:
                raise KeywordError(f'{key} : {value}'
                                   'doesn\'t exist in database !'
                                   )

        except KeywordError as err:
            print(err)

        else:
            # Filling attributes object with result
            for i, c in enumerate(tuple(columns.split(", "))):
                setattr(object_to_read, c, result[i])

    def _select_table(self, class_ref):
        """Private method for getting an entire table from the database.

        Args:
            class_ref (class reference): Model class reference representing
                table in database from which we want data

        """
        table = class_ref().TABLE_NAME
        columns = ", ".join(class_ref().attrs())

        self._cursor.execute(f"SELECT {columns} FROM {table}")
        list_of_objects = list()

        for values in self._cursor.fetchall():

            tmp_object = class_ref()

            for i, c in enumerate(tuple(columns.split(", "))):

                setattr(tmp_object, c, values[i])

            list_of_objects.append(tmp_object)

        return list_of_objects

    def _filling_liaison_table(self, object_linked, liaison_data):
        """In charge of C part of CRUD in a liaison table.

        Args:
            object_linked (model object): Model object linked to the liaison
                table by a many to many relation
            liaison_data (list): List of model objects to insert in
				the liaison table with the object_linked

        """
        table = liaison_data[0].TABLE_NAME + '_' + object_linked.TABLE_NAME
        columns = (f'{object_linked.TABLE_NAME}' +
                   '_id' +
                   ', ' +
                   f'{liaison_data[0].TABLE_NAME}' +
                   '_id'
                   )

        replacement = self._get_placeholders(len(tuple(columns.split(', '))))
        list_of_values = list()

        # For each object in liaison data
        # Getting the id attribute of it
        for an_object in liaison_data:
            list_of_values.append((object_linked.id, an_object.id))

        query = (f'INSERT INTO {table} ({columns})'
                 f'VALUES ({replacement})'
                 )

        self._cursor.executemany(query, list_of_values)

    def _is_there_relation(self, object_to_inspect):
        """Check if a many to many relation exists.

        Args:
            object_to_inspect (model object): Model object to inspect
			
        Return:
            bool: Return True if there is many to many relation, False
                otherwise

        """
        return bool(object_to_inspect.belong_to)

    def _get_liaison_data(self, object_to_inspect):
        """Get back data from a many to many relation attribute.

        Args:
            object_to_inspect (model object): Model object to inspect

        Return:
            object_to_inspect.belong_to (list): List containing data
                object_to_inspect have a many to many liaison with

        """
        return object_to_inspect.belong_to

    def _get_placeholders(self, reference):
        """Set a tuple of sql placeholders.

        Args:
            reference (int): How much sql placeholders needs to be define

        Returns:
            placeholders (str): SQL placeholders

        """
        return ", ".join('%s' for i in range(reference))

    def _get_back_id(self):
        """Return last inserted id.

        Return
            id (int): Last inserted id in DB

        """
        self._cursor.execute("SELECT LAST_INSERT_ID()")

        return self._cursor.fetchall()[0][0]

    def _get_where_clause(self, **kwargs):
        """Take a keyword argument and return a pair of key/values as strings.

        Args:
            kwargs (dict): Keyword argument

        Return:
            key (str): Key as string
            value (str): Value as string

        """
        key = next((f"{i}" for i in kwargs))
        value = f"{kwargs[key]}"

        return key, value
