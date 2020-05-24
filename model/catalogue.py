# coding: utf-8

import requests
from configuration import (URL,
                           HEADER,
                           CATEGORIES_TO_SCRAPE,
                           FIELDS,
                           KEYWORDS,
                           PAGE_SIZE,
                           )

from model.product import Product
from model.category import Category
from re import compile as re_compile
from re import sub
from re import match


class Catalogue:
    """In charge of calling the API.

    Get back data and make them useable.

    """

    def __init__(self):
        """Create catalogue of products.

        Args:
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

        # Regular expression for getting rid of dashes
        self._re_dash = re_compile(r'-')

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

            # We don't want empty fields in our catalogue
            all_fields_are_complete = all(True if product[j] != '' else False
                                          for j in product
                                          )

            # If the product is complete, all fields wanted and filled
            if len(product) == len(KEYWORDS) and all_fields_are_complete:

                # Append to self._catalogue every product as a Product object
                # and switching for more convenient keywords
                product_obj = Product(**{KEYWORDS[key]: (value
                                                         ).capitalize()
                                         for key, value in product.items()
                                         }
                                      )

                # For every word in the json key 'categories'
                for c in product['categories'].split(','):

                    # Getting rid of spaces
                    c = sub(self._re_spaces, '', c)

                    # Getting rid of dashes, putting spaces instead
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

                # If current product belong at least to one category
                if len(product_obj.belong_to) > 0:

                    # Keeping it
                    self._catalogue.append(product_obj)

    @property
    def catalogue(self):
        return self._catalogue
