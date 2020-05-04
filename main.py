# coding: utf-8

from mysql import connector

from manager import Manager

from catalogue import Catalogue

from category import Category
from product import Product
from categoryandproduct import CategoryAndProduct
from substitution import Substitution

from configuration import (CREDENTIALS,
						   ITEMS_TO_SHOW,
						  )


def main():

	# Creating an empty catalogue
	catalogue_object = Catalogue()

	# Filling it with products from the API
	catalogue_object.get_data()

	# Filling the DB with data previously received
	catalogue_object.filling_db()

	main_menu()


def main_menu:

	print("Menu principal:")
	print("1. Choissisez un aliment à substituer")
	print("2. Retrouvez vos précédentes substitutions")

	user_input = input()

	if user_input == 1:

		choose_a_product()

	else:

		substitutions_saved()

def choose_a_product:

	# Get all categories from the DB
	id_and_categories = Category()

	expgen = ((element.id_cat, element.name) for element in id_and_categories)

	# Setting page to show to 1
	page = 1

	# Getting page 1
	to_show = paging(page,
					 [el[1] for el in expgen]
					)

	# Showing page
	for i, j in enumerate(to_show):
		print(f"{i+1}. {j}")

	input_ok = False

	# User choose a category
	while not input_ok:

		try:
			user_choice = (int(input())) - 1
			input_ok = 1
			user_choice = to_show[user_choice]
		except:
			print("Please use a valid id")

	# Getting the id of the category choosed by the user
	category_id = Category(manager, sql_cursor)
	category_id.filter_by(f'name={user_choice}')
	category_id = category_id.read()[0].id_cat

	# Getting barre code of products that match previous category id
	list_of_products = CategoryAndProduct(manager, sql_cursor)
	list_of_products.filter_by(f'category_id={category_id}')
	list_of_products = list_of_products.read()

	# Getting products information from their barre code
	products_infos = Product(manager, sql_cursor)

	for bc in list_of_products:
		products_infos.filter_by(f'barre_code={bc}')
		products_infos + products_infos.read()[0]

	page = 1

	# Getting names of all products
	expgen = (element.name for element in products_infos.buffer)

	to_show = paging(page,
					 [i for i in expgen],
					)

	# Showing page
	for i, j in enumerate(to_show):
		print(f"{i+1}. {j}")

	input_ok = False

	# User choose a product
	while not input_ok:

		try:
			user_choice = (int(input())) - 1
			input_ok = 1
			user_choice = to_show[user_choice]
		except:
			print("Please use a valid id")

	choosen_product = [element for element in products_infos.buffer if element.name = user_choice]

	for attr in choosen_product:
		print(attr)


	print("1. Substitution")
	print("2. Menu principal")

		choix_utilisateur <- entrée_utilisateur()

		si 1:

			product_substitute = liste_produits[produit_choisi]
			product_substitute.get_substitute(choix_utilisateur_catégorie)

			afficher "product_substitute"

			afficher "Enregistrement ?"

			record_substitution = Substitution(manager,
											   sql_cursor,
											   barre_code_to_substitute=barre_code_choix_utilisateur,
											   barre_code_substitute=product_subsitute['barre_code'],
											  )

			afficher "Substitution enregistrée"

			afficher "Retour au menu principal"

			menu_principal()

		fin si

		si 2 :

			menu_principal()

		fin si

def anciennes_substitutions():

	all_substititions = Substitution(manager, sql_cursor)

	historique = all_substititions.read()

	pagination

	afficher "10 premières substitution"

	afficher "1. Voir détail substitution"

	afficher "2. Retour au menu principal"

	si 1:

		bc_to_substitute = Product(manager, sql_cursor)
		bc_substitute = Product(manager, sql_cursor)

		bc_to_substitute.filter_by(f'barre_code={historique[0]}')
		bc_to_substitute = bc_to_substitute.read()

		bc_substitute.filter_by(f'barre_code={historique[1]}')
		bc_substitute = bc_substitute.read()

		afficher "bc_to_substitute/bc_substitute"

		afficher "1. Retour aux substitutions"

		afficher "2. Retour au menu principal"

		si 1:

			anciennes_substitutions()

		fin si

		si 2:

			menu_principal()

	fin si

	si 2:

		menu_principal()

	fin si


def paging(page, list_of_items):

	# How much (ITEMS_TO_SHOW) is in list_of_items
	how_much_to_show = len(list_of_items) // ITEMS_TO_SHOW

	# Number of pages
	total_pages = how_much_to_show + 1 if ((list_of_items) % ITEMS_TO_SHOW) else how_much_to_show

	# If page asked doesn't exist, return last existing one
	if page > total_pages:

		last_page = ((total_pages - 1) * ITEMS_TO_SHOW) + 1

		return list_of_items[last_page:]

	# Else, return items that match page asked
	else:

		prev_page = (page - 1) if (page > 1) else 1
		start = 1 + (ITEMS_TO_SHOW * prev_page)
		end = (page * ITEMS_TO_SHOW) if ((page * ITEMS_TO_SHOW) < len(list_of_items)) else len(list_of_items)

		return list_of_items[start:end]


if __name__ = "__main__":

	main()