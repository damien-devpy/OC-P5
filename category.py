# coding: utf-8

class Category:
	"""Model class of the category table in database
	"""

	TABLE_NAME = "category"

	def __init__(self,
				 id_cat=None,
			     name=None,
			     manager_object=None,
			     cursor_object=None,
			    ):

		"""init method

		Args:

			id_cat (int): id of the category set by DB
			name (str): name of the category

			manager_object (manager object): Gave access to the manager
			cursor_object (cursor object): Needed for managing DB

		Attributes:

			self._manager (manager object): attribute from the argument
			self._object (cursor object): attribute from the argument

			self._id_cat (int): attribute that represent id column in DB
			self._name (str): attribute that represent name column in DB

			self._buffer (list): Container for category_objects for a massive insert

		"""

		self._id_cat = id_cat
		self._name = name

		self._manager = manager_object
		self._cursor = cursor_object

		self._buffer = list()


	def save(self):
		"""Insert data in DB, through the manager

		"""

		columns = tuple de (self.__dict[1][0])
		values = tuple de (self._name)

		self._manager.insert(self._cursor, Category.TABLE_NAME, columns, values)


	def save_all(self):
		"""Insert all data in buffer, in DB, trough the manager
		"""

		columns = tuple de (self.__dict[1][0])

		self._buffer = liste de [tuple de(category_object.name) pour chaque catégory_object dans self._buffer]

		self._manager.insert(self._cursor, Category.TABLE_NAME, columns, self._buffer)


	def read(self, columns='*'):
		"""Reading data from DB, through the manager

		Args:

			columns (tuple): Tuple of string on which columns we want to read data.
				Default to *, meaning all of them.

		Returns:

			result (list): List of category_object 

		"""

		si columns == '*':

			columns = tuple de (self.__dict[1][0])

		manager_object.select(self._cursor, Category.TABLE_NAME, columns)

		resultat <- liste

		pour chaque élément dans self._cursor:
			si la longueur de columns == longueur de élément:

				r = Category(*élément)
			
			sinon:

				tmp_kwargs = {columns[i]:élément[i] pour chaque i dans élément}
				r = Category(**tmp_kwargs)

			resultat <- r

		fin pour

		retourner resultat


	def __add__(self, category_object):
		"""Allow to use the add operator between category_objects
			Result in a list of category_object

		Args:

			category_object (category object): Model representing category table in DB

		"""

		self._buffer.append(category_object)