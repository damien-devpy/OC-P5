# coding: utf-8

import mysql.connector
from catalogue import Catalogue
from models import Product, Category, CategoryAndProduct, Substitution
from manager import Manager


def main():

	objet_manager <- Manager()
	objet_catalogue <- Catalogue()
	objet_product <- Product()
	objet_category <- Category()
	objet_cat_and_prod <- CategoryAndProduct()
	manager <- Manager()
	objet_substitution <- Substitution()
	objet_inspection <- ModelInspection()
	objet_mysql <- mysql.connector.connect("informations utilisateur")

	connexion à la base de donnée
	objet_curseur <- objet_mysql.curseur()
	
	ouvrir le fichier 'create_sql.db':
		pour chaque ligne du fichier
			objet_curseur <- executer la ligne

	#Insertion des catégories

	Pour chaque catégorie du catalogue:

		modèle_catégorie <- catégorie
		inspection du modèle_catégorie
		liste_de_catégories_db <- insertion de la donnée

	objet_manager <- insérer (objet_curseur, 
							  table, 
							  inspection du modèle_catégories(colonnes), 
							  liste_de_catégories_db
							 )

	#Insertion des produits dans la table produit
	#Et des données dans la table intermédiaire

	Pour chaque produit du catalogue:

		modèle_produit <- produit
		inspection du modèle_produit
		liste_de_produits_db <- insertion de la donnée

	objet_manager <- insérer (objet_curseur,
							  table,
							  inspection du modèle produit(colonnes),
							  liste_de_produits_db,
							 )

	#Insertion des données dans la table intermédiaire

	Récupérer la liste des catégories avec leurs id:

		liste_catégories_id <- object_manager <- selectionner (objet_curseur,
															   table,
															   inspection du modèle catégories(colonnes),
															  )

		# TODO TODO TODO TODO TODO 





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

def choisis_un_aliment:

		récupérer les catégories en base

		pagination

		afficher "10 premières catégories"

		choix_utilisateur <- entrée_utilisateur()

		récupérer les produits en base de la catégorie choisie

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