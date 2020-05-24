# coding: utf-8
"""Main file of the app."""

from controler.controler import Controler


def main():
    """Create an instance of class Controler.

    Call controler method and launch app.

    """
    controler = Controler()

    controler.controler()


if __name__ == "__main__":

    main()
