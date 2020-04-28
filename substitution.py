# coding: utf-8

class Substitution:
	"""Model class of substitution table in database
	"""

	TABLE_NAME = "substitution"

	def __init__(self, manager_object, cursor_object, **kwargs):
		"""init method

		Args:

			manager_object (manager object): Gave access to the manager
			cursor_object (cursor object): Needed for managing DB
			kwargs (dict): Variable number of keywords arguments and  type (id (int), name (str), barre_code (int), ...)

		Attributes:

			self._manager (manager object): attribute from the argument
			self._object (cursor object): attribute from the argument
			self._barre_code_to_substitute (int): attribute that represent barre_code_to_substitute column in DB
 			self._barre_code_substitute (int): attribute that represent barre_code_substitute column in DB

		"""

		self._manager = manager_object
        self._cursor = cursor_object
        self._barre_code_to_substitute = kwargs.get('barre_code_to_substitute')
        self._barre_code_substitute = kwargs.get('barre_code_substitute')


    def save(self):
		"""Insert data in DB, through a manager

		"""

		self._manager.insert()

