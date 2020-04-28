# coding: utf-8

import mysql.connector

class Manager:
	"""In chage of managing data base
	"""

	def __init__(self):
		pass


	def select(self, cursor_object, table, columns, where_clause=False):
		"""In charge of R part of CRUD (read)

		Args:

			cursor_object (cursor object): needed for managing DB
			table (str): ame of the table to read
			columns (tuple): columns to read

		"""
		si where_clause est vrai:

			cursor_object <- executer la requête : "SELECT columns FROM table WHERE " + where_clause

		else:
			cursor_object <- executer la requête : "SELECT columns FROM table"


	def insert(self, cursor_object, table, columns, values):
		"""In charge of C part of CRUD (create)

		Args:

			cursor_object (cursor object): need for managing DB
			table (str): name of the table to read
			columns (tuple of str): columns in wich we want to insert data
			values (tuple): data to insert
			
		"""

				cursor_object <- executer la requête : "INSERT INTO table (columns) VALUES (élément)"

	def substitution(self):
		"""Specifically in charge for looking a product substitution
		"""

