# coding: utf-8

from re import sub
from re import compile as re_compile

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
				Default to None.
			cursor_object (cursor object): Needed for managing DB
				Default to None.
			**kwargs (dict): Variable number of arguments

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

			self._pattern (regular expression) : Contain a compiled regular expression

		"""

		self._manager = manager_object
		self._cursor = cursor_object

		self._barre_code = kwargs.get['barre_code']
		self._name = kwargs.get['name']
		self._nutrition_grade = kwargs.get['nutrition_grade']
		self._brand = kwargs.get['brand']
		self._ingredients = kwargs.get['ingredients']
		self._quantity = kwargs.get['quantity']
		
		self._filter = False
		self._buffer = list()

		self._pattern = re_compile(r'[_]')

		columns = (self.__dict__[2][0],
				   self.__dict[3][0],
				   self.__dict[4][0],
				   self.__dict[5][0],
				   self.__dict[6][0],
				   self.__dict[7][0],
				  )

	    # Getting rid of the underscore sign of the attribute
		# gives columns names in DB
		self._columns = tuple(sub(self._pattern, '', attr) for attr in columns)

	def save(self):
		"""Insert data in DB, through a manager

		"""

		values = (self._barre_code,
				  self._name,
				  self._nutrition_grade,
				  self._brand,
				  self._ingredients,
				  self._quantity,
				 )

		self._manager.insert(self._cursor, Product.TABLE_NAME, self._columns, values)


	def save_all(self):
		"""Insert all data in buffer, in DB, trough the manager
		"""

		self._manager.insert(self._cursor, Product.TABLE_NAME, self._columns, self._buffer)


	def filter_by(self, where_clause):
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

			result (list): List of product_object 

		"""

		if columns == '*':
			columns = self._columns

		# If a where clause exist
		if self._filter:

			self._manager.select(self._cursor, Product.TABLE_NAME, columns, where=self._filter)
			self._filter = False

		else:

			self._manager.select(self._cursor, Product.TABLE_NAME, columns)

		# Storing result of the query in a list
		result = list()

		# For each row
		for element in self._cursor:

			# Temporary kwargs containing columns and data related read from
			# the DB. 
			tmp_kwargs = {columns[i]:element[i] for i in element}
			r = Product(**tmp_kwargs)

			result.append(r)

		return result


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
		self._barre_code = substitute.get['barre_code']
		self._name = substitute.get['name']
		self._nutrition_grade = substitute.get['nutrition_grade']
		self._brand = substitute.get['brand']
		self._ingredients = substitute.get['ingredients']
		self._quantity substitute.get['quantity']


	def __add__(self, product_object):
		"""Allow to use the add operator between product_objects
			Result in a list of product_object

		Args:

			product_object (product object): product to add to the buffer
			
		"""

		# Adding to the buffer a tuple containing object attributes
		self._buffer.append((product_object.barre_code,
		 				 	 product_object.name,
		 				 	 product_object.nutrition_grade,
		 				 	 product_object.brand,
		 				 	 product_object.ingredients,
		 				 	 product_object.quantity,
		 				    )
						   )



