# coding: utf-8

import inspect

class ModelInspection:
	"""In charge of inspecting models, through module inspect"""

	def get_columns(self, object_to_inspect):
		"""Public method in charge of inspecting a model and returning columns
		which he represent

		Args:

			object_to_inspect (str): object instance we want to inspect
		
		Return:

			columns (tuple): Contain all columns of the model

		"""

		columns <- tuple(inspecter l''object_to_inspect)

		retourner columns

		pass

	def get_values(self, object_to_inspect):
		"""Public methode in charge of inspecting a model and returning values
		contains in attributes

		Args:

			object_to_inspect (str): object instance we want to inspect

		Return:

			values (tuple): Contain all values in attributes of the instance of object_to_inspect

		"""

		values <- tuple(inspecter l''object_to_inspect)

		retourner values

		pass