# coding: utf-8

import requests
from configuration import (URL,
						   HEADER,
						   CATEGORIES_TO_SCRAPE,
						   PRODUCTS_PER_CATEGORIES,
						   FIELDS,
						   KEYWORDS,
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

		self._catalogue = list() # Empty catalogue of products
		self._set_of_categories = set()

	def get_data(self):
		"""In charge of calling the API and receiving raw data
		"""

		i = 0
		k = 1 #Number of the current page scrapped

		for category in CATEGORIES_TO_SCRAPE:

			# While we haven't enough products for this category
			while i < PRODUCTS_PER_CATEGORIES:


				response = requests.get(URL+category+f'/{k}.json?fields='+FIELDS,
										headers=HEADER
									   )

				_processing_data(response.json()['products'])

				i = len(self._catalogue) # Setting i to the number of products scrapped
				k += 1 # Turning page


	def _processing_data(self, raw_catalogue):
		"""In charge of cleaning data and then add them to self._catalogue

		Args:

			raw_catalogue (dict): raw json data, from the API
			category (str): current category scrapped

		"""

		for product in raw_catalogue:

			# We don't want empty fields in our catalogue
			if_all_fields_are_complete = all(True if product[j] != '' else False 
											 for j in product
											)

			# If the product is complete, all fields wanted and filled
			if len(product) == len(KEYWORDS) and if_all_fields_are_complete:

				# Append to self._catalogue every product (dict type) by switching 
				# for more convenient keywords
				switching_kw = {KEYWORDS[key]:value for key, value in product.items()}
				self._catalogue.append(switching_kw)

				for c in product['categories'].split(', '):

					# Building a set of (unique) categories to which product belong
					self._set_of_categories.add(c)