# coding: utf-8

class Substitution:
	"""Model class of substitution table in database
	"""

	def __init__(self):
		"""init method

		Attributes:

			barre_code_to_substitute (int): column in substitution table
			barre_code_substitute (int): column in substition table

			header (list of str): header of the substitution table (barre_code_to_substitute, ...)
			table (str): name of the table

		"""