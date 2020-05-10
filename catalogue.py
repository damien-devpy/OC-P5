# coding: utf-8

import requests
from configuration import (URL,
						   HEADER,
						   CATEGORIES_TO_SCRAPE,
						   FIELDS,
						   KEYWORDS,
						   PAGE_SIZE,
						  )

from product import Product
from category import Category
from model import Model
import time
import pdb


class Catalogue:
	"""In charge of calling the API, getting back data

	and making them useable

	"""

	def __init__(self):
		"""Creating catalogue of products

		Args:

			self._catalogue (list): containing all products and categories, 
				cleaned, ready for registering in DB

		"""

		self._catalogue = list() # Empty catalogue of products



	def get_data(self):
		"""In charge of calling the API and receiving raw data
		
		"""

		for category in CATEGORIES_TO_SCRAPE:

				response = requests.get(f'{URL}&tag_0={category}&fields={FIELDS}&page_size={PAGE_SIZE}',
										headers=HEADER
									   )

				self._processing_data(response.json()['products'])

				print(len(self._catalogue))



	def _processing_data(self, raw_catalogue):
		"""In charge of cleaning data and then add them to self._catalogue

		Args:

			raw_catalogue (dict): raw json data, from the API

		"""

		for product in raw_catalogue:

			# We don't want empty fields in our catalogue
			all_fields_are_complete = all(True if product[j] != '' else False 
											 for j in product
											)

			# If the product is complete, all fields wanted and filled
			if len(product) == len(KEYWORDS) and all_fields_are_complete:

				# Append to self._catalogue every product as a Product object
				# and switching for more convenient keywords
				product_obj = Product(**{KEYWORDS[key]:value for key, value in product.items()})

				# For every word in the json key 'categories'
				for c in product['categories'].split(', '):

					# Turn it to a Category object
					category_obj = Category(name=c)

					# Append it to the Product object which he belong to
					product_obj.belong_to.append(category_obj)

				self._catalogue.append(product_obj)



	def getter_catalogue(self):
		return self._catalogue


	catalogue = property(getter_catalogue)
