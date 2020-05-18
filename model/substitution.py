# coding: utf-8

from model.model import Model

class Substitution(Model):
	"""Model class of substitution table in database
	"""

	# Table name in database this model class represent
	TABLE_NAME = "substitution"

	# How much columns this model class has as attributes
	# in declaration order
	COLUMNS = 3

	def __init__(self, **kwargs):
		"""init method

		Args:

			**kwargs (dict): Variable number of arguments

		Attributes:

			self._barre_code_to_substitute (int): attribute that represent barre_code_to_substitute column in DB
 			self._barre_code_substitute (int): attribute that represent barre_code_substitute column in DB

		"""

		self.id = kwargs.get('id')
		self.id_to_substitute = kwargs.get('id_to_substitute')
		self.id_substitute = kwargs.get('id_substitute')

		Model.__init__(self)
		self.ignore = True