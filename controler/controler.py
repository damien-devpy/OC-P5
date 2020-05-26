# coding: utf-8
"""Controler part of the app. Ensure logic of the app."""

from sys import exit as sys_exit
from configuration import ITEMS_TO_SHOW
from model.product import Product
from model.category import Category
from model.substitution import Substitution
from model.catalogue import Catalogue
from orm.manager import Manager
from view.view import View


class Controler():
    """Controler part of the app.

    Manage inputs from user and interaction between objects.

    """

    def __init__(self):
        """Init attributes of controler objects.

        Attributes:
            self._catalogue (catalogue object): Needed to get data from the
                api
            self._manager (manager object): Needed for interaction with DB
            self._vue (vue object): Needed for displaying ui

        """
        self._catalogue = Catalogue()
        self._manager = Manager()
        self._vue = View()

        self._page = None

    def controler(self):
        """Ensure logic of the app.

        Manage every part of the menu and interaction between objects.

        """
        # If database doesn't exist
        if not self._manager.is_there_db():
            # Getting data from the OpenFoodFacts API
            self._catalogue.get_data()

            # Creating database
            self._manager.create_db()

            # Inserting data in database
            self._manager.insert_all(self._catalogue.catalogue)

        self._manager.set_db()

        self._vue.help_menu()
        self._main_menu()

    def _main_menu(self):
        """Manage the main menu of the app."""
        self._vue.main_menu()

        input_user = input().lower()

        if input_user == '1':
            self._categories_menu()

        elif input_user == '2':
            self._substitution_menu()

        elif input_user == 'help':
            self._vue.help_menu()
            self._main_menu()

        elif input_user == 'exit':
            sys_exit()

        else:
            self._vue.make_correct_input()
            self._main_menu()

    def _categories_menu(self):
        """Manage the categories menu of the app."""
        self._page = 1

        # Getting list of categories from the database
        categories = self._manager.select(Category)

        # Displaying categories in a sub menu considering current page
        categories_to_show = self._paging(categories)
        self._vue.sub_menu(categories_to_show)

        # Allow the user to go through several categories
        # For making a choice
        category_choosed = self._navigation(categories, self._main_menu)

        self._products_menu(category_choosed)

    def _products_menu(self, category_choosed):
        """Manage the product menu of the app."""
        self._page = 1

        # Getting list of products from the category choosed
        products = self._manager.select_through_join(Category,
                                                     name=category_choosed.name
                                                     )

        # Displaying products in a sub menu considering current page
        products_to_show = self._paging(products)
        self._vue.sub_menu(products_to_show)

        # Allow the user to go through several products
        # for making a choice
        product_choosed = self._navigation(products, self._categories_menu)

        # Display details of the chosen product to substitute
        # and find a suitable one
        self._vue.old_product()
        self._vue.details_menu(product_choosed)
        self._find_substitute(product_choosed, category_choosed)

    def _find_substitute(self, product_choosed, category_choosed):
        """Find substitute for a product choose by user."""
        # Keeping id of the product to substitute
        id_old_product = product_choosed.id

        # Looking for a product substitute
        product_choosed.get_substitute(category_choosed.name)

        # If a substitute has been found
        if id_old_product != product_choosed.id:
            self._vue.new_product()
            self._vue.details_menu(product_choosed)
            self._vue.save_substitute()

            input_user = input().lower()

            # If user want to save the substitution
            # Record it
            if input_user == 'y':
                substitution = Substitution(id_to_substitute=id_old_product,
                                            id_substitute=product_choosed.id,
                                            )
                substitution.save()
                self._main_menu()

            # Get back to the previous menu
            elif input_user == 'back':
                self._products_menu(category_choosed)

            # Get back to the main menu
            elif input_user == 'main':
                self._main_menu()

            # Exit the app
            elif input_user == 'exit':
                sys_exit()

            else:
                self._main_menu()

        else:
            self._vue.better_product()
            self._main_menu()

    def _substitution_menu(self):
        """Manage the substitute menu of the app."""
        self._page = 1

        substitutions = self._manager.select(Substitution)

        # If there is some data in database:
        if substitutions:
            substitutions_to_show = self._paging(substitutions)
            self._vue.sub_menu(substitutions_to_show, sub=True)

            sub_choosed = self._navigation(substitutions,
                                           self._main_menu,
                                           sub=True,
                                           )

            old_product = Product()
            old_product.get(id=sub_choosed.id_to_substitute)
            new_product = Product()
            new_product.get(id=sub_choosed.id_substitute)

            # Display substitutions
            self._vue.details_menu(old_product, new_product)

            self._substitution_menu()

        else:
            self._vue.empty_menu()
            self._main_menu()

    def _navigation(self, items, func_reference, sub=False):
        """Manage the navigation through categories and products menus.

        Args:
            items (list): List of items displaying that user must to choose
            func_reference (function reference): Allow going back to the
                previous menu
            sub (bool): Default to False. If True, items
                is a list of substitution objects

        Return:
            item_choosed (...): Item choosed by user

        """
        input_user = input().lower()

        # If user want to display another page
        if any((input_user == "<", input_user == ">")):
            if input_user == "<":
                # Display previous page
                self._page -= 1
                items_to_show = self._paging(items)
                self._vue.sub_menu(items_to_show, sub)
                return self._navigation(items, func_reference, sub)

            else:
                # Display next page
                self._page += 1
                items_to_show = self._paging(items)
                self._vue.sub_menu(items_to_show, sub)
                return self._navigation(items, func_reference, sub)

        # Get back to the previous menu
        elif input_user == 'back':
            func_reference()

        # Get back to the main menu
        elif input_user == 'main':
            self._main_menu()

        # Display help menu
        elif input_user == 'help':
            self._vue.help_menu()
            return self._navigation(items, func_reference, sub)

        # Exit the app
        elif input_user == 'exit':
            sys_exit()

        else:
            items_to_show = self._paging(items)
            input_ok = False

            while not input_ok:
                try:
                    input_user = int(input_user)
                    input_ok = True

                except ValueError:
                    self._vue.make_correct_input()
                    self._vue.sub_menu(items_to_show, sub)
                    return self._navigation(items, func_reference, sub)

            # If input user match proposals
            if 1 <= input_user <= len(items_to_show):
                # Return item asked minus 1, id are shown from 1 to 10
                return items_to_show[input_user-1]

            else:
                self._vue.make_correct_input()
                self._vue.sub_menu(items_to_show, sub)
                return self._navigation(items, func_reference, sub)

    def _paging(self, list_of_items):
        """Paginate a iterable regarding a specific asked page.

        Args:
            list_of_items (list): A list of objects to paginate

        Return:
            list_of_items (list): Part of iterable matching the page asked

        """
        # How much pages are contains in the iterable
        total_pages = self._get_total_pages(list_of_items)

        # If user made a wrong input
        if not 1 <= self._page <= total_pages:
            self._fix_page_asked(total_pages)

        # Return items that match page asked
        if self._page == 1:
            return list_of_items[0:ITEMS_TO_SHOW]

        else:
            start, end = self._get_slices(list_of_items)

            return list_of_items[start:end]

    def _get_total_pages(self, list_of_items):
        """Return total pages that list_of_items can contains.

        Args:
            list_of_items (list): A list of objects to paginate

        Return:
            total_pages (int): Pages contains by list_of_items regarding
                ITEMS_TO_SHOW

        """
        # How much (ITEMS_TO_SHOW) is in list_of_items
        how_much_to_show = len(list_of_items) // ITEMS_TO_SHOW

        # Number of pages, for instance:
        # A list containing 42 items is a 5 pages list if ITEMS_TO_SHOW = 10
        total_pages = (how_much_to_show + 1
                       if len(list_of_items) % ITEMS_TO_SHOW
                       else how_much_to_show
                       )

        return total_pages

    def _fix_page_asked(self, total_pages):
        """Fix page_asked if the user made a wrong input.

        Args:
            total_pages (int): How much pages are contains in list_of_items

        """
        # Prevent user incorrect input
        if self._page < 1:
            # Setting to first one if negative
            self._page = 1

        elif self._page > total_pages:
            # Setting to last one if greater than total pages
            self._page = total_pages

    def _get_slices(self, list_of_items):
        """Determine slices regarding the page asked.

        Args:
            list_of_items (list): A list of objects to paginate

        Return:
            start (int): First slice
            end (int): Second slice

        """
        # Page start slice is (page - 1) * ITEMS_TO_SHOW
        start = ITEMS_TO_SHOW * (self._page - 1)

        # Page end slice is page * ITEMS_TO_SHOW if page is not the last one
        end = ((self._page * ITEMS_TO_SHOW)
               if ((self._page * ITEMS_TO_SHOW) < len(list_of_items))
               # Else end page slice is end of list
               else len(list_of_items)
               )

        return start, end
