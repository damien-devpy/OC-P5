# coding: utf-8

class Product:
	"""Model class of the product table in database
	"""

	TABLE_NAME = "product"

	def __init__(self,
				 manager_object=None,
				 cursor_object=None,
				 **kwargs
				):

		"""init method

		Args:

			manager_object (manager object): Gave access to the manager
			cursor_object (cursor object): Needed for managing DB
			kwargs (dict): Variable number of keywords arguments and  type (id (int), name (str), barre_code (int), ...)

		Attributes:

			self._manager (manager object): attribute from the argument
			self._object (cursor object): attribute from the argument

			self._barre_code (int): attribute that represent barre_code column in DB
			self._name (str): attribute that represent name column in DB
			self._nutrition_grade (str): attribute that represent nutrition_grade column in DB
			self._brand (str): attribute that represent brand column in DB
			self._ingredients (str): attribute that represent ingredients column in DB
			self._quantity (str): attribute that represent quantity column in DB

			self._filter (bool): Default to False. Else, contain string like 'column=value' if the user want to add 
				a where clause to a query
			self._buffer (list): Container for category_objects for a massive insert

		"""

		self._manager = manager_object
		self._cursor = cursor_object

		self._barre_code = kwargs.get('barre_code')
		self._name = kwargs.get('name')
		self._nutrition_grade = kwargs.get('_nutrition_grade')
		self._brand = kwargs.get('brand')
		self._ingredients = kwargs.get('ingredients')
		self._quantity = kwargs.get('quantity')

		self._filter = False
		self._buffer = list()


	def save(self):
		"""Insert data in DB, through a manager

		"""

		columns = tuple de(self.__dict__[2][0],
						   self.__dict[3][0],
						   self.__dict[4][0],
						   self.__dict[5][0],
						   self.__dict[6][0],
						   self.__dict[7][0],)

		values = tuple de(self.__dict__[2][1],
						   self.__dict[3][1],
						   self.__dict[4][1],
						   self.__dict[5][1],
						   self.__dict[6][1],
						   self.__dict[7][1],)

		self._manager.insert(self._cursor, Product.TABLE_NAME, columns_, values)


	def save_all(self):
		"""Insert all data in buffer, in DB, trough the manager
		"""

		colums = tuple de(self.__dict__[2][0],
						   self.__dict[3][0],
						   self.__dict[4][0],
						   self.__dict[5][0],
						   self.__dict[6][0],
						   self.__dict[7][0],)

		self._buffer = liste de[tuple de(product_object.barre_code,
										 product_object.name,
										 product_object.nutrition_grade,
										 product_object.brand,
										 product_object.ingredients,
										 product_object.quantity,) pour chaque product_object dans self._buffer]

		self._manager(self._cursor, Product.TABLE_NAME, columns, self._buffer)

	def filter(self, where_clause):
		"""Allow to a add a where_clause

		Args:

			where_clause (str): String looking like 'column=value' for adding a where clause

		"""

		self._filter = where_clause

	def read(self, columns='*'):
		"""Reading data from DB, through a manager

		Args:

			columns (tuple): Tuple of string on which columns we want to read data.
				Default to *, meaning all of them.

		Returns:

			result (list): List of category_object 

		"""

		si columns == '*':
			columns = tuple de(self.__dict__[2][0],
							   self.__dict[3][0],
							   self.__dict[4][0],
							   self.__dict[5][0],
							   self.__dict[6][0],
							   self.__dict[7][0],)

		si self._filter est vrai:

			self._manager.select(self._cursor, Product.TABLE_NAME, columns, where=self._filter)
			self._filter = False

		sinon:

			self._manager.select(self._cursor, Product.TABLE_NAME, colums)


		resultat <- liste

		pour chaque élément dans self._cursor:

			tmp_kwargs = {columns[i]:élément[i] pour chaque i pour élément}

			r = Product(**tmp_kwargs)

			ajouter r à résultat

		fin pour

		retourner résultat

	def get_substitute(self, user_category):
		"""Looking for a product substitute, through the manager
			and the substition method
		Args:

			user_category (str): Category choosed by user, for a product substitution

		Returns:

			result (tuple): Tuple containing all rows of the product substitute

		"""

		self._manager.subsitution(self._cursor, user_category, self._nutrition_grade)

		cb_substitute <- self._cursor[0]

		self._filter <- f'barre_code={cb_substitute}'

		self.read()

	def __add__(self, product_object):
		"""Allow to use the add operator between product_objects
			Result in a list of product_object

		Args:

			product_object (product object): Model representing product table in DB
			
		"""

		self._buffer.append(product_object)


