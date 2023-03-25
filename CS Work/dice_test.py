"""Project 1: Chuck-a-luck.

Author: Matrix Chen
Version: 03/23/2023

Honor Code and Acknowledgments:
    This work complies with the JMU Honor Code.
"""

import driver
import chuck_a_luck
import test_chuck_a_luck
import dice

import dice


def test_roll_dice():
    assert dice.roll_dice() == [4, 4, 1]


def test_are_valid():
    assert dice.are_valid([1, 2, 3])


def test_add_values():
    assert dice.add_values([1, 2, 3]) == 6


def test_count_values():
    assert dice.count_values([4, 4, 1], 4) == 2

