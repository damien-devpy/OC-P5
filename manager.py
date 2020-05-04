# coding: utf-8

from mysql import connector
from configuration import USER

class Manager:
	"""In chage of managing data base
	"""

	def __init__(self):
		"""

		Args: 

			self._cnx (object connector): Used to connect to the DB
			self._cursor (object cursor): Used to interact (i.e select, create)
				with the DB

		"""

		self._cnx = connector.connect(USER)
		self._cursor = self._cnx.cursor()


	def insert_all(self, list_of_objects):
		"""In charge of C part of CRUD (create), for a massive insert

		Args:

			list_of_objects (list): A list of objects to insert at once in DB

		"""

		# Before inserting data in DB, checking if the object contain
		# a relation to any liaison table
		relation_exist = _is_there_relation(list_of_objects[0])

		if relation_exist:

			for an_object in list_of_objects:

				# Filling table with the current object
				insert(an_object, set_id=True)

				data_liaison_table = _get_liaison_data(an_object)

				# Filling the liaison table with the data to insert in it
				# and the current object linked with
				_filling_liaison_table(an_object, data_liaison_table)

			self._cnx.commit()

		else:

			for an_object in list_of_objects:

				insert(an_object, set_id=True)

			self._cnx.commit()



	def insert(self, object_to_insert, set_id=False):
		"""In charge of C part of CRUD (create), for inserting data in DB

		Args:

			object_to_insert (model object): Model object to insert in database
			set_id (bool): If id has to get back after insertion in DB and
				attribute object set to id value. Default to False.

		"""

		table = object_to_inspect.TABLE_NAME
		columns = _get_columns(object_to_inspect)
		values = _get_values(object_to_inspect, columns)
		replacement = _get_placeholders(values)

		self._cursor.execute(f"INSERT INTO {table} {columns} VALUES {replacement}", values)

		if set_id:

			fresh_id = _get_back_id()

			setattr(object_to_inspect, 'id', fresh_id)


	def select(self, object_to_read, column=None, **kwargs):
		"""In charge of R part of CRUD (read), for selecting data in DB

		Args:

			object_to_read (model object): Model object used to select table to
				read, and filled with informations from DB if a specific row
				where asked

			column (str): Default to None. Otherwise, meaning method has to
				look for a specific column in the table DB

			**kwargs (dict): Keyword argument for looking a specific row

		Return:

		"""

		table = object_to_read.TABLE_NAME

		# If a specific column is asked
		if column:

			return _select_column(self, object_to_read, column)

		# Elif, a specific row is asked
		elif kwargs:

			_select_row(self, object_to_read, **kwargs)

		# Else, an entire table is asked
		else:

			return _select_table(self, object_to_read)



	def substitution(self, cursor_object, user_category, nutrition_grade_to_substitute):
		"""Specifically in charge for looking a product substitution
		"""

		cursor_object.execute(f"""SELECT barre_code, MIN(nutrition_grade)
												FROM (
												SELECT product.barre_code, product.nutrition_grade FROM product
												INNER JOIN category_and_products
												ON product.barre_code = category_and_product.product_barre_code
												INNER JOIN category_and_products as c_a_p
												ON category_and_product.category_id = c_a_p.category_id
												WHERE product.nutrition_grade < {nutrition_grade_to_substitute}
													AND category_and_product.category_id = {user_category}
												) as minimal_nutriscore;)"""
												)



	def _select_column(self, object_to_read, column):
		"""Private method for reading a specific column in table from the
			database

		Args: 

			object_to_read (model object): Model object used to select table to
			read
			columns (str): Specific column to look for in the table

		"""

		table = object_to_read.TABLE_NAME

		self._cursor.execute(f"SELECT {column} FROM {table}")

		list_of_values = list()

		for value in self._cursor.fetchall()
			object_to_read.column = value[0]
			list_of_values.append(object_to_read)

		return list_of_values



	def _select_row(self, object_to_read, **kwargs):
		"""Private method for getting a specific row in a table from the
			database

		Args:

			object_to_read (model object): Model object used to select table to
			read, and filled with information of the specific row
			kwargs (dict): Keyword argument for a specific row

		"""

		table = object_to_read.TABLE_NAME
		columns = _get_columns(object_to_read)

		# Building where clause from the keyword argument
		keyword = [f'{i}={j}' for i, j in kwargs.items()][0]

		self._cursor.execute(f"SELECT {columns} FROM {table} WHERE {keyword}")

		# Getting the result of the query
		result = self._cursor.fetchone()

		# Filling attributes object with result
		for i, c in enumerate(columns):
			object_to_read.c = result[i]



	def _select_table(self, object_to_read):
		"""Private method for getting an entire table from the database

		Args:

			object_to_read (model object): Model object used to select table to
			read

		"""

		columns = _get_columns(object_to_read)

		self._cursor.execute(f"SELECT {columns} FROM {table}")

		list_of_objects = list()

		for values in self._cursor.fetchall():

			for i, c in enumerate(columns):
				object_to_read.c = values[i]

			list_of_objects.append(object_to_read)


		return list_of_objects



	def _filling_liaison_table(self, object_linked, liaison_data):
		"""In charge of C part of CRUD (create), for inserting data
			in a liaison table in DB

		Args:

			object_linked (model object): Model object linked to the liaison
				table by a many to many relation
			liaison_data (list): List of data from model object to insert in 
			the liaison table regarding the object_linked

		"""

		table = object_linked.TABLE_NAME + '_' liaison_data[0].TABLE_NAME
		columns = (object_linked.TABLE_NAME + '_id', 
				   liaison_data.TABLE_NAME+ '_id')
		replacement = _get_placeholders(columns)

		list_of_values = list()

		# For each object in liaison data
		# Getting the attribute id of it
		for an_object in liaison_data:
			list_of_values.append((object_linked.id, an_object.id))

		self._cursor.executemany(f"INSERT INTO {table} {columns} VALUES {replacement}", list_of_values)



	def _is_there_relation(self, object_to_inspect):
		"""Looking for an type list attr, which represent a many to many
			relation

		Args: 

			object_to_inspect (model object): Model object inspect


		Return:

			Bool: Return True if there is many to many relation, False
				otherwise

		"""

		for attr in object_to_inspect.__dict__.values():

			if isinstance(attr, list):

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

			object_to_inspect (model object): Model object to inspect

		Returns:

			columns (tuple): Tuple of columns of the table in DB

		"""

		all_attr = object_to_inspect.__dict__
		columns = []

		for i, attr in enumerate(all_attr):

			# If current attr not a manager either a many to many relation
			if i > 1 and not isinstance(attr, list):

				columns.append(attr)


		return tuple(columns)



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

			reference (tuple): How much sql placeholders needs to be define

		Returns:

			placeholders (tuple): Same size tuple as values, containing sql
				placeholders

		"""

		return tuple([", ".join('%s' for i in range(len(reference)))])



	def _get_back_id(self):
		"""Return last inserted id

		Return 

			id (int): Last inserted id in DB

		"""

		self._cursor.execute('LAST_INSERT_ID()')

		return self._cursor.fetchall()[0]