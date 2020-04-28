# coding: utf-8

import requests
from configuration import (URL,
						   HEADER,
						   CATEGORIES_TO_SCRAPE,
						   PRODUCTS_PER_CATEGORIES,
						   FIELDS,
						  )


class Catalogue:
	"""In charge of calling the API, getting back data

	and making them useable

	"""

	def __init__(self):
		"""Creating catalogue of products

		self._catalogue (dict): containing all products and categories, 
			cleaned, ready for registering in DB

		"""

		self._catalogue = _get_data() # Creating catalogue of products
		self._categories_for_each_product = list()


	def _get_data(self):
		"""In charge of calling the API and receiving raw data
		"""

		i = 0
		k = 1 #Number of the current page scrapped

		for category in CATEGORIES_TO_SCRAPE:

			# While we haven't enough products for this category
			while i < PRODUCTS_PER_CATEGORIES:


				response = requests.get(URL+category+f'/{k}.json?'+FIELDS)

				_processing_data(response.json())

				i = len(self._catalogue) # Setting i to the number of products scrapped
				k += 1 # Turning page

		# Building a set of each, unique, category
		self._set_of_categories = {category 
								   for categories_of_each_product in self._categories_for_each_product
								   for category in categories_of_each_product
								  }


	def _processing_data(self, raw_catalogue):
		"""In charge of cleaning data and then add them to self._catalogue

		Args:

			raw_catalogue (dict): raw json data, from the API
			category (str): current category scrapped

		"""

		for product in raw_catalogue:

			si le produit est complet:

				mettre en forme le produit

				ajouter le produit à self._catalogue #Tel quel, sous forme de dictionnaire
				ajouter la liste des catégories de ce produit à self.categories_for_each_product