# coding: utf-8

from configuration import ITEMS_TO_SHOW
from model.product import Product
import pdb

class View:
	"""In charge of the view part of the app"""

	def __init__(self):
		
		self.page = None


	def main_menu(self):
		"""Main menu of the app"""

		print()
		print("Main menu:")
		print("1. Pick up a product and find a substitute")
		print("2. Get back your old substitutions")
		print()
		print("How to use this app:")
		print()
		print("Making a choice: the number near your choice + Enter")
		print("Going back to the main menu anytime you want: 'back' + Enter")
		print()


	def sub_menu(self, list_of_items):
		"""In charge of getting information to print considering
			page asked

		Args:

			list_of_items (list): List of items to print

		"""

		items_to_show = self.paging(list_of_items)

		for i, item in enumerate(items_to_show):

			print(f"{i+1}. {item.name} ({item.id})")

		print()


	def sub_menu_substitution(self, list_of_items):
		"""In charge of printing old substitutions

			list_of_items (list): List of items to print

		"""

		print()

		items_to_show = self.paging(list_of_items)

		for i, item in enumerate(items_to_show):

			old_product = Product()
			old_product.get(id=item.id_to_substitute)
			new_product = Product()
			new_product.get(id=item.id_substitute)

			print(f"{i+1} - {old_product.name, old_product.nutrition_grade}",
				  end=''
				 )
			print(f" -> {new_product.name, new_product.nutrition_grade}")
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


	def paging(self, list_of_items):
		"""Paginate a iterable regarding a specific asked page

		Args:

			list_of_items (list): A list of objects to paginate

		Return:

			page (list): Part of iterable matching the page asked

		"""

		total_pages = self._get_total_pages(list_of_items)

		if not 1 <= self.page <= total_pages:

			self._fix_page_asked(list_of_items,
								 total_pages,
								)

		# Return items that match page asked
		if self.page == 1:
			return list_of_items[0:ITEMS_TO_SHOW]

		else:
			start, end = self._get_slices(list_of_items)

			return list_of_items[start:end]


	def get_object_with_paging(self, list_of_items, choice):
		"""Return an object in list_of_items based on a choice made from
			a list_of_items paged

		Args:

			list_of_items (list): A list of objects
			choice (int): Which item choosed in the page_asked

		Return:

			an_object (object): Matching object from the user choice

		"""

		# Element are displaying with an increment of 1
		choice -= 1

		total_pages = self._get_total_pages(list_of_items)

		if not 1 <= self.page <= total_pages:

			self._fix_page_asked(list_of_items,
							     total_pages,
								)


		start, end = self._get_slices(list_of_items)
		list_paged = list_of_items[start:end]

		# If user choice doesn't match proposal
		if choice < 0:

			choice = start

		elif choice >= ITEMS_TO_SHOW:

			# End slice exlude, so we need to substracte one
			choice = ITEMS_TO_SHOW - 1

		return list_paged[choice]


	def make_correct_input(self):
		"""Tell the user to make a correct input"""

		print("Please make a correct input")
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

	def _fix_page_asked(self, list_of_items, total_pages):
		"""Set how much pages are contains in list_of_items regarding
			ITEMS_TO_SHOW
		   	Fixing page_asked if the user made a wrong input

		Args:

			list_of_items (list): A list of objects to paginate

		"""

		# Prevent user incorrect input
		if self.page < 1:

			# Setting to first one if negative
			self.page = 1

		elif self.page > total_pages:

			# Setting to last one if greater than total pages
			self.page = total_pages


	def _get_slices(self, list_of_items):
		"""Determine slices regarding the page asked

		Args:

			list_of_items (list): A list of objects to paginate

		Return:

			start (int): First slice
			end (int): Second slice

		"""

		# Page start slice is (page - 1) * ITEMS_TO_SHOW
		start = ITEMS_TO_SHOW * (self.page - 1)

		# Page end slice is page * ITEMS_TO_SHOW if page is not the last one
		end = ((self.page * ITEMS_TO_SHOW) 
			   if ((self.page * ITEMS_TO_SHOW) < len(list_of_items))
			   # Else end page slice is end of list
			   else len(list_of_items)
			  )

		return start, end