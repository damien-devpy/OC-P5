# coding: utf-8

class Substitution:
	"""Model class of substitution table in database
	"""

	TABLE_NAME = "substitution"

	def __init__(self, 
				 barre_code_to_substitute=None,
				 barre_code_substitute=None,
				 manager_object=None,
				 cursor_object=None,
				):
		"""init method

		Args:

			self._barre_code_to_substitute (int): barre code of the product we want to find a substitute
			self._barre_code_substitute (int): barre code of the product that suit for substitution

			manager_object (manager object): Gave access to the manager
			cursor_object (cursor object): Needed for managing DB

		Attributes:

			self._manager (manager object): attribute from the argument
			self._object (cursor object): attribute from the argument
			self._barre_code_to_substitute (int): attribute that represent barre_code_to_substitute column in DB
 			self._barre_code_substitute (int): attribute that represent barre_code_substitute column in DB

		"""

        self._barre_code_to_substitute = barre_code_to_substitute
        self._barre_code_substitute = barre_code_substitute

		self._manager = manager_object
        self._cursor = cursor_object


    def save(self):
		"""Insert data in DB, through a manager

		"""

		columns <- tuple de(élément[0] de élément dans self.__dict__)
		values <- tuple de(élément[1] de élément dans self.__dict__)

		self._manager.insert(self._cursor, Substitution.TABLE_NAME, colums, values)

	def read(self, columns='*'):
		"""Reading data from DB, through a manager

		Args:

			columns (tuple): Tuple of string on which columns we want to read data.
				Default to *, meaning all of them.

		Returns:

			result (list): List of category_object 

		"""

		si columns == '*':
			columns <- tuple de(élément[0] de élément dans self.__dict__)

		self._manager.insert(self._cursor, Substitution.TABLE_NAME, columns)

		résultat <- liste

		pour chaque élément dans self._cursor:

			si la longueur de columns == longueur de élément:

				r = Substitution(*élément)

			sinon:

				tmp_kwargs = {columns[i]:élément[i] de i dans élément}
				r = Substitution(**tmp_kwargs)

			résultat <- r

		fin pour

		retourner résultat

