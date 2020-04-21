# coding: utf-8

import mysql.connector
from configuration import DATABASE, USER

class InitDataBase:
	"""In charge of creating local data base and related user"""

	def __init__(self):
		pass


	def create_database(self, DATABASE):
		"""Creating a local database
		
		Args:

		DATABASE (str): SQL file name containing instruction for
			database creation

		"""
		pass
		

	def create_user(self, USER):
		"""Create an user related to our database
		
		Args:
		
		USER (dict): contains all information needed for user
			creation (user, user password, host)

		"""
		pass