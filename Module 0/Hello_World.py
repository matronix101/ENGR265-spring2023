# Welcome To Your First (maybe) Python File!!

# This one is going to be fairly simple, so don't fret

# Below this line is going to be a "print" function

# Right Click in this Window, and click "Run Hello_World.py"
# Then Look down to the bottom to see what happens!

# After your first run, try it out for yourself!

# YOUR CODE HERE #
"""Project 2: Crypto Portfolio.

Author: Matrix Chen
Version: 04/18/2023

Honor Code and Acknowledgments:
    This work complies with the JMU Honor Code.
"""
market = []


def add_check(symbol, price, amount):
    """Checks coins to see if it can be added.

    Args:
        symbol (str): The symbol.
        price (float): The price.
        amount (float): The amount owned.

    Returns:
        False if it fails any test.
    """
    if symbol not in market:
        return False
    if price is None:
        return False
    if price < 0.0:
        return False
    if price > 250000:
        return False
    if amount is None:
        return False
    if amount < 0.0:
        return False
    if amount > 1000000:
        return False


class Portfolio:
    """Represents the owned coin portfolios.

    Attributes:
        _coins (list): Coin data array.
        _market (Market): The market
    """

    def __init__(self, market):
        self._market = market
        self._coins = []

    def add_coin(self, symbol, price, amount):
        if (add_check(symbol, price, amount)) is False:
            return False
        else:
            objectified = tuple(symbol, price, amount)
            return_tuple = Portfolio(objectified)
            self._coins.append(return_tuple)
            return True

    def add_coins(self, coin_desc):
        pass
    def get_original_value(self):
        return self._get_original_value

    def get_current_value(self):
        return self._get_current_value

    def get_gain_loss(self):
        return self._gain_loss

    def get_best_earner(self):
        return self._get_best_earner

    def get_worst_earner(self):
        return self._get_worst_earner

    def get_coin(self, symbol):
        return self._get_coin

    def find_new_coin(self, search_term):
        pass
    def __str__(self):
        pass
# Generates a description of coin