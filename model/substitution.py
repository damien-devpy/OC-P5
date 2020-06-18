# coding: utf-8
"""Parent class of Model, representing table substitution in database."""

from model.model import Model


class Substitution(Model):
    """Class of substitution table in database."""

    # Table name in database this model class represent
    TABLE_NAME = "substitution"

    def __init__(self, **kwargs):
        """Init attributes of substitution objects.

        Args:
            **kwargs (dict): Variable number of arguments

        Attributes:
            self._id_to_substitute (int): attribute that represent
                id_to_substitute column in DB
            self._id_substitute (int): attribute that represent
                id_substitute column in DB

        """
        Model.__init__(self)
        self._ignore = True

        self._id = kwargs.get('id')
        self._id_to_substitute = kwargs.get('id_to_substitute')
        self._id_substitute = kwargs.get('id_substitute')

    @property
    def id(self):
        """Return private attribute id"""
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def id_to_substitute(self):
        """Return private attribute id_to_substutite"""
        return self._id_to_substitute

    @id_to_substitute.setter
    def id_to_substitute(self, value):
        self._id_to_substitute = value

    @property
    def id_substitute(self):
        """Return private attribute id_to_substutite"""
        return self._id_substitute

    @id_substitute.setter
    def id_substitute(self, value):
        self._id_substitute = value

        
