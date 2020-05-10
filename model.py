# coding: utf-8

from manager import Manager

class Model:
	"""Model class representing table database
	"""

	def save(self):
		"""Used for insert data through the manager
		"""

		manager = Manager()
		manager.set_db()

		manager.insert(self)



	def get(self, **kwargs):
		"""Used to get data from a specific key/value keyword argument

		Args:

			kwargs (dict): Keyword argument for getting a specific row

		"""

		manager = Manager()
		manager.set_db()

		manager.select(self, **kwargs)