# coding: utf-8

class Product:
	"""Model class of the product table in database
	"""

	TABLE_NAME = "product"

	def __init__(self, manager_object=None, cursor_object=None, **kwargs):
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


	def save(self):
		"""Insert data in DB, through a manager

		"""

		columns = tuple de(élément[0] de élément dans self.__dict__)
		values = tuple de(élément[1] de élément dans self.__dict__)

		self._manager.insert(self._cursor, Product.TABLE_NAME, columns_, values)

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
			self._manager.select(self._cursor, Product.TABLE_NAME, colums)

		resultat <- liste

		pour chaque élément dans self._cursor:
			r = Product('barre_code': élément[0],
						'name': élément[1],
						'nutrition_grade': élément[2],
						'brand': élément[3],
						'ingredients': élément[4]
						'quantity': élément[5],)

			ajouter r à résultat

		fin pour

		retourner résultat




