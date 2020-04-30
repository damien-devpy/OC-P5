# coding: utf-8

import mysql.connector

class Manager:
	"""In chage of managing data base
	"""


	def select(self, cursor_object, table, columns, where_clause=False):
		"""In charge of R part of CRUD (read)

		Args:

			cursor_object (cursor object): needed for managing DB
			table (str): name of the table to read
			columns (tuple): columns to read
			where_clause (bool): Default to False. If not, contain a string looking
				like 'column=value' for the keyword WHERE in a query

		"""

		if where_clause:

			cursor_object.execute(f'SELECT {columns} FROM table WHERE {where_clause}')

		else:

			cursor_object.execute(f'SELECT {columns} FROM table')

		


	def insert(self, cursor_object, table, columns, values):
		"""In charge of C part of CRUD (create)

		Args:

			cursor_object (cursor object): need for managing DB
			table (str): name of the table to read
			columns (tuple of str): columns in wich we want to insert data
			values (tuple): data to insert
			
		"""

		replacement = f'({", ".join('%s' for i in columns)})'

		# If values is a list of values
		if isinstance(values, list):

			cursor_object.executemany(f'INSERT INTO table {columns} VALUES {replacement}', values)

		else:

			cursor_object.execute(f'INSERT INTO table {columns} VALUES {replacement}', values)


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