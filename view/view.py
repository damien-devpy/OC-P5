# coding: utf-8

from model.product import Product


class View:
    """In charge of the view part of the app."""

    def main_menu(self):
        """Display main menu of the app."""
        print("\nMain menu:")
        print("1. Pick up a product and find a substitute")
        print("2. Get back your old substitutions\n")

    def help_menu(self):
        """Display help menu of the app."""
        print("\nHelp menu - How to use this app")
        print("- id near your choice + enter for choosing")
        print("- 'main' for getting back to the main menu")
        print("- 'back' for previous menu")
        print("- 'exit' for exit (: \n")

    def save_substitute(self):
        print("\nDo you want to save this substitution ?", end=' ')
        print("('y' for yes)\n")

    def better_product(self):
        print("\nYou already have the safest product !\n")

    def make_correct_input(self):
        """Tell the user to make a correct input."""
        print("Please make a correct input\n")

    def empty_menu(self):
        """Inform user there is nothing yet."""
        print("\nNothing recorded yet !\n")

    def sub_menu(self, list_of_items, sub=False):
        """Get information to print considering page asked.

        Args:
            list_of_items (list): List of items to print
            sub (bool): Default to False. If True, list_of_items
                is a list of substitution objects

        """
        print()

        if not sub:

            for i, item in enumerate(list_of_items):

                print(f"{i+1}. {item.name} ({item.id})")

            print()

        else:

            self._sub_menu_substitution(list_of_items)

    def _sub_menu_substitution(self, list_of_items):
        """In charge of printing old substitutions.

        Args:
            list_of_items (list): List of items to print

        """
        print()

        for i, item in enumerate(list_of_items):

            old_product = Product()
            old_product.get(id=item.id_to_substitute)
            new_product = Product()
            new_product.get(id=item.id_substitute)

            print(f'{i+1} - '
                  f'{old_product.id}',
                  f'{old_product.name}',
                  f'{old_product.nutrition_grade}',
                  f'{old_product.brand}',
                  end=''
                  )

            print(f' -> '
                  f'{new_product.id}',
                  f'{new_product.name}',
                  f'{new_product.nutrition_grade}',
                  f'{new_product.brand}'
                  )
            print()

    def details_menu(self, *item_to_detail):
        """In charge of printing details of an item.

        Args:
            details_item (iterable): An iterable to print

        """
        for item in item_to_detail:

            for i, attr in enumerate(item):

                if i > 0:
                    print(attr)

                # Else, id attribute is not shown to the user
                else:
                    continue

            print()
