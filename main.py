# coding: utf-8

import mysql.connector

from manager import Manager

from catalogue import Catalogue

from category import Category
from product import Product
from categoryandproduct import CategoryAndProduct
from substitution import Substitution

from configuration import (CREDENTIALS,
						   KEYWORDS_API_APP,
						  )


def main():

	# Connection to mysql with user credentials
	cnx = mysql.connector.connect(CREDENTIALS)

	# Creating a cursor wich interact with DB
	sql_cursor = cnx.cursor()

	# Creating the DB from a sql file
	with open('create_db.sql', 'r', encodig='utf-8') as sql_file:
		for line in sql_file:
			sql_cursor.execute(line)

	# Manager object in charge of SQL queries
	manager_object = Manager()

	# Creating an empty catalogue
	catalogue_object = Catalogue()

	# Filling it with products from the API
	catalogue_object.get_data()


	# Filling DB table category with products categories

	categories = Category(manager=manager_object, cursor=sql_cursor)

	for each_category in catalogue_object.set_of_categories:
		categories + Category(name=each_category)

	categories.save_all()

	# After insertion, getting each categories with his id
	id_and_categories = categories.read()


	# Filling DB table product with products
	# Filling DB intermediary table category_and_product

	all_products = Product(manager=manager_object, cursort=sql_cursor)

	all_cat_and_prod = CategoryAndProduct(manager=manager_object,
										  cursor=sql_cursor,
										 )

	for each_product in catalogue_object.catalogue:
		all_products + Product(each_product)

		# For each couple (id, category) in table category
		for element in id_and_categories:
			# If the current product belong to the current category
			if element[1] in each_product[6]:

				# Saving couple (category_id, product_barre_code)
				# in intermediary table category_and_product
				tmp_cap = CategoryAndProduct(category_id=element[0],
											 product_barre_code=each_product[0],
											)
				all_cat_and_prod + tmp_cat


	all_products.save_all()
	all_cat_and_prod.save_all()

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

		page = 1

		showing_categories = 10

		paging(page, showing_categories, id_and_categories)

		afficher "10 premières catégories"

		choix_utilisateur <- entrée_utilisateur()

		récupérer les produits en base de la catégorie choisie

			categorie_utilisateur = CategoryAndProduct(manager_object=manager,
													   cursor_object=curseur,
													   category_id=choix_utilisateur,
													  )

			categorie_utilisateur.filter_by(f'category_id={choix_utilisateur}')
			liste_cb = categorie_utilisateur.read(columns='product_barre_code')

		liste_produits <- liste

		pour chaque code_barre dans liste_cb:
			p = Product(manager_object=manager,
						cursor_object=curseur,
					   )

			p.filter_by(f'barre_code={code_barre}')
			p.read()

			liste_produits <- p

		pour chaque produits dans liste_produits:

			afficher le produit

		choix_utilisateur <- entrée_utilisateur()

		récupérer les informations dans liste_produits[produit_choisi]

		afficher "Détail du produit"

		afficher "1. Substitution"

		afficher "2. Retour au menu principal"

		choix_utilisateur <- entrée_utilisateur()

		si 1:

			product_substitute = liste_produits[produit_choisi]
			product_substitute.get_substitute(choix_utilisateur_catégorie)

			afficher "product_substitute"

			afficher "Enregistrement ?"

			record_substitution = Substitution(manager_object=manager,
											   cursor_object=curseur,
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

	all_substititions = Substitution(manager_object=manager, cursor_object=curseur)

	historique = all_substititions.read()

	pagination

	afficher "10 premières substitution"

	afficher "1. Voir détail substitution"

	afficher "2. Retour au menu principal"

	si 1:

		bc_to_substitute = Product(manager_object=manager, cursor_object=curseur)
		bc_substitute = Product(manager_object=manager, cursor_object=curseur)

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


def entrée_utilisateur():

	Afficher "Question"

	return input utilisateur

def paging(page, nb_items_to_show, list_of_items):

	debut = (page-1) + nb_items_to_show
	fin = page*nb_items_to_show

	si la page <= (len(list_of_items)%nb_items_to_show):

		return list_of_items[debut:fin]

	sinon si la page > (len(list_of_items)%nb_items_to_show) et len(list_of_items)%10 != 0

		return list_of_items[::-(len(list_of_items)%nb_items_to_show)]

	sinon:

		return list_of_items[::-nb_items_to_show]


if __name__ = "__main__":

	main()