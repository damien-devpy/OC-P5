# coding: utf-8

class Model:
	"""Model class representing table database
	"""

	def __init__(self):
		"""

		Args:

			self._manager (object manager): Used to interact with DB

		"""


		self._manager = Manager()


	def save_all(self, list_of_objects):
		"""Used for a massive insert through the manager

		Args:

			list_of_objects (list): A list of objects to insert in DB

		"""

		self._manager.insert_all(list_of_objects)


	def save(self):
		"""Used for insert data through the manager
		"""

		self._manager.insert(self)


	def get_row(self, **kwargs):
		"""Used to get data from a specific key/value keyword argument

		Args:

			kwargs (dict): Keyword argument for getting a specific row

		"""

		self._manager.select(self, **kwargs)


	def find(self, column):
		"""Used to select a specific column in a table DB

		Args:

			column (str): Specific column to look for in a table DB

		Returns:

			list_of_values (list): Return a list of values containing the
				specified column of the table

		"""

		list_of_values = self._manager.select(self, column)

		return list_of_values

	def read(self):
		"""Used to select the entire table in DB

		Returns:

			list_of_values (list): Return a list of tuple, each one containing
				values for all column of the table

		"""

		table = self._manager.select(self)

		return table

