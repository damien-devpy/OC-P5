# coding: utf-8
"""View part of the app. Display all ui."""

from configuration import URL_FOR_PRODUCT
from model.product import Product
from model.category import Category


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
        """Ask user if he want to save current substitution."""
        print(f"{'_':_^200}")
        print("Do you want to save this substitution ?", end=' ')
        print("('y' for yes)\n")

    def better_product(self):
        """Inform user he alreay have the best product."""
        print("\nYou already have the safest product !\n")

    def make_correct_input(self):
        """Tell the user to make a correct input."""
        print("Please make a correct input\n")

    def empty_menu(self):
        """Inform user there is nothing yet."""
        print("\nNothing recorded yet !\n")

    def old_product(self):
        """Display old product mention."""
        print(f"\n\n{'Old product':_^200}")

    def new_product(self):
        """Display new product mention."""
        print(f"{'New product':_^200}")

    def sub_menu(self, list_of_items, sub=False):
        """Get information to print considering page asked.

        Args:
            list_of_items (list): List of items to display
            sub (bool): Default to False. If True, list_of_items
                is a list of substitution objects

        """
        if not sub:
            if isinstance(list_of_items[0], Category):
                print(f"\n{'Categories':_^200}\n")

                for i, item in enumerate(list_of_items):
                    print(f"{i+1} - ", end="")
                    print(f"{item.name}")

            elif isinstance(list_of_items[0], Product):
                print(f"\n{'Products':_^200}\n")
                print(f"{' Nom':<70} {'Nutriscore':<40}"
                      f"{'Brand':<40} {'Quantity'}"
                      )

                for i, item in enumerate(list_of_items):
                    line = (f"{i+1:>2} - {item.name:<70}"
                            f"{item.nutrition_grade:<35}"
                            f"{item.brand:<45}"
                            f"{item.quantity}"
                            )

                    print(f"{line}")

        else:
            self._sub_menu_substitution(list_of_items)

    def _sub_menu_substitution(self, list_of_items):
        """In charge of printing old substitutions.

        Args:
            list_of_items (list): List of items to print

        """
        for i, item in enumerate(list_of_items):

            old_product = Product()
            old_product.get(id=item.id_to_substitute)
            new_product = Product()
            new_product.get(id=item.id_substitute)

            print(f"\n{i+1} - "
                  f"{old_product.name} - "
                  f"Nutritrion grade: {old_product.nutrition_grade}\n"
                  )
            print(f"{'------>':<10}", end='')
            print(f"{new_product.name} - "
                  f"Nutritrion grade: {new_product.nutrition_grade}"
                  f" ({URL_FOR_PRODUCT + str(new_product.barre_code)})\n"
                  )

    def details_menu(self, *item_to_detail):
        """In charge of printing details of an item.

        Args:
            item_to_detail (iterable): An iterable to print

        """
        print('Details product')

        for item in item_to_detail:

            print(f"{'_':_^200}")
            print(f"{'Barre code: ':>2}", end='')
            print(f"{item.barre_code}\n")
            print(f"{'Product name: '+item.name:>2}\n")
            print(f"{'Nutrition grade: '+item.nutrition_grade:>2}\n")
            print(f"{'Brand: '+item.brand:>2}\n")
            print(f"{'Where to find it: '+item.store:>2}\n")
            print(f"{'Link to the product: '+URL_FOR_PRODUCT+str(item.barre_code):>2}\n")
            print(f"{'Details: '+item.ingredients:>2}\n")
            print(f"{'_':_^200}")
            print()
