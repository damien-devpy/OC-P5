# coding: utf-8
"""Child class of Model, representing table category in database."""

from model.model import Model
import model.product


class Category(Model):
    """Model class of the category table in database."""

    # Table name in database this model class represent
    TABLE_NAME = "category"

    def __init__(self, **kwargs):
        """Init attributes of category objects.

        Args:
            **kwargs (dict): Variable number of arguments

        Attributes:
            self._id_cat (int): attribute that represent id column in DB
            self._name (str): attribute that represent name column in DB

        """
        Model.__init__(self)
        self._duplicate_key = True
        self._liaison_table = model.product.Product

        self.id = kwargs.get('id')
        self.name = kwargs.get('name')
