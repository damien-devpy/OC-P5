# coding: utf-8

# File name of the SQL script creating the DB
DATABASE = 'create_db.sql'

USER = {'user':'***', 'password':'***', 'host':'localhost'}

# Products will be from this categories
CATEGORIES_TO_SCRAPE = {'pizzas',
			  'sweet-spreads',
			  'dairies',
			  'meals',
			  'cheeses',
			  'salted-spreads',
			  'fruit-juices',
			  'sausages',
			  'frozen-ready-made-meals',
			  'rillettes'
}

# Number of page per categories we need to scrape
PAGE = 1

#Header for the API
HEADER = {'User-Agent': 'OFF App in progress - v0.1'}

# Useful entries in json data return by the API
BARRE_CODE = 'code'
NAME = 'product_name_fr'
SCORE = 'nutriscore_grade'
BRAND = 'brands'
INGREDIENTS = 'ingredients_text_debug'
QUANTITY = 'quantity'
CATEGORIES = 'categories_tags'