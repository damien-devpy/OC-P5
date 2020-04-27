# coding: utf-8

class Category:
	"""Model class of the category table in database
	"""

	TABLE_NAME = "category"

	def __init__(self, id_cat=None, name):
		"""init method

		Attributes:

			id (int): id column in category table
			name (str): name column in category 

		"""

		self._id = id_cat
		self._name = name

	def save(self, manager_object, cursor_object):
		"""Saving data in DB, through a manager

		Args:

			manager_object (object manager): Gave access to insert method manager
			cursor_object (object cursor): Needed for managing DB

		"""

		manager_object.insert(cursor_object, Category.TABLE_NAME, column_name, self._name)

	def read(self, manager_object, cursor_object, columns='*'):
		"""Reading data from DB, through a manager

		Args:

			manager_object (object manager): Gave access to select method manager
			cursor_object (object cursor): Needed for managing DB

		"""

		si columns == '*':

			columns <- toutes les colonnes

		manager_object.select(cursor_object, Category.TABLE_NAME, columns)