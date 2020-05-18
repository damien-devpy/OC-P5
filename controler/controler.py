# coding: utf-8

import configuration

from model.model import Model
from model.product import Product
from model.category import Category
from model.substitution import Substitution
from orm.manager import Manager
from model.catalogue import Catalogue
from view.view import View

from copy import copy

import pdb


class Controler():
	"""Controler part of the app, manage inputs from user and
		iteraction between objects for instance

	"""

	def __init__(self):

		self._catalogue = Catalogue()
		self._manager = Manager()
		self._vue = View()


	def controler(self):

		# If database doesn't exist
		if not self._manager.is_there_db():

			# Getting data from the OpenFoodFacts API
			self._catalogue.get_data()

			# Creating database
			self._manager.create_db()

			# Inserting data in database
			self._manager.insert_all(self._catalogue.catalogue)


		self._manager.set_db()

		input_ok = False

		# While an input as not occured, or an incorrect one
		while not input_ok:

			# Display main menu and ask user for a choice
			self._vue.main_menu()

			input_user = input()

			try:
				input_user = int(input_user)
				input_ok = True

			except:
				self._vue.make_correct_input()


		if input_user == 1:

			# User can choose among many categories
			category_choosed = self._categories_menu()

			# User choose a product belonging to the category choosed
			product_choosed = self._products_menu(category_choosed)

			# Displaying all details about the product
			self._vue.details_menu(product_choosed)

			print("Do you want to find a substitute for this product ?", end =' ')
			print("(y for yes)")
			print()

			if input().lower() == 'y':

				self._find_substitute(product_choosed, category_choosed)

			else:
				# Get back to the main menu
				self.controler()


		elif input_user == 2:
			
			sub_choosed = self._substitution_menu()

		else:
			exit()


	def _categories_menu(self):

		self._vue.page = 1

		# Getting list of categories from the database
		categories = self._manager.select(Category)

		# Displaying categories in a sub menu
		self._vue.sub_menu(categories)

		category_choosed = self._navigation(categories)

		return category_choosed


	def _products_menu(self, category_choosed):

		self._vue.page = 1

		# Getting list of products of the chosen category
		products = self._manager.select_through_join(Product,
											   		 Category,
											   		 name=category_choosed.name,
											  		 )
		# Displaying products in a sub menu
		self._vue.sub_menu(products)

		product_choosed = self._navigation(products)

		return product_choosed


	def _substitution_menu(self):

		self._vue.page = 1

		# Getting list of substitutions from the database
		substitutions = self._manager.select(Substitution)

		# Displaying categories in a sub menu
		self._vue.sub_menu_substitution(substitutions)

		sub_choosed = self._navigation(substitutions)

		return sub_choosed


	def _navigation(self, items):

		input_ok = False

		# While an input as not occured, or an incorrect one
		while not input_ok:

			input_user = input()

			# If user want to go back to the main menu
			if input_user == "back":

				self.controler()	

			# If user want to display another page
			elif any((input_user == "<", input_user == ">")):

				if input_user == "<":
					# Display previous page
					self._vue.page -= 1
					self._vue.sub_menu(items)

				else:
					# Display next page
					self._vue.page += 1
					self._vue.sub_menu(items)

			else:

				try:
					input_user = int(input_user)
					input_ok = True

				except:
					self._vue.make_correct_input()

				else:
					item_choosed = self._vue.get_object_with_paging(items,
												              		input_user,
											   			     	   )
		return item_choosed


	def _find_substitute(self, product_choosed, category_choosed):

		# Keeping id of the product to substitute
		id_substitute = product_choosed.id
		
		# Looking for a substitute of the chosen product
		# get_substitute change product in place
		product_choosed.get_substitute(category_choosed)

		self._vue.details_menu(product_choosed)

		# If a substitute has been found
		if id_substitute != product_choosed:

			print("Do you want to save your substitution ?")
			print("Use 'y' for yes, any other input to get back to the main menu")
			print()

			if input().lower() == 'y':

				substitution = Substitution(id_to_substitute=id_substitute,
											id_substitute=product_choosed.id,
										   )

				substitution.save()

				self.controler()

			else:

				# Get back to the main menu
				self.controler()

		else:

			print("You already have the best produt !")
			print()



