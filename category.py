# coding: utf-8

from re import sub
from re import compile as re_compile

class Category:
	"""Model class of the category table in database
	"""

	TABLE_NAME = "category"

	def __init__(self,
				 manager_object=None,
				 cursor_object=None,
				 **kwargs
			    ):
		"""init method

		Args:

			manager_object (manager object): Gave access to the manager
			cursor_object (cursor object): Needed for managing DB
			**kwargs (dict): Variable number of arguments

		Attributes:

			self._manager (manager object): attribute from the argument
			self._object (cursor object): attribute from the argument

			self._id_cat (int): attribute that represent id column in DB
			self._name (str): attribute that represent name column in DB

			self._buffer (list): Container for category_objects for a massive insert

		"""

		self._manager = manager_object
		self._cursor = cursor_object

		self._id_cat = kwargs.get['id_cat']
		self._name = kwargs.get['name']

		self._buffer = list()

		self._pattern = re_compile(r'[_]')

		columns = (self.__dict[2][0],
				   self.__dict[3][0],
				  )

		self._columns = tuple(sub(self._pattern,
								  '',
								  columns,
								 )
							 )


	def save(self):
		"""Insert data in DB, through the manager

		"""

		columns = tuple(self._columns[1])

		values = (self._name,)

		self._manager.insert(self._cursor, Category.TABLE_NAME, self._columns, values)


	def save_all(self):
		"""Insert all data in buffer, in DB, trough the manager
		"""

		# id category is an auto_increment column in DB, so we don't need to manage it
		# Forward only attribute name
		columns = tuple(self._columns[1])

		self._manager.insert(self._cursor, Category.TABLE_NAME, self._colums, self._buffer)


	def read(self, columns='*'):
		"""Reading data from DB, through the manager

		Args:

			columns (tuple): Tuple of string on which columns we want to read data.
				Default to *, meaning all of them.

		Returns:

			result (list): List of category_object 

		"""

		if columns == '*':

			columns = self._columns

		self._manager.select(self._cursor, Category.TABLE_NAME, columns)

		# Storing result of the query in a list
		result = list()

		# For each row
		for element in self._cursor:

			# Temporary kwargs containing columns and data related read from
			# the DB.
			tmp_kwargs = {columns[i]:element[i] for i in element}
			r = Category(**tmp_kwargs)

			result.append(r)

		return result


	def __add__(self, category_object):
		"""Allow to use the add operator between category_objects
			Result in a list of category_object

		Args:

			category_object (category object): Model representing category table in DB

		"""

		# Adding to the buffer a tuple containing object attributes
		self._buffer.append((category_object.name,))