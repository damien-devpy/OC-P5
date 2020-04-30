# coding: utf-8

from re import sub
from re import compile as re_compile

class Substitution:
	"""Model class of substitution table in database
	"""

	TABLE_NAME = "substitution"

	def __init__(self, 
				 manager_object=None,
				 cursor_object=None,
				 **kwargs,
				):
		"""init method

		Args:

			manager_object (manager object): Gave access to the manager
			cursor_object (cursor object): Needed for managing DB
			**kwargs (dict): Variable number of arguments

		Attributes:

			self._manager (manager object): attribute from the argument
			self._object (cursor object): attribute from the argument
			self._barre_code_to_substitute (int): attribute that represent barre_code_to_substitute column in DB
 			self._barre_code_substitute (int): attribute that represent barre_code_substitute column in DB

		"""

		self._manager = manager_object
        self._cursor = cursor_object

        self._barre_code_to_substitute = kwargs.get['barre_code_to_substitute']
        self._barre_code_substitute = kwargs.get['barre_code_substitute']

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

		values = (self._barre_code_to_substitute,
				  self._barre_code_substitute,
				 )

		self._manager.insert(self._cursor, Substitution.TABLE_NAME, self._columns, values)

	def read(self, columns='*'):
		"""Reading data from DB, through a manager

		Args:

			columns (tuple): Tuple of string on which columns we want to read data.
				Default to *, meaning all of them.

		Returns:

			result (list): List of substitution_object

		"""

		if columns == '*':
			columns = self._columns

		self._manager.insert(self._cursor, Substitution.TABLE_NAME, columns)
		
		# Storing result of the query in a list
		result = list()

		# For each row
		for element in self._cursor:*

			# Temporary kwargs containing columns and data related read from
			# the DB. 
			tmp_kwargs = {columns[i]:élément[i] for i in element}
			r = Substitution(**tmp_kwargs)

			result.append(r)

		return result

