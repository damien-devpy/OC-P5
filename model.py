# coding: utf-8

from manager import Manager

class Model:
	"""Model class representing table database
	"""

	def save(self, manager_object):
		"""Used for insert data through the manager

		Args:

			manager_object (manager object): Needed for acces to manager 
				methods

		"""

		manager_object.insert(self)



	def get(self, manager_object, **kwargs):
		"""Used to get data from a specific key/value keyword argument

		Args:

			manager_object (manager object): Needed for acces to manager 
				methods
			kwargs (dict): Keyword argument for getting a specific row

		"""

		manager_object.select(self, **kwargs)