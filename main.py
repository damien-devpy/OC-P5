# coding: utf-8

import mysql.connector
from catalogue import Catalogue
from category import Category
from product import Product
from substitution import Substitution
from categoryandproduct import CategoryAndProduct
from modelinspection import ModelInspection
from manager import Manager


def main():

	connexion <- mysql.connector.connect("informations utilisateur")

	curseur <- connexion.cursor()
	
	ouvrir le fichier 'create_sql.db':
		pour chaque ligne du fichier
			curseur <- executer la ligne

	obj_catalogue <- Catalogue()
	obj_model_inspection <- ModelInspection()
	manager <- Manager()

	#Insertion des catégories

	pour chaque catégorie dans obj_catalogue.categories_uniques:

		cat = Category(name=catégorie)
		cat.save(manager, curseur)

	fin pour

	#Insertion des produits

	pour chaque produit dans obj_catalogue.catalogue:

		p = Product(**produit)
		p.save(manager, curseur)

	fin pour

	#Alimentation de la table intermédiaire

	Category().read(manager, curseur)

	pour chaque élément dans le curseur:

		dictionnaire{id_cat, catégorie} <- enregistrer les éléments

	fin pour

	pour chaque produit dans obj_catalogue.catalogue:

		pour chaque élément dans le dictionnaire(id_cat, catégorie):

			si le produit appartient à la catégorie

			c_a_p = CategoryAndProduct(category_id=id_cat, product_barre_code=produit['barre_code'])
			c_a_p.save()

	fin pour

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

			categorie_utilisateur = CategoryAndProduct(category_id=choix_utilisateur)
			categorie_utilisateur.read(manager, curseur, columns='product_barre_code', )

		afficher "Liste des produits"

		choix_utilisateur <- entrée_utilisateur()

		récupérer le détail du produit choisis

		afficher "Détail du produit"

		afficher "1. Substitution"

		afficher "2. Retour au menu principal"

		choix_utilisateur <- entrée_utilisateur()

		si 1:

			rechercher une substitution

			afficher "produit de substitution"

			afficher "Enregistrement ?"

			afficher "Retour au menu principal"

			menu_principal()

		fin si

		si 2 :

			menu_principal()

		fin si

def anciennes_substitutions():

	rechercher toutes les substitutions

	pagination

	afficher "10 premières substitution"

	afficher "1. Voir détail substitution"

	afficher "2. Retour au menu principal"

	si 1:

		récupérer les détail des produits

		afficher "Produits"

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