# coding: utf-8

import requests
from configuration import (CATEGORIES_TO_SCRAPE,
						   PAGE,
						   FIELDS
						  )

class Catalogue:

	"""In charge of calling the API, getting back data

	and making them useable

	"""

	def __init__(self):
		"""Creating catalogue of products

		self._catalogue (...): Private attribute, containing all
		products and categories, cleaned, ready for registering in DB

		"""

		self._catalogue = _get_data()
		self._categories_for_each_product = []
		self._set_de_categories = {}


	def _get_data(self):
		"""In charge of calling the API and receiving raw data
		"""

		pour chaque catégorie à scrapper:

			pour chaque page de produits à scrapper:  #Tant que le nombre de produits / catégories n'a pas été atteint ?
				object_requests <- récupérer données ('url/catégorie/page.json?fields')

				_processing_data(object_requests.json())


	def _processing_data(self, raw_catalogue):
		"""In charge of cleaning data and then add them to self._catalogue

		Args:

			raw_catalogue (dict): raw json data, from the API
			category (str): current category scrapped

		"""

		pour chaque produits dans raw_catalogue:

			si le produit est complet:

				mettre en forme le produit

				ajouter le produit à self._catalogue #Tel quel, sous forme de dictionnaire
				ajouter la liste des catégories de ce produit à self.categories_for_each_product