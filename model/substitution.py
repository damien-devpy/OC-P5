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

        self.id = kwargs.get('id')
        self.id_to_substitute = kwargs.get('id_to_substitute')
        self.id_substitute = kwargs.get('id_substitute')
