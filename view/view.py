# coding: utf-8

from configuration import ITEMS_TO_SHOW
import pdb

class View:
	"""In charge of the view part of the app"""

	def __init__(self):
		pass


	def main_menu(self):
		"""Main menu of the app"""

		print("Menu principal:")
		print("1. Choissisez un aliment à substituer")
		print("2. Retrouvez vos précédentes substitutions")



	def sub_menu(self, list_of_items, page):
		"""In charge of getting information to print considering
			page asked

		Args:

			list_of_items (list): List of items to print, considering
				page asked

			page (int): Page to show

		"""

		items_to_show = paging(list_of_items, page)

		for i, item in enumerate(items_to_show):

			for j, element in enumerate(item):

				if j > 0:
					print(i, element)

				# id of the object is not shown to the user
				else:
					continue



	def details(self, details_item):
		"""In charge of printing details of an item

		Args:

			details_item (iterable): An iterable to print

		"""

		for i in details_item:
			print(i)



	def paging(self, list_of_items, page_asked):
		"""Paginate a iterable regarding a specific asked page

		Args:

			list_of_items (list): A list of items to paginate
			page_asked (int): Which page of the iterable will be return

		Return:

			page (list): Part of iterable matching the page asked

		"""

		# How much (ITEMS_TO_SHOW) is in list_of_items
		how_much_to_show = len(list_of_items) // ITEMS_TO_SHOW

		# Number of pages
		# A list containing 42 items is a 5 pages list if ITEMS_TO_SHOW = 10
		total_pages = (how_much_to_show + 1 
					   if len(list_of_items) % ITEMS_TO_SHOW 
					   else how_much_to_show
					  )

		# Prevent user incorrect input
		if page_asked < 1:

			# Setting to first one if negative
			page_asked = 1

		elif page_asked > total_pages:

			# Setting to last one if greater than total pages
			page_asked = total_pages


		# Return items that match page asked
		if page_asked == 1:

			return list_of_items[0:ITEMS_TO_SHOW]

		else:

			# If ITEMS_TO_SHOW = 10 
			# And the fith page of a 42 list items is asked
			# Return (page_asked - 1) x ITEMS_TO_SHOW, which his 40 to 42 items

			prev_page = (page_asked - 1) if (page_asked > 1) else 1

			start = ITEMS_TO_SHOW * prev_page
			end = ((page_asked * ITEMS_TO_SHOW) 
				   if ((page_asked * ITEMS_TO_SHOW) < len(list_of_items)) 
				   else len(list_of_items)
				  )

			return list_of_items[start:end]


	def make_correct_input(self):
		"""Tell the user to make a correct input"""

		return "Please make a correct input"
