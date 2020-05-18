# coding: utf-8

from model.model import Model

class Category(Model):
	"""Model class of the category table in database
	"""

	# Table name in database this model class represent
	TABLE_NAME = "category"
	
	# How much columns this model class has as attributes
	# in declaration order
	COLUMNS = 2

	def __init__(self, **kwargs):
		"""init method

		Args:

			**kwargs (dict): Variable number of arguments

		Attributes:

			self._id_cat (int): attribute that represent id column in DB
			self._name (str): attribute that represent name column in DB

		"""

		self.id = kwargs.get('id')
		self.name = kwargs.get('name')

		Model.__init__(self)
		self.duplicate_key = True
		self.liaison_table = "product"