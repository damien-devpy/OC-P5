# coding: utf-8
"""Build up a catalogue by collecting data from an api."""

from re import compile as re_compile
from re import sub
from re import match
import requests
from configuration import (URL,
                           HEADER,
                           CATEGORIES_TO_SCRAPE,
                           FIELDS,
                           KEYWORDS,
                           PAGE_SIZE,
                           COUNTRY,
                           CATEGORIES_LC,
                           )
from model.product import Product
from model.category import Category


class Catalogue:
    """In charge of calling the API.

    Get back data and make them useable.

    """

    def __init__(self):
        """Create catalogue of products.

        Attributes:
            self._catalogue (list): containing all products and categories,
                cleaned, ready for registering in DB

        """
        self._catalogue = list()  # Empty catalogue of products

        # Regular expression for getting rid of categories looking like en:...
        # or fr:...
        self._re_header = re_compile(r'^en:+|^fr:+')

        # Regular expression for getting rid of spaces at beginning of a
        # string
        self._re_spaces = re_compile(r'^ *')

        # Regular expressions for getting rid of dashes and underscores
        self._re_dash = re_compile(r'[-]')
        self._re_underscores = re_compile(r'[_]')

    def get_data(self):
        """In charge of calling the API and receiving raw data."""
        for category in CATEGORIES_TO_SCRAPE:

            response = requests.get(f'{URL}'
                                    f'&tag_0={category}'
                                    f'&fields={FIELDS}'
                                    f'&page_size={PAGE_SIZE}',
                                    headers=HEADER
                                    )

            self._processing_data(response.json()['products'])

    def _processing_data(self, raw_catalogue):
        """In charge of cleaning data and then add them to self._catalogue.

        Args:
            raw_catalogue (dict): raw json data, from the API

        """
        for product in raw_catalogue:

            if self._product_ok(product):

                # Get rid of keys asked only for sorting products
                del product['countries']
                del product['categories_lc']

                # If product is complete, turn it as a Product object
                # and switching for more convenient keywords
                product_obj = Product(**{KEYWORDS[key]: (value
                                                         ).capitalize()
                                         for key, value in product.items()
                                         }
                                      )

                # Sort categories for each product
                product_obj = self._sort_categories(product['categories'],
                                                    product_obj,
                                                    )

                # If current product belong at least to one category
                if len(product_obj.belong_to) > 0:
                    # Set up store and brand correctly
                    product_obj = self._set_brand_store_right(product_obj)
                    # Getting rid of underscores in ingredients str
                    product_obj.ingredients = sub(self._re_underscores,
                                                  '',
                                                  product_obj.ingredients,
                                                  )
                    # Keeping it
                    self._catalogue.append(product_obj)

    def _product_ok(self, product):
        """Check if product is ok regarding criterias in configuration file."""
        # We don't want empty fields in our catalogue
        all_fields_are_complete = all(True if product[j] != '' else False
                                      for j in product
                                      )

        # Return True if the product is complete
        # (len(KEYWORD) + 1, asking countries but not registering it)
        # all fields wanted and filled
        # and the right country
        # and the right language
        return (len(product) == len(FIELDS.split(','))
                and all_fields_are_complete
                and product['countries'] == COUNTRY
                and product['categories_lc'] == CATEGORIES_LC
                )

    def _sort_categories(self, categories, product_obj):
        """Sort categories with regular expressions and criterias."""
        # For every word in the json key 'categories'
        for c in categories.split(','):
            # Getting rid of spaces
            c = sub(self._re_spaces, '', c)

            # Getting rid of dashes and underscores
            c = sub(self._re_dash, ' ', c)

            # If c look like en:/fr: or don't have more then
            # 2 caracters
            if match(self._re_header, c) or len(c) <= 2:
                # We don't register it
                continue

            else:
                c.capitalize()

                # Turn it to a Category object
                category_obj = Category(name=c)

                # Append it to the Product object which he belong to
                product_obj.belong_to.append(category_obj)

        return product_obj

    def _set_brand_store_right(self, product_obj):
        """Set right brand and store attributes.

        Only one brand and store per product.

        """
        product_obj.brand = product_obj.brand.split(',')[0]
        product_obj.store = product_obj.store.split(',')[0]

        return product_obj

    @property
    def catalogue(self):
        """Return list private attribute."""
        return self._catalogue
