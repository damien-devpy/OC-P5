# coding: utf-8

import mysql.connector

class Manager:
	"""In chage of managing data base
	"""

	def __init__(self):
		pass


	def select(self, cursor_object, table, *args):
		"""In charge of R part of CRUD (read)

		Arguments:

			cursor_object (cursor object): needed for managing DB
			table (str): name of the table to read
			*args (str): Variiable number of columns to read

		"""

		columns = tuple de chaque valeur dans *args

		cursor_object <- executer la requête : "SELECT columns FROM table"


	def insert(self, cursor_object, table, **kwargs):
		"""In charge of C part of CRUD (create)

		Arguments:

			cursor_object (cursor object): need for managing DB
			table (str): name of the table to read
			**kwargs (str): Variable number of kwargs, wich represent columns (keys) and data to insert (values) in table
			
		"""

		dictionnaire <- **kwargs unpacking

		cursor_object <- executer la requête : "INSERT INTO table (clés du dictionnaire) VALUES (valeurs du dictionnaire)"

	def substitution(self):
		"""Specifically in charge for looking a product substitution
		"""