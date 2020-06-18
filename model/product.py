# coding: utf-8
"""Parent class of Model, representing table product in database."""

from model.model import Model
from orm.manager import Manager
import model.category


class Product(Model):
    """Class of the product table in database."""

    # Table name in database this model class represent
    TABLE_NAME = "product"

    def __init__(self, **kwargs):
        """Init attributes of product objects.

        Args:
            **kwargs (dict): Variable number of arguments

        Attributes:
            self._barre_code (int): attribute that represent barre_code column
                in DB
            self._name (str): attribute that represent name column in DB
            self._nutrition_grade (str): attribute that represent
                nutrition_grade column in DB
            self._brand (str): attribute that represent brand column in DB
            self._store (str): attribute that represent store column in DB
            self._ingredients (str): attribute that represent ingredients
                column in DB
            self._quantity (str): attribute that represent quantity column
                in DB

        """
        Model.__init__(self)
        self._liaison_table = model.category.Category

        self._id = kwargs.get('id')
        self._barre_code = kwargs.get('barre_code')
        self._name = kwargs.get('name')
        self._nutrition_grade = kwargs.get('nutrition_grade')
        self._brand = kwargs.get('brand')
        self._store = kwargs.get('store')
        self._ingredients = kwargs.get('ingredients')
        self._quantity = kwargs.get('quantity')

    @property
    def id(self):
        """Return private attribute id"""
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def barre_code(self):
        """Return private attribute barre_code"""
        return self._barre_code

    @barre_code.setter
    def barre_code(self, value):
        self._barre_code = value

    @property
    def name(self):
        """Return private attribute name"""
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def nutrition_grade(self):
        """Return private attribute nutrition_grade"""
        return self._nutrition_grade

    @nutrition_grade.setter
    def nutrition_grade(self, value):
        self._nutrition_grade = value

    @property
    def brand(self):
        """Return private attribute brand"""
        return self._brand

    @brand.setter
    def brand(self, value):
        self._brand = value

    @property
    def store(self):
        """Return private attribute store"""
        return self._store

    @store.setter
    def store(self, value):
        self._store = value

    @property
    def ingredients(self):
        """Return private attribute ingredients"""
        return self._ingredients

    @ingredients.setter
    def ingredients(self, value):
        self._ingredients = value

    @property
    def quantity(self):
        """Return private attribute quantity"""
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        self._quantity = value        

    def get_substitute(self, chosen_category):
        """Look for a product substitute.

        Args:
            chosen_category (str): Category choosed by user, for a product
                substitution

        """
        with Manager() as manager:
            manager.set_db()
            manager.substitution(self, chosen_category)
