# coding: utf-8

from mysql import connector
from configuration import (DATABASE,
						   DATABASE_NAME,
						  )
from model.keyworderror import KeywordError
import pdb

class Manager:
	"""In chage of managing data base
	"""

	def __init__(self):

		self._cnx = connector.connect(user='admin', host='localhost', password='admin')
		self._cursor = self._cnx.cursor()


	def create_db(self):
		"""Creating the database from a sql file
		"""

		with open(DATABASE, mode='r', encoding='utf-8') as sql_file:
			for line in sql_file:
				self._cursor.execute(line)


	def set_db(self):

		self._cursor.execute(f"USE {DATABASE_NAME}")


	def is_there_db(self):
		"""Checking if database exist

		Return:

			bool: True if database exist, False otherwhise

		"""

		self._cursor.execute(f"SHOW DATABASES LIKE '{DATABASE_NAME}'")
		self._cursor.fetchall()

		# If self._cursor contain a result, database exist, return True
		if self._cursor.rowcount:

			return True

		else:

			return False


	def insert_all(self, list_of_objects):
		"""In charge of C part of CRUD (create), for a massive insert

		Args:

			list_of_objects (list): A list of objects to insert at once in DB

		"""

		# Before inserting data in DB, checking if objects contains
		# a relation to any liaison table
		relation_exist = self._is_there_relation(list_of_objects[0])

		if relation_exist:

			for an_object in list_of_objects:

				# Filling table with the current object
				self.insert(an_object)

				data_liaison_table = self._get_liaison_data(an_object)
				
				# Filling table for every objects in data_liaison_table
				for liaison_object in data_liaison_table:
					
					self.insert(liaison_object)

				# After inserting every objects in their proper tables
				# Filling the liaison table
				self._filling_liaison_table(an_object, data_liaison_table)

		else:

			for an_object in list_of_objects:

				insert(an_object)


	def insert(self, object_to_insert):
		"""In charge of C part of CRUD (create), for inserting data in DB

		Args:

			object_to_insert (model object): Model object to insert in database

		"""

		table = object_to_insert.TABLE_NAME
		columns = self._get_columns(object_to_insert)
		values = self._get_values(object_to_insert, tuple(columns.split(', ')))
		replacement = self._get_placeholders(len(values))

		# If there is a duplicate key
		if object_to_insert.__dict__['duplicate_key']:

			duplicate_key = "ON DUPLICATE KEY UPDATE id = LAST_INSERT_ID(id)"
			query = f"INSERT INTO {table} ({columns}) VALUES ({replacement}) {duplicate_key}"

		# Elif there is a ignore attribute
		elif object_to_insert.__dict__['ignore']:

			query = f"INSERT IGNORE INTO {table} ({columns}) VALUES ({replacement})"

		else:

			query = f"INSERT INTO {table} ({columns}) VALUES ({replacement})"

		self._cursor.execute(query, values)

		fresh_id = self._get_back_id()
		setattr(object_to_insert, 'id', fresh_id)

		self._cnx.commit()


	def select(self, an_object, column=None, **kwargs):
		"""In charge of R part of CRUD (read), for selecting data in DB

		Args:

			class_ref: If select query is for a column or a table, an_object is
				a class reference for the table in database. For a specific row
				an_object will be a model object

			column (str): Default to None. Otherwise, meaning method has to
				look for a specific column in the table DB

			**kwargs (dict): Keyword argument for looking a specific row

		Return:

		"""

		self._cursor.execute("START TRANSACTION")

		# If a specific column is asked
		if column:

			return self._select_column(an_object, column)

		# Elif, a specific row is asked
		elif kwargs:

			self._select_row(an_object, **kwargs)

		# Else, an entire table is asked
		else:

			return self._select_table(an_object)

		self._cnx.commit()


	def select_through_join(self,
							class_ref_starting,
							**kwargs,
							):
		"""Specific method for selecting data in DB if we need to go through
			table liaison

		"""

		starting_table = class_ref_starting.TABLE_NAME
		
		key, value = self._get_where_clause(**kwargs)

		ending_table = class_ref_starting().liaison_table().TABLE_NAME

		# Getting columns of the ending table, represent by attributes of the 
		# class reference
		ending_columns = self._get_columns(class_ref_starting().liaison_table())

		# Using query join, table name is needed with columns
		# in order to not being ambiguous 
		ending_table_columns = ", ".join(f"{ending_table}.{c}" for c in ending_columns.split(", "))

		liaison_table_name = sorted([starting_table, ending_table])
		liaison_table_name = liaison_table_name[1] + "_" + liaison_table_name[0]

		self._cursor.execute(f"""
			SELECT {ending_table_columns} FROM {ending_table}
			INNER JOIN {liaison_table_name}
			ON {ending_table}.id = {liaison_table_name}.{ending_table}_id
			INNER JOIN {starting_table}
			ON {starting_table}.id = {liaison_table_name}.{starting_table}_id
			WHERE {starting_table}.{key} = "{value}" """
		)

		tmp_list = list()

		for value in self._cursor.fetchall():
			
			tmp_object = class_ref_starting().liaison_table()

			for i, c in enumerate(tuple(ending_columns.split(', '))):

				setattr(tmp_object, c, value[i])

			tmp_list.append(tmp_object)


		return tmp_list


	def substitution(self, product_object, category_choosed):
		"""Specifically in charge for looking a product substitution
			Substitute occur IN PLACE

		Args:

			product_object (model object): Product choosed by user for looking
				to a substitute
			category_choosed (model object): Category choosed by user for
				looking for a product to substitute

		"""

		columns = self._get_columns(product_object)
		columns_with_table_name = ', '.join(f"{product_object.TABLE_NAME}.{c}" for c in columns.split(', '))

		query = f"""
			SELECT {columns} FROM (
				SELECT {columns_with_table_name}
				FROM {product_object.TABLE_NAME}
				INNER JOIN product_category
				ON product.id = product_category.product_id
				INNER JOIN category
				ON product_category.category_id = category.id
				INNER JOIN category as category_2
				ON category.name = category_2.name
				WHERE category_2.name = "{category_choosed.name}") as products 
			WHERE products.nutrition_grade < "{product_object.nutrition_grade}"
			ORDER BY products.nutrition_grade

				"""

		self._cursor.execute(query)

		# Making columns an iterable
		columns = tuple(columns.split(', '))

		# Getting first result of the query, i.e. product with better nutriscore
		result = self._cursor.fetchmany(size=1)

		# If a better product has been found
		if result:

			for i, value in enumerate(result[0]):

				setattr(product_object, columns[i], value)


