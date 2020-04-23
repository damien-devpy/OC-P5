# coding: utf-8

import mysql.connector
from configuration import DATABASE, USER

class InitDataBase:
	"""In charge of creating local data base and related user"""

	def __init__(self):
		pass


	def create_database(self, DATABASE, cursor_object):
		"""Creating a local database
		
		Args:

		DATABASE (str): SQL file name containing instruction for
			database creation

		cursor_object (cursor object): Object from mysql.connector needed for DB interaction

		"""
		ouverture du fichier DATABASE

		lecture de chaque ligne du fichier

		executer chaque ligne du fichier