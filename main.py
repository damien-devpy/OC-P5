# coding: utf-8

from catalogue import Catalogue
from mysql import connector

def main():
	"""Main function of the application
	This where menu take place and user can :
		- See product details
		- Make a substitution and save it
	"""

	Création du catalogue produits <- Création d''un objet type Catalogue()

	tant que l''utilisateur souhaite continuer:

		choix_utilisateur <- fonction menu_principal()

		si 1:

			choix_utilisateur <- fonction menu_choix_utilisateur("afficher les catégories")

			choix_utilisateur <- fonction menu_choix_utilisateur("afficher les produits d'une catégorie", choix_utilisateur)

			afficher en détail le produit

			trouver_une_substitution(choix_utilisateur)

			afficher le produit de substitution

			proposer d''enregistrer la substitution

			demande si l''utilisateur souhaite continuer

		fin si

		sinon:

			rechercher les substitutions

			afficher les substitutions

			demander si l''utilsateur souhaite continuer


definir fonction menu_principal():

	afficher le menu principal :

		1 - Choisir un produit à substituer
		2 - Consulter l''historique des substitutions

	retourner le choix utilisateur


definir fonction menu_choix_utilisateur(requete à utiliser, catégorie=False):
	
	si catégorie est vrai:

		liste <- produits retournés par la requête à utiliser

	sinon 

		liste <- catégorie retournées par la requête à utiliser

	pour chaque élément dans la liste
		afficher un numéro et l''élément
	fin pour

	retourner choix utilisateur


if __name__ == "__main__":
	main()