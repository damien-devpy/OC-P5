# coding: utf-8

# File name of the SQL script creating the DB
DATABASE = 'create_db.sql'

USER = {'user':'***', 'password':'***', 'host':'localhost'}

#Header for the API
HEADER = {'User-Agent': 'OFF App in progress - v0.1'}

#url of the API
URL = ''

#Fields to get
FIELDS = 'code,product_name_fr,nutriscore_grade,brands,ingredients_text_debug,quantity,categories_tags'

# Products will be from this categories
CATEGORIES_TO_SCRAPE = {'old-fashioned-crisps', #chips-a-l-ancienne 
			  'hummus', # houmous
			  'fr:compotes-pour-bebe',
			  'white-hams', #jambons-blancs
			  'pure-butter-brioche', #brioches-pur-beurre
			  'fr:yaourts-sur-lit-de-fruits',
			  'fr:saucissons-secs-pur-porc',
			  'waffles', # gaufres
			  'pestos', #sauces-pesto
			  'rillettes',
}


# Number of products per categories to scrap
PRODUCTS_PER_CATEGORIES = 100

# Useful entries in json data return by the API
BARRE_CODE = 'code'
NAME = 'product_name_fr'
SCORE = 'nutriscore_grade'
BRAND = 'brands'
INGREDIENTS = 'ingredients_text_debug'
QUANTITY = 'quantity'
CATEGORIES = 'categories_tags'