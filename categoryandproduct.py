# coding: utf-8

class CategoryAndProduct:
    """Model class of the category_and_product table in database
    """

    TABLE_NAME = "category_and_product"

    def __init__(self,
    			 category_id=None,
    			 product_barre_code=None,
    			 manager_object=None,
    			 cursor_object=None,
    			):
		"""init method

		Args:

			category_id (int): id of category in table category
			product_barre_code (int): barre_code of a product in product table

			manager_object (manager object): Gave access to the manager
			cursor_object (cursor object): Needed for managing DB

		Attributes:
			
			self._manager (manager object): attribute from the argument
			self._object (cursor object): attribute from the argument

			self._category_id (int): attribute that represent category_id column in DB
			self._product_barre_code (int): attribute that represent product_barre_code column in DB

			self._filter (bool): Default to False. Else, contain string like 'column=value' if the user want to add 
				a where clause to a query
			self._buffer (list): Container for category_objects for a massive insert

        """

        self._category_id = category_id
        self._product_barre_code = product_barre_code

        self._manager = manager_object
        self._cursor = cursor_object

        self._filter = False
        self._buffer = list()


	def save(self):
		"""Insert data in DB, through a manager

		"""

		columns = tuple de(self.__dict__[0][0], self.__dict[1][0])
		values = tuple de(self._category_id, self._product_barre_code)

		self._manager.insert(self._cursor, CategoryAndProduct.TABLE_NAME, columns, values)

	def save_all(self):
		"""Insert all data in buffer, in DB, trough the manager
		"""

		columns = tuple de(self.__dict__[0][0], self.__dict[1][0])

		self._buffer = liste de [tuple de(cap_object.category_id, cap_object.product_barre_code) pour chaque cap_object dans self._buffer]

		self._manager.insert(self._cursor, CategoryAndProduct.TABLE_NAME, columns, self._buffer)


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
			columns = tuple de(self.__dict__[0][0], self.__dict[1][0])

		si self._filter est vrai:

			self._manager.select(self._cursor, Product.TABLE_NAME, columns, where=self._filter)
			self._filter = False

		sinon:

			self._manager.select(self._cursor, Product.TABLE_NAME, columns)

		résultat <- liste

		pour chaque élément dans self._cursor:

			si la longueur de columns == longueur de self.__dict__:

				r = CategoryAndProduct(*élément)

			sinon:

				tmp_kwargs = {columns[i]:élément[i] pour i dans élément}
				r = CategoryAndProduct(**tmp_kwargs)

			résultat <- r

		fin pour

		retourner résultat


