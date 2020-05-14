# coding: utf-8

from model import Model

class Product(Model):
	"""Model class of the product table in database
	"""

	TABLE_NAME = "product"
	COLUMNS = 7

	def __init__(self, **kwargs):
		"""init method

		Args:

			**kwargs (dict): Variable number of arguments

		Attributes:

			self._barre_code (int): attribute that represent barre_code column in DB
			self._name (str): attribute that represent name column in DB
			self._nutrition_grade (str): attribute that represent nutrition_grade column in DB
			self._brand (str): attribute that represent brand column in DB
			self._ingredients (str): attribute that represent ingredients column in DB
			self._quantity (str): attribute that represent quantity column in DB

		"""

		self.id = kwargs.get('id')
		self.barre_code = kwargs.get('barre_code')
		self.name = kwargs.get('name')
		self.nutrition_grade = kwargs.get('nutrition_grade')
		self.brand = kwargs.get('brand')
		self.ingredients = kwargs.get('ingredients')
		self.quantity = kwargs.get('quantity')

		self.belong_to = list()


	def get_substitute(self, user_category):
		"""Looking for a product substitute, through the manager
			and the substition method
		Args:

			user_category (str): Category choosed by user, for a product substitution

		Returns:

			result (tuple): Tuple containing all rows of the product substitute

		"""

		# Searching the DB for a product substitute from the user choice
		self._manager.subsitution(self._cursor, user_category, self._nutrition_grade)

		# Getting the barre_code of the product sustitute
		cb_substitute  = self._cursor[0]

		# Adding a where clause for reading DB where the row equal the barre_code
		# of the product substitute
		self.filter_by(f'barre_code={cb_substitute}')

		# Getting all informations of this product
		substitute = self.read()[0]

		# Making self the product of substitution
		self._barre_code = substitute.get('barre_code')
		self._name = substitute.get('name')
		self._nutrition_grade = substitute.get('nutrition_grade')
		self._brand = substitute.get('brand')
		self._ingredients = substitute.get('ingredients')
		self._quantity = substitute.get('quantity')


