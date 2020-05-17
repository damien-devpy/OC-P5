# coding: utf-8

import configuration

from model.model import Model
from model.product import Product
from model.category import Category
from model.substitution import Substitution
from orm.manager import Manager
from model.catalogue import Catalogue
from view.view import View

# class Controler:
# 	"""In charge of the control part of the app, inputs from user and
# 		iteraction between objects for instance

# 	"""

# 	def __init__(self):
# 		pass

# 	

def controler():
	"""Controler part of the app, manage inputs from user and
		iteraction between objects for instance

	"""

	catalogue = Catalogue()
	manager = Manager()
	vue = View()

	# Getting data from the OpenFoodFacts API
	catalogue.get_data()

	# Creating database
	manager.create_db()

	# Inserting data in database
	manager.insert_all(catalogue.catalogue)

	input_ok = False

	# While an input as not occured, or an incorret one
	while not input_ok:

		# Display main menu and ask user for a choice
		vue.main_menu()

		input_user = input()

		try:
			input_user = int(input_user)
			input_ok = True

		except:
			vue.make_correct_input()


	if input_user == 1:

		current_page = 1

		# Getting list of categories from the database
		categories = manager.select(Category)

		# Displaying categories in a sub menu
		vue.sub_menu(categories, current_page)


		input_ok = False

		# While an input as not occured, or an incorret one
		while not input_ok:

			input_user = input()

			# If user want to display another page
			if any((input_user == "<", input_user == ">")):

				if input_user == "<":

					# Display previous page
					vue.sub_menu(categories, current_page-1)

				else:

					# Display next page
					vue.sub_menu(categories, current_page+1)

			else:






