# coding: utf-8

import mysql.connector

from manager import Manager

from catalogue import Catalogue

from category import Category
from product import Product
from categoryandproduct import CategoryAndProduct
from substitution import Substitution


def main():

	connexion <- mysql.connector.connect("informations utilisateur")

	curseur <- connexion.cursor()
	
	ouvrir le fichier 'create_sql.db':
		pour chaque ligne du fichier
			curseur <- executer la ligne

	obj_catalogue <- Catalogue()
	manager <- Manager()

	#Insertion des catégories

	categories = Category(manager_object=manager, cursor_object=curseur)

	pour chaque catégorie dans obj_catalogue.list_categories:
		c = Category(name=categorie)
		categories + c

	fin pour

	categories.save_all()

	id_and_categories = categories.read()

	#Insertion des produits

	all_products = Product(manager_object=manager, cursor_object=curseur)

	pour chaque produit dans obj_catalogue.catalogue:

		p = Product(**produit)
		all_products + p

	fin pour

	all_products.save_all()

	#Alimentation de la table intermédiaire

	all_cat_and_prod = CategoryAndProduct(manager_object=manager, cursor_object=curseur)

	pour chaque produit dans obj_catalogue.catalogue:

		pour chaque élément dans id_and_categories:

			si le produit appartient à la catégorie:

				cap = CategoryAndProduct(category_id=élément[id],
										 product_barre_code=produit['barre_code'],
										)
				all_cat_and_prod + cap

	fin pour

	all_cat_and_prod.save_all()

	menu_principal()


def menu_principal:

	afficher "Menu principal"
	afficher "1. Choissisez un aliment à substituer"
	afficher "2. Retrouvez vos précédentes substitutions"

	choix_utilisateur <- entrée_utilisateur()

	si 1:

		choisir_un_aliment()

	sinon:

		anciennes_substitutions()

def choisir_un_aliment:

		pagination de liste_categories

		afficher "10 premières catégories"

		choix_utilisateur <- entrée_utilisateur()

		récupérer les produits en base de la catégorie choisie

			categorie_utilisateur = CategoryAndProduct(manager_object=manager,
													   cursor_object=curseur,
													   category_id=choix_utilisateur,
													  )

			categorie_utilisateur.filter(f'category_id={choix_utilisateur}')
			liste_cb = categorie_utilisateur.read(columns='product_barre_code')

		liste_produits <- liste

		pour chaque code_barre dans liste_cb:
			p = Product(manager_object=manager,
						cursor_object=curseur,
					   )

			p.filter(f'barre_code={code_barre}')
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

		bc_to_substitute.filter(f'barre_code={historique[0]}')
		bc_to_substitute = bc_to_substitute.read()

		bc_substitute.filter(f'barre_code={historique[1]}')
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


if __name__ = "__main__":

	main()