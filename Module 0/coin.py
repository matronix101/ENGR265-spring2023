"""Project 2: Crypto Portfolio.

Author: Matrix Chen
Version: 04/09/2023

Honor Code and Acknowledgments:
    This work complies with the JMU Honor Code.
"""


class Coin:
    """Represents the coin value.

    Attributes:
        _symbol (str): Coin symbol.
        _name (str): Coin name.
        _price (float): Value of coin.
        _description (str): Description of coin.
    """

    def __init__(self, symbol, name, price, description):
        self._symbol = symbol
        self._name = name
        self._price = price
        self._description = description

    def get_symbol(self):
        return self._symbol

    def get_name(self):
        return self._name

    def get_price(self):
        return self._price

    def set_description(self, description):
        self._description = description

    def get_description(self):
        return self._description

    def __str__(self):
        # Generates a description of coin
        a = f'{self._symbol}: {self._name} is trading at {(self._price):.10f}'
        b = f'{self._name} {self._desc}'
        return (f'{a}\n{b}')

    def __eq__(self, other):
        return isinstance(other, Coin) and self._symbol == other.symbol \
               and self._name == other.name
