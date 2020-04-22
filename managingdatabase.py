# coding: utf-8

import mysql.connector

class ManagingDataBase:
	"""In charge of managing local database"""

	def __init__(self):

		pass


	def create(self, table, column, data):
		"""In charge of the C part of CRUD (CREATE)

		Args:
			table (str) : In wich table data will be insert
			column (tuple): In wich column(s) data will be insert
			data (list of tuple): List of tuples containing data to insert

		"""
		pass


	def read(self, table, column, **kwargs):
		"""In charge of the R part of CRUD (READ)

		Args:

			table (str): In wich table we need to read
			column (tuple) : Column(s) to read
			**kwargs : Variable number of kwargs to read some specific rows

		Returns:

			result (cursor object): iterable containing data
			
		"""
		pass