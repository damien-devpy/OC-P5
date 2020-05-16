# coding: utf-8

from models.model import Model

class Substitution(Model):
	"""Model class of substitution table in database
	"""

	TABLE_NAME = "substitution"
	COLUMNS = 3

	def __init__(self, **kwargs):
		"""init method

		Args:

			**kwargs (dict): Variable number of arguments

		Attributes:

			self._barre_code_to_substitute (int): attribute that represent barre_code_to_substitute column in DB
 			self._barre_code_substitute (int): attribute that represent barre_code_substitute column in DB

		"""

		self.id = kwargs.get['id']
		self.barre_code_to_substitute = kwargs.get('barre_code_to_substitute')
		self.barre_code_substitute = kwargs.get('barre_code_substitute')