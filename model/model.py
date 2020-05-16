# coding: utf-8

from orm.manager import Manager
import pdb


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
		"""
		
		manager = Manager()
		manager.set_db()

		manager.select(self, **kwargs)



	def __iter__(self):

		return iter(self.__dict__.values())	