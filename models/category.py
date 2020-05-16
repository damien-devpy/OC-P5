# coding: utf-8

from models.model import Model

class Category(Model):
	"""Model class of the category table in database
	"""

	TABLE_NAME = "category"
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

		# Set this attribute is there is a risk for registering twice the same
		# information in database
		self.duplicate_key = True