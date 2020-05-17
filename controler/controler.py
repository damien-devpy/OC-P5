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
			self._manager.insert_all(catalogue.catalogue)

		else:

			self._manager.set_db()

			input_ok = False

			# While an input as not occured, or an incorret one
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

				category_choosed = self._categories_menu()

				product_choosed = self._products_menu(category_choosed)

				self._vue.details_menu(product_choosed)

				self._vue.make_substitution()

				if input().lower() == 'y':

					product_to_substitute = copy(product_choosed)
					product_substitute = product_choosed.get_substitute(category_choosed)

					self._vue.details_menu(product_substitute)

					self._vue.record_substitution()

					if input().lower() == 'y':

						substitution = Substitution(id_to_substitute=product_to_substitute.id,
													id_substitute=product_substitute.id,
												   )

						substitution.save()
						self.controler()

					else:

						# Get back to the main menu
						self.controler()

				else:

					# Get back to the main menu
					self.controler()


	def _categories_menu(self):

		current_page = 1

		# Getting list of categories from the database
		categories = self._manager.select(Category)

		# Displaying categories in a sub menu
		self._vue.sub_menu(categories, current_page)

		input_ok = False

		# While an input as not occured, or an incorrect one
		while not input_ok:

			input_user = input()

			# If user want to display another page
			if any((input_user == "<", input_user == ">")):

				if input_user == "<":
					# Display previous page
					current_page -= 1
					self._vue.sub_menu(categories, current_page)

				else:
					# Display next page
					current_page += 1
					self._vue.sub_menu(categories, current_page)

			else:

				try:
					input_user = int(input_user)
					input_ok = True

				except:
					self._vue.make_correct_input()

				else:
					category_choosed = self._vue.get_object_with_paging(categories,
														  				current_page,
												         	    		input_user,
											   			 	   	   	   )

		return category_choosed



	def _products_menu(self, category_choosed):

		current_page = 1

		# Getting list of products of the chosen category
		products = self._manager.select_through_join(Product,
											   Category,
											   name=category_choosed.name,
											  )
		# Displaying products in a sub menu
		self._vue.sub_menu(products, current_page)

		input_ok = False

		# While an input as not occured, or an incorrect one
		while not input_ok:

			input_user = input()

			# If user want to display another page
			if any((input_user == "<", input_user == ">")):

				if input_user == "<":
					# Display previous page
					current_page -= 1
					self._vue.sub_menu(products, current_page)

				else:
					# Display next page
					current_page += 1
					self._vue.sub_menu(products, current_page)

			else:

				try:
					input_user = int(input_user)
					input_ok = True

				except:
					self._vue.make_correct_input()

			product_choosed = self._vue.get_object_with_paging(products,
														  	   current_page,
												               input_user,
											   			      )

			return product_choosed


