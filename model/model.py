# coding: utf-8

from orm.manager import Manager
import pdb


class Model:
	"""Model class representing table database
	"""

	def __init__(self):

		# Set this attribute True if there is a risk for registering twice the same
		# information in database but you don't want to ignore it
		self.duplicate_key = False

		# Set this attribute True for database to ignore a row if an information
		# match a unique key already registered
		self.ignore = False

		# Filling it for representing a many to many relation
		self.belong_to = list()

		# Filling it with name of the table which there is a many to many
		# relation
		self.liaison_table = None
		

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
		"""Making model objects iterable

		Return:

			iterator: An iterator that contain all attributes representing
				columns in database

		"""

		# Return an iterator containing attributes of self that do
		# represent a column in database
		# (For instance, duplicate_key and belong_to attributes DO NOT 
		# represent columns of a table)
		return (value 
				for i, value 
				in enumerate(self.__dict__.values())
			    if i < self.COLUMNS
			   )