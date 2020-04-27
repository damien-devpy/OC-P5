# coding: utf-8

class Product:
	"""Model class of the product table in database
	"""

	TABLE_NAME = "product"

	def __init__(self, barre_code, name, nutrition_grade, brand, ingredients, quantity):
		"""init method

		Attributes:

			barre_code	(int): column barre_code in product table
			name (str): column name in product table
			nutrition_grade (str): column nutrition_grade in product table
			brand (str): column brand in product table
			ingredients (str): column ingredients in product table
			quantity (str): column quantity in product table

		"""

		self._barre_code = barre_code
		self._name = name
		self._nutrition_grade = nutrition_grade
		self._brand = brand
		self._ingredients = ingredients
		self._quantity = quantity


	def save(self, manager_object, cursor_object):
		"""Saving data in DB, through a manager

		Args:

			manager_object (object manager): Gave access to insert method manager
			cursor_object (object cursor): Needed for managing DB

		"""

		manager_object.insert(cursor_object, Product.TABLE_NAME, columns_name, (self._barre_code,
																				self._name,
																				self._nutrition_grade,
																				self._brand,
																				self._ingredients,
																				self._quantity,
																			   )
							 )

	def read(self, manager_object, cursor_object, columns='*'):
		"""Reading data from DB, through a manager

		Args:

			manager_object (object manager): Gave access to select method manager
			cursor_object (object cursor): Needed for managing DB

		"""

		si columns == '*':
			colums <- toutes les colonnes

		manager_object.select(cursor_object, Product.TABLE_NAME, columns)

