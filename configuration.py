# coding: utf-8

# File name of the SQL script creating the DB
DATABASE = 'create_db.sql'

CREDENTIALS = 'user=***, password=***, host=localhost'

#Header for the API
HEADER = {'User-Agent': 'OFF App in progress - v0.1'}

#url of the API
URL = ' https://fr.openfoodfacts.org/categorie/'

#Fields to get
FIELDS = 'code,product_name_fr,nutriscore_grade,brands,ingredients_text_debug,quantity,categories'

# Products will be from this categories
CATEGORIES_TO_SCRAPE = {'chips-a-l-ancienne', # old-fashioned-crisps 
			  'houmous', # hummus
			  'compotes-pour-bebe',
			  'jambons-blancs', # white-hams
			  'brioches-pur-beurre', # pure-butter-brioche
			  'yaourts-sur-lit-de-fruits',
			  'saucissons-secs-pur-porc',
			  'gaufres', # waffles
			  'sauces-pesto', # pestos
			  'rillettes',
}


# Number of products per categories to scrap
PRODUCTS_PER_CATEGORIES = 100