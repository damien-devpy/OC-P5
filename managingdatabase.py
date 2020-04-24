# coding: utf-8

import mysql.connector
from configuration import CATEGORIES_TO_SCRAPE

class ManagingDataBase:
	"""In charge of managing local database"""

	def __init__(self):

		pass


	def insert(self, cursor_object, table, column, data):
		"""In charge of the C part of CRUD (CREATE)

		Args:
			cursor_object (cursor_object): Needed mysql object for interact with DB
			table (str): In wich table data will be insert
			column (tuple): In wich column(s) data will be insert
			data (list of tuple): List of tuples containing data to insert

		"""

			values = tuple(%s pour chaque élément dans column)

			executer la requête : (('INSERT INTO' + str(table) + str(column) + 'VALUES' + str(values)), data)

	def insert_data(self, cursor_object, values_product):
		"""In charge of specifically insert category and products after getting through the API

		Args:
			cursor_object (cursor_object): Needed mysql object for interact with DB
			values_product (dict): Contains as much set there is CATEGORIES_TO_SCRAPE, each one contains
			a tuple for each product of this categories

		"""

			pour chaque élément dans CATEGORIES_TO_SCRAPE:
				executer la requête : (("INSERT INTO category (name) VALUES (%s)"), élément)

				pour chaque produit dans values_product[élément]:
					executer la requête : (("INSERT INTO product VALUES (%s, %s, %s, %s, %s, %s)"), (produit[BARRE_CODE],
										   					   										 produit[NAME],
										   					   										 produit[SCORE],
										   					   										 produit[BRAND],
										   					   										 produit[INGREDIENTS],
										   				       										 produit[QUANTITY],
										   					   										 )
										   )

	def select(self, cursor_object, table, column):
		"""In charge of the R part of CRUD (READ)

		Args:
			cursor_object (cursor_object): Needed mysql object for interact with DB
			table (str): In wich table we need to read
			column (tuple): Column(s) to read
			
		"""
			executer la requête : 'SELECT' + str(column) + 'FROM' + str(table)

	def substitute(self, cursor_object, barre_code):
		"""In charge of finding substitute for a product

		Args:
			cursor_object (cursor_object): Needed mysql object for interact with DB
			barre_code (int): barre_code number for the product to substitute

		Returns

			barre_code (int): barre_code number for the produc substitute