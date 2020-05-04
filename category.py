# coding: utf-8

class Category(Model):
	"""Model class of the category table in database
	"""

	TABLE_NAME = "category"

	def __init__(self, **kwargs):
		"""init method

		Args:

			**kwargs (dict): Variable number of arguments

		Attributes:

			self._id_cat (int): attribute that represent id column in DB
			self._name (str): attribute that represent name column in DB

		"""

		Model.__init__(self)

		self._id = kwargs.get['id']
		self._name = kwargs.get['name']