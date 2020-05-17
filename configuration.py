# coding: utf-8

# File name of the SQL script creating the DB
DATABASE = 'orm/create_db.sql'
DATABASE_NAME = 'alimentation'

# CREDENTIALS = {'user':'root', 'password':'admin', 'host':'localhost'}

#Header for the API
HEADER = {'User-Agent': 'OFF App in progress - v0.1'}

#url of the API
URL = 'https://fr.openfoodfacts.org/cgi/search.pl?action=process&tagtype_0=categories&tag_contains_0=contains&json=true'

#Fields to get
FIELDS = 'code,product_name_fr,nutriscore_grade,brands,ingredients_text_debug,quantity,categories'

# Products will be from this categories
CATEGORIES_TO_SCRAPE = {'rillettes-de-canard',
			  	        'yaourts-sucres',
						'petits-beurres',
			  			'camemberts',
			  			'quatre-quarts'
			  		   }

PAGE_SIZE = 500

# Switching keywords of the API for the app's own kw
KEYWORDS = {'code': 'barre_code',
			'product_name_fr': 'name',
			'nutriscore_grade': 'nutrition_grade',
			'brands': 'brand',
			'ingredients_text_debug': 'ingredients',
			'quantity': 'quantity',
			'categories': 'categories',
	   	   }

# Items to be shown to the user in the view part
ITEMS_TO_SHOW = 10