# coding: utf-8

from mysql import connector
from configuration import (DATABASE,
						   CREDENTIALS,
						  )
import pdb
from copy import copy

class Manager:
	"""In chage of managing data base
	"""

	cnx = connector.connect(user=CREDENTIALS['user'],
							host=CREDENTIALS['host'],
							password=CREDENTIALS['password'],
						   )

	cursor = cnx.cursor()


	def __init__(self):

		self._cursor = Manager.cursor
		self._cnx = Manager.cnx



	def create_db(self):
		"""Creating the database from a sql file
		"""

		with open(DATABASE, mode='r', encoding='utf-8') as sql_file:
			for line in sql_file:
				self._cursor.execute(line)



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
				self.insert(an_object, set_id=True)

				data_liaison_table = self._get_liaison_data(an_object)
				
				# Filling table for every objects in data_liaison_table
				for liaison_object in data_liaison_table:
					
					self.insert(liaison_object, set_id=True)

				# After inserting every objects in their proper tables
				# Filling the liaison table
				self._filling_liaison_table(an_object, data_liaison_table)

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

		table = object_to_insert.TABLE_NAME
		columns = self._get_columns(object_to_insert)
		values = self._get_values(object_to_insert, tuple(columns.split(', ')))
		replacement = self._get_placeholders(values)
		duplicate_key = "ON DUPLICATE KEY UPDATE id = LAST_INSERT_ID(id)"

		query = f"INSERT INTO {table} ({columns}) VALUES ({replacement}) {duplicate_key}"

		self._cursor.execute(query, values)

		if set_id:

			fresh_id = self._get_back_id()

			setattr(object_to_insert, 'id', fresh_id)


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

		# If a specific column is asked
		if column:

			return self._select_column(object_to_read, column)

		# Elif, a specific row is asked
		elif kwargs:

			self._select_row(object_to_read, **kwargs)

		# Else, an entire table is asked
		else:

			return self._select_table(object_to_read)



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

		self._cursor.execute(f"SELECT ({column}) FROM {table}")

		list_of_values = list()

		for value in self._cursor.fetchall():
			setattr(object_to_read, column, value[0])
			list_of_values.append(copy(object_to_read))


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
		columns = self._get_columns(object_to_read)

		# Building where clause from the keyword argument
		keyword = [f'{i}={j}' for i, j in kwargs.items()][0]

		self._cursor.execute(f"SELECT ({columns}) FROM {table} WHERE {keyword}")

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

		columns = self._get_columns(object_to_read)

		self._cursor.execute(f"SELECT ({columns}) FROM {table}")

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
			liaison_data (list): Model objects to insert in 
			the liaison table with the object_linked

		"""

		table = object_linked.TABLE_NAME + '_' + liaison_data[0].TABLE_NAME
		columns = f"{object_linked.TABLE_NAME + '_id' + ', ' + liaison_data[0].TABLE_NAME + '_id'}"
		replacement = self._get_placeholders(tuple(columns.split(', ')))

		list_of_values = list()

		# For each object in liaison data
		# Getting the id attribute of it
		for an_object in liaison_data:
			list_of_values.append((object_linked.id, an_object.id))

		self._cursor.executemany(f"INSERT INTO {table} ({columns}) VALUES ({replacement})", list_of_values)



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

			object_to_inspect (model object): Model object to inspect

		Returns:

			columns (tuple): Tuple of columns of the table in DB

		"""

		all_attr = object_to_inspect.__dict__
		columns = []

		for i, attr in enumerate(all_attr):

			# If current attr not a manager either a many to many relation
			if i > 1 and not isinstance(all_attr[attr], list):

				columns.append(attr)


		return ", ".join(columns)



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

		return ", ".join('%s' for i in range(len(reference)))



	def _get_back_id(self):
		"""Return last inserted id

		Return 

			id (int): Last inserted id in DB

		"""

		self._cursor.execute("SELECT LAST_INSERT_ID()")

		return self._cursor.fetchall()[0][0]