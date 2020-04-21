# coding: utf-8

import mysql.connector

class ManagingDataBase:
	"""In charge of managing local database"""

	def __init__(self):

		pass


	def create(self, column, data):
		"""In charge of the C part of CRUD (CREATE)

		Args:

			column (tuple): In wich column(s) data will be insert
			data (list of tuple): list of tuples containing data to insert

		"""
		pass


	def read(self, table, *args):
		"""In charge of the R part of CRUD (READ)

		Args:

			table (str): in wich table we need to search
			*args: Variable number of colum(s) from where we want data

		Returns:

			result (list of tuples): list of tuples containing data
			
		"""
		pass