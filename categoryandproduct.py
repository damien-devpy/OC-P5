# coding: utf-8

class CategoryAndProduct:
    """Model class of the category_and_product table in database
    """

    def __init__(self):
        """init method

        Attributes:

            category_id (int): category_id column in category_and_product table
            product_barre_code (int): product_barre_code column in category_and_product table
			table_name (str): Table name this model represent

        """
        
        pass

	def unpacking_values(self, data):
		"""Public method in charge of unpacking values, ffrom catalogue to model, or from DB to model

		Args:

		data (tuple): Contain data to unpack into attributes

		"""

		pour chaque élément dans cursor_object:
			mettre ces attributs dans l''état(self, attr, value)

		pass
