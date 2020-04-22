# coding: utf-8

import requests
from configuration import CATEGORIES, PRODUCTS_NUM

class Catalogue:
	"""In charge of managing OpenFoodFacts API, collecting data
	and create a catalogue of products

	"""

	def __init__(self):

		# list of tuples: useable data collected by _get_date() method
		self._catalogue = _get_data(CATEGORIES, PRODUCTS_NUM)


	catalogue = property(_get_catalogue)

	def _get_catalogue(self):
		# list of tuples: getter method
		return self._catalogue


	def _get_data(self, categories, products_num):
		"""Collecting json data from the API

		Args:

			categories (list): list of products categories we want
			products_num (int): number of products per categories we need

		Returns:

			catalogue (list of tuples): cleaned data (through _processing_data())

		"""
		pass


	def _processing_data(self, raw_catalogue):
		"""Extracting data needed from a raw json catalogue

		Args: 

			raw_catalogue (dict): raw json data from the API

		Returns:

			processed_data (list of tuples): cleaned data

		"""
		pass


