# coding: utf-8

from model.model import Model
from orm.manager import Manager
import model.category

class Product(Model):
	"""Model class of the product table in database
	"""

	# Table name in database this model class represent
	TABLE_NAME = "product"

	# How much columns this model class has as attributes
	# in declaration order
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

		Model.__init__(self)
		self.liaison_table = model.category.Category


	def get_substitute(self, chosen_category):
		"""Looking for a product substitute, through the manager
			and the substition method
			
		Args:

			chosen_category (str): Category choosed by user, for a product substitution

		"""

		manager = Manager()
		manager.set_db()

		manager.substitution(self, chosen_category)


