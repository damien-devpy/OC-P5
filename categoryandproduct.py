# coding: utf-8

class CategoryAndProduct:
    """Model class of the category_and_product table in database
    """

    TABLE_NAME = "category_and_product"

    def __init__(self, category_id, product_barre_code):
        """init method

        Attributes:

            category_id (int): category_id column in category_and_product table
            product_barre_code (int): product_barre_code column in category_and_product table

        """

        self._category_id = category_id
        self._product_barre_code = product_barre_code

	def save(self, manager_object, cursor_object):
		"""Saving data in DB, through a manager

		Args:

			manager_object (object manager): Gave access to insert method manager
			cursor_object (object cursor): Needed for managing DB

		"""

		manager_object.insert(cursor_object, CategoryAndProduct.TABLE_NAME, columns_name, (self._category_id,
																						   self._product_barre_code,
																						   )
							 )

	def read(self, manager_object, cursor_object, columns='*'):
		"""Reading data from DB, through a manager

		Args:

			manager_object (object manager): Gave access to select method manager
			cursor_object (object cursor): Needed for managing DB

		"""

		si columns == '*':
			colums <- toutes les colonnes

		manager_object.select(cursor_object, Product.TABLE_NAME, columns)

