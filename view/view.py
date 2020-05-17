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
		print()


	def sub_menu(self, list_of_items, page):
		"""In charge of getting information to print considering
			page asked

		Args:

			list_of_items (list): List of items to print, considering
				page asked

			page (int): Page to show

		"""

		items_to_show = self.paging(list_of_items, page)

		for i, item in enumerate(items_to_show):

			print(f"{i+1} - {item.name}")

		print()


	def details_menu(self, item_to_detail):
		"""In charge of printing details of an item

		Args:

			details_item (iterable): An iterable to print

		"""

		for i, attr in enumerate(item_to_detail):

			if i > 0:
				print(attr)

			# Else, id attribute is not shown to the user
			else:
				continue

		print()


	def paging(self, list_of_items, page_asked):
		"""Paginate a iterable regarding a specific asked page

		Args:

			list_of_items (list): A list of objects to paginate
			page_asked (int): Which page of the iterable will be return

		Return:

			page (list): Part of iterable matching the page asked

		"""

		total_pages = self._get_total_pages(list_of_items)

		if any((page_asked < 1, page_asked > total_pages)):

			page_asked = self._fix_page_asked(list_of_items,
											  page_asked,
											  total_pages,
											 )

		# Return items that match page asked
		if page_asked == 1:
			return list_of_items[0:ITEMS_TO_SHOW]

		else:
			start, end = self._get_slices(list_of_items, page_asked)

			return list_of_items[start:end]


	def get_object_with_paging(self, list_of_items, page_asked, choice):
		"""Return an object in list_of_items based on a choice made from
			a list_of_items paged

		Args:

			list_of_items (list): A list of objects
			page_asked (int): At which page the user made is choice
			choice (int): Which item choosed in the page_asked

		Return:

			an_object (object): Matching object from the user choice

		"""

		# Element are displaying with an increment of 1
		choice -= 1

		if choice < 0:
			choice = 0

		elif choice > ITEMS_TO_SHOW:
			choice = ITEMS_TO_SHOW

		total_pages = self._get_total_pages(list_of_items)

		if any((page_asked < 1, page_asked > total_pages)):

			page_asked = self._fix_page_asked(list_of_items,
											  page_asked,
											  total_pages,
											 )


		start, end = self._get_slices(list_of_items, page_asked)
		list_paged = list_of_items[start:end]

		return list_paged[choice]


	def make_correct_input(self):
		"""Tell the user to make a correct input"""

		print("Please make a correct input")
		print()


	def make_substitution(self):
		"""Ask the user if he want to substitute current product"""

		print("Do you want to find a substitute for this product ?", end =' ')
		print("(y for yes, any other input for main menu)")
		print()

	def record_substitition(self):
		"""Ask the user if he want to record the substitution in database"""

		print("Do you want to save your substitution ?")
		print("Use 'y' for yes, any other input to get back to the main menu")
		print()

############################## PRIVATE METHODS ##############################

	def _get_total_pages(self, list_of_items):
		"""Return total pages that list_of_items can contains regarding
			ITEMS_TO_SHOW

		Args:

			list_of_items (list): A list of objects to paginate

		Return:

			total_pages (int): Pages contains by list_of_items regarding
				ITEMS_TO_SHOW

		"""

		# How much (ITEMS_TO_SHOW) is in list_of_items
		how_much_to_show = len(list_of_items) // ITEMS_TO_SHOW

		# Number of pages
		# A list containing 42 items is a 5 pages list if ITEMS_TO_SHOW = 10
		total_pages = (how_much_to_show + 1 
					   if len(list_of_items) % ITEMS_TO_SHOW 
					   else how_much_to_show
					  )


		return total_pages

	def _fix_page_asked(self, list_of_items, page_asked, total_pages):
		"""Set how much pages are contains in list_of_items regarding
			ITEMS_TO_SHOW
		   	Fixing page_asked if the user made a wrong input

		Args:

			list_of_items (list): A list of objects to paginate
			page_asked (int): Which page of the iterable will be return

		Return:

			page_asked (int): page_asked fixed if needed

		"""

		# Prevent user incorrect input
		if page_asked < 1:

			# Setting to first one if negative
			page_asked = 1

		elif page_asked > total_pages:

			# Setting to last one if greater than total pages
			page_asked = total_pages

		return page_asked


	def _get_slices(self, list_of_items, page_asked):
		"""Determine slices regarding the page asked

		Args:

			list_of_items (list): A list of objects to paginate
			page_asked (int): Which page of the iterable will be return

		Return:

			start (int): First slice
			end (int): Second slice

		"""

		# If ITEMS_TO_SHOW = 10 
		# And the fith page of a 42 list items is asked
		# Return (page_asked - 1) x ITEMS_TO_SHOW, which his 40 to 42 items
		prev_page = (page_asked - 1) if (page_asked > 1) else 1

		start = ITEMS_TO_SHOW * prev_page if prev_page != 1 else 0
		end = ((page_asked * ITEMS_TO_SHOW) 
			   if ((page_asked * ITEMS_TO_SHOW) < len(list_of_items)) 
			   else len(list_of_items)
			  )

		return start, end