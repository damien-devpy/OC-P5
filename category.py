# coding: utf-8

class Category:
	"""Model class of the category table in database
	"""

	TABLE_NAME = "category"

	def __init__(self, manager_object=None, cursor_object=None, **kwargs):
		"""init method

		Args:

			manager_object (manager object): Gave access to the manager
			cursor_object (cursor object): Needed for managing DB
			kwargs (dict): Variable number of keywords arguments and  type (id (int), name (str), barre_code (int), ...)

		Attributes:

			self._manager (manager object): attribute from the argument
			self._object (cursor object): attribute from the argument
			self._id (int): attribute that represent id column in DB
			self._name (str): attribute that represent name column in DB

		"""
		
		self._manager = manager_object
		self._cursor = cursor_object
		self._id = kwargs.get('id')
		self._name = kwargs.get('name')

	def save(self):
		"""Insert data in DB, through a manager

		"""

		columns = tuple de (élément[0] de élément dans self.__dict__)
		values = tuple de (élément[1] de élément dans self.__dict__)

		self._manager.insert(self._cursor, Category.TABLE_NAME, columns, values)

	def read(self, columns='*'):
		"""Reading data from DB, through a manager

		Args:

			columns (tuple): Tuple of string on which columns we want to read data.
				Default to *, meaning all of them.

		Returns:

			result (list): List of category_object 

		"""

		si columns == '*':

			columns = tuple (élément[0] de élément dans self.__dict__)

		manager_object.select(self._cursor, Category.TABLE_NAME, columns)

		resultat <- liste

		pour chaque élément dans self._cursor:
			r = Category('id':élément[0], 'name':élément[1])

			resultat <- r

		fin pour

		retourner resultat