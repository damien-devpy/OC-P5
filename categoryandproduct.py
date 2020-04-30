# coding: utf-8

from re import sub
from re import compile as re_compile

class CategoryAndProduct:
    """Model class of the category_and_product table in database
    """

    TABLE_NAME = "category_and_product"

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

			self._category_id (int): attribute that represent category_id column in DB
			self._product_barre_code (int): attribute that represent product_barre_code column in DB

			self._filter (bool): Default to False. Else, contain string like 'column=value' if the user want to add 
				a where clause to a query
			self._buffer (list): Container for category_objects for a massive insert

        """

        self._manager = manager_object
        self._cursor = cursor_object

        self._category_id = kwargs.get['category_id']
        self._product_barre_code = kwargs.get['product_barre_code']

        self._filter = False
        self._buffer = list()

		self._pattern = re_compile(r'[_]')

        columns = (self.__dict__[2][0], 
        		   self.__dict__[3][0],
        		  )

        self._columns = tuple(sub(self._pattern,
        						  '',
        						  columns,
        						 )
       						 )


	def save(self):
		"""Insert data in DB, through a manager

		"""

		values = (self._category_id,
				  self._product_barre_code,
				 )

		self._manager.insert(self._cursor, CategoryAndProduct.TABLE_NAME, self._columns, values)


	def save_all(self):
		"""Insert all data in buffer, in DB, trough the manager
		"""

		self._manager.insert(self._cursor, CategoryAndProduct.TABLE_NAME, self._columns, self._buffer)

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

		if columns == '*':
			columns = self._columns


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
			r = CategoryAndProduct(**tmp_kwargs)

			result.append(r)

		return result


	def __add__(self, cap_object):
		"""Allow to use the add operator between product_objects
			Result in a list of cap_object

		Args:

			cap_object (categoryandproduct_object): cap object to add to the buffer
			
		"""
		
		# Adding to the buffer a tuple containing object attributes
		self._buffer.append((cap_object.category_id,
							 product_barre_code,
							)
						   )
