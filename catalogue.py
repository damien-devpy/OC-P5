# coding: utf-8

import requests
from configuration import (CATEGORIES_TO_SCRAPE,
						   PAGE,
						   HEADER,
						   BARRE_CODE,
						   NAME,
						   SCORE,
						   BRAND,
						   QUANTITY,
						   CATEGORIES,
)

class Catalogue:
	"""In charge of managing OpenFoodFacts API, collecting data
	and create a catalogue of products

	"""

	def __init__(self):

		# list of tuples: useable data collected by _get_date() method
		_get_data(CATEGORIES_TO_SCRAPE, PAGE)


	catalogue = property(_get_catalogue)

	def _get_catalogue(self):
		# list of tuples: getter method
		return self._catalogue


	def _get_data(self, categories, page):
		"""Collecting json data from the API

		Args:

			categories (list): list of products categories we want
			products_num (int): number of products per categories we need

		"""

		self._catalogue <- dictionnaire
		
		pour chaque élément dans categories:
			self._catalogue['élement'] <- ensemble()

			pour chaque page à consulter:
				réponse = requests.get(f"""https://fr-en.openfoodfacts.org/category/{élément}/{page}.json?
										   fields=code,product_name_fr,nutriscore_grade,brands,ingredients_text_debug,quantity""", 
										   header=HEADER)

				_processing_data(réponse, élément)


			fin pour
		fin pour

	def _processing_data(self, raw_catalogue, élément):
		"""Extracting data needed from a raw json catalogue

		For each product complete, append to self._catalogue 
		a tuple containing clean data

		Args: 

			raw_catalogue (dict): raw json data from the API
			élément (str): current categories we are running

		"""

		pour chaque produit dans raw_catalogue:
			si le produit est complet:

				ajouter à self._catalogue['élément'] le tuple (produit[BARRE_CODE],
										   					   produit[NAME],
										   					   produit[SCORE],
										   					   produit[BRAND],
										   					   produit[INGREDIENTS],
										   				       produit[QUANTITY],
										   					   )
			fin si
		fin pour


