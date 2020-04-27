# coding: utf-8

import mysql.connector

class Manager:
	"""In chage of managing data base
	"""

	def __init__(self):
		pass


	def select(self, cursor_object, table, columns):
		"""In charge of R part of CRUD (read)

		Args:

			cursor_object (cursor object): needed for managing DB
			table (str): ame of the table to read
			columns (tuple): columns to read

		"""

		cursor_object <- executer la requête : "SELECT columns FROM table"


	def insert(self, cursor_object, table, columns, values):
		"""In charge of C part of CRUD (create)

		Args:

			cursor_object (cursor object): need for managing DB
			table (str): name of the table to read
			columns (tuple of str): columns in wich we want to insert data
			values (list of tuple): data to insert
			
		"""

		Démarrer une transaction

			Pour chaque élément dans values:

				cursor_object <- executer la requête : "INSERT INTO table (columns) VALUES (élément)"

		Commit

	def substitution(self):
		"""Specifically in charge for looking a product substitution
		"""

