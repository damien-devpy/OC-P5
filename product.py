# coding: utf-8

class Product:
	"""Model class of the product table in database
	"""

	def __init__(self):
		"""init method

		Attributes:

			barre_code	(int): column barre_code in product table
			name (str): column name in product table
			nutrition_grade (str): column nutrition_grade in product table
			brand (str): column brand in product table
			ingredients (str): column ingredients in product table
			quantity (str): column quantity in product table
			table_name (str): Table name this model represent

		"""

		pass

	def unpacking_values(self, data):
		"""Public method in charge of unpacking values, ffrom catalogue to model, or from DB to model

		Args:

		data (tuple): Contain data to unpack into attributes

		"""

		pour chaque élément dans cursor_object:
			mettre ces attributs dans l''état(self, attr, value)


		pass