############################## PRIVATE METHODS ##############################


	def _select_column(self, class_ref, column):
		"""Private method for reading a specific column in table from the
			database

		Args: 

			class_ref (class): Reference to the class model representing a
				table in database, on which the search has to be done
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
		"""Private method for getting a specific row in a table from the
			database

		Args:

			object_to_read (model object): Model object used to select table to
			read, and filled with information of the specific row
			kwargs (dict): Keyword argument for a specific row

		"""

		table = object_to_read.TABLE_NAME
		columns = self._get_columns(object_to_read)

		# Building where clause from the keyword argument
		# key = next((f"{i}" for i in kwargs.keys()))
		# value = f"{kwargs[key]}"

		key, value = self._get_where_clause(**kwargs)

		query = f"SELECT {columns} FROM {table} WHERE {key}='{value}'"

		self._cursor.execute(query)

		# Getting the result of the query
		result = self._cursor.fetchone()

		# If keyword asked doesn't exist in database
		try:
			if self._cursor.rowcount == -1:
				raise KeywordError(f"{key} : {value} doesn't exist in database !")

		except KeywordError as err:
			print(err)

		else:

			# Filling attributes object with result
			for i, c in enumerate(tuple(columns.split(", "))):
				setattr(object_to_read, c, result[i])



	def _select_table(self, class_ref):
		"""Private method for getting an entire table from the database

		Args:

			class_ref (class reference): Model class reference representing
				table in database from which we want data

		"""

		table = class_ref().TABLE_NAME
		columns = self._get_columns(class_ref())

		self._cursor.execute(f"SELECT {columns} FROM {table}")

		list_of_objects = list()

		for values in self._cursor.fetchall():

			tmp_object = class_ref()

			for i, c in enumerate(tuple(columns.split(", "))):

				setattr(tmp_object, c, values[i])

			list_of_objects.append(tmp_object)


		return list_of_objects



	def _filling_liaison_table(self, object_linked, liaison_data):
		"""In charge of C part of CRUD (create), for inserting data
			in a liaison table in DB

		Args:

			object_linked (model object): Model object linked to the liaison
				table by a many to many relation
			liaison_data (list): Model objects to insert in 
			the liaison table with the object_linked

		"""

		table = object_linked.TABLE_NAME + '_' + liaison_data[0].TABLE_NAME
		columns = f"{object_linked.TABLE_NAME + '_id' + ', ' + liaison_data[0].TABLE_NAME + '_id'}"
		replacement = self._get_placeholders(len(tuple(columns.split(', '))))

		list_of_values = list()

		# For each object in liaison data
		# Getting the id attribute of it
		for an_object in liaison_data:
			list_of_values.append((object_linked.id, an_object.id))

		self._cursor.executemany(f"INSERT INTO {table} ({columns}) VALUES ({replacement})", list_of_values)

		self._cnx.commit()



	def _is_there_relation(self, object_to_inspect):
		"""Looking for an type list attr, which represent a many to many
			relation

		Args: 

			object_to_inspect (model object): Model object to inspect


		Return:

			Bool: Return True if there is many to many relation, False
				otherwise

		"""

		for attr in object_to_inspect.__dict__.values():

			# If attr is a list and containing data, i.e. existing relation
			if isinstance(attr, list) and len(attr) > 0 :

				return True

		return False



	def _get_liaison_data(self, object_to_inspect):
		"""Looking for data to insert in a liaison table, wich may contain
			in a type list attribute

		Args:

			object_to_inspect (model object): Model object inspect

		"""

		for attr in object_to_inspect.__dict__.values():

			if isinstance(attr, list):

				return attr



	def _get_columns(self, object_to_inspect):
		"""In charge of collecting attributes names of an object

		Args:

			object_to_inspect: Model object from which we want attributes 
				who represente columns in database

		Returns:

			columns (tuple): Tuple of columns of the table in DB

		"""

		all_attr = object_to_inspect.__dict__
		
		return ", ".join(attr  
						 for i, attr in enumerate(all_attr)
						 if i < object_to_inspect.COLUMNS
						)



	def _get_values(self, object_to_inspect, columns):
		"""In charge of collecting attributes values of an object

		Args:

			object_to_inspect (model object): Model object to inspect
			columns (tuple): Represent attributes names of the object

		Returns:

			values (tuple): Tuple of values to insert in the DB

		"""

		return tuple(getattr(object_to_inspect, c) for c in columns)



	def _get_placeholders(self, reference):
		"""In charge of setting a tuple of sql placeholders regarding the size
			of another tuple argument

		Args:

			reference (int): How much sql placeholders needs to be define

		Returns:

			placeholders (tuple): Same size tuple as values, containing sql
				placeholders

		"""

		return ", ".join('%s' for i in range(reference))



	def _get_back_id(self):
		"""Return last inserted id

		Return 

			id (int): Last inserted id in DB

		"""

		self._cursor.execute("SELECT LAST_INSERT_ID()")

		return self._cursor.fetchall()[0][0]



	def _get_where_clause(self, **kwargs):
		"""Take a keyword argument and return a pair of key/values as strings

		Args:

			kwargs (dict): Keyword argument

		Return:

			key (str): Key as string
			value (str): Value as string

		"""

		key = next((f"{i}" for i in kwargs.keys()))
		value = f"{kwargs[key]}"

		return key, value