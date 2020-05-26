# coding: utf-8
"""Parent class for child class representing table in database."""

from orm.manager import Manager


class Model:
    """Parent model class representing table database."""

    # How much attributes are define for DB behaviour
    DB_ATTRIBUTES = 4

    def __init__(self):
        """Init attributes of classes instances who inherits from Model.

        Attributes:
            self._duplicate_key (bool): Default to False. Set this attribute
                True if there is a risk for registering twice the same
                information in database but you don't want to ignore it.

            self._ignore (bool): Default to False. Set this attribute True
                for database to ignore a row if an information match a unique
                key already registered.

            self._belong_to (list): Filled for representing a many to many
                relationship.

            self._liaison_table (class reference): Default to None. Filling it
                with name of the table which there is a many to many relation.

        """
        self._duplicate_key = False

        self._ignore = False

        self._belong_to = list()

        self._liaison_table = None

    def save(self):
        """Insert data through the manager."""
        manager = Manager()
        manager.set_db()

        manager.insert_one_at_a_time(self)

    def get(self, **kwargs):
        """Get data from a specific key/value keyword argument."""
        manager = Manager()
        manager.set_db()

        manager.select(self, **kwargs)

    def attrs(self):
        """Return an iterator of attributes names of self.

        Only attributes representing columns in DB.

        """
        return (attr
                for i, attr in enumerate(self.__dict__.keys())
                if i >= Model.DB_ATTRIBUTES)

    def values(self):
        """Return an interator of attributes values of self.

        Only attributes representing columns in DB.

        """
        return (value
                for i, value in enumerate(self.__dict__.values())
                if i >= Model.DB_ATTRIBUTES)

    @property
    def duplicate_key(self):
        """Return bool private attribute."""
        return self._duplicate_key

    @property
    def ignore(self):
        """Return bool private attribute."""
        return self._ignore

    @property
    def belong_to(self):
        """Return list private attribute."""
        return self._belong_to

    @belong_to.setter
    def belong_to(self, value):
        self._belong_to = value

    @property
    def liaison_table(self):
        """Return many to many relationship private attribute."""
        return self._liaison_table
