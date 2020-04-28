# coding: utf-8

class CategoryAndProduct:
    """Model class of the category_and_product table in database
    """

    TABLE_NAME = "category_and_product"

    def __init__(self, manager_object, cursor_object, **kwargs):
		"""init method

		Args:

			manager_object (manager object): Gave access to the manager
			cursor_object (cursor object): Needed for managing DB
			kwargs (dict): Variable number of keywords arguments and  type (id (int), name (str), barre_code (int), ...)

		Attributes:
			
			self._manager (manager object): attribute from the argument
			self._object (cursor object): attribute from the argument
			self._category_id (int): attribute that represent category_id column in DB
			self._product_barre_code (int): attribute that represent product_barre_code column in DB
			self._filter (bool): Default to False. Else, contain string like 'column=value' if the user want to add 
				a where clause to a query

        """

        self._manager = manager_object
        self._cursor = cursor_object
        self._category_id = kwargs.get('category_id')
        self._product_barre_code = kwargs.get('product_barre_code')
        self._filter = False


	def save(self):
		"""Insert data in DB, through a manager

		"""

		columns = tuple de(élément[0] de élément dans self.__dict__)
		values = tuple de(élément[1] de élément dans self.__dict__)

		self._manager.insert(self._cursor, CategoryAndProduct.TABLE_NAME, columns, values)


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
			colums = tuple de(élément[0] de élément dans self.__dict__)

		si self._filter est vrai:

			self._manager.select(self._cursor, Product.TABLE_NAME, columns, where=self._filter)

		sinon:

			self._manager.select(self._cursor, Product.TABLE_NAME, columns)

