"""Dice.

Author: Matrix Chen
Version: 03/26/2023

Honor Code and Acknowledgments:
    This work complies with the JMU Honor Code.
"""
import random


def roll_dice(dices, random_number=0):
    """Rolling Dice.

    Args:
        dices (int): The number of die.
        random_number (int): The seed number to remember it.

    Returns:
        dice_list (list): The list of dice.
    """
    '''Dice List that will be full later'''
    dice_list = []
    dies = dices
    random.seed(random_number)

    '''If more than 10 die or less than 1 die'''
    if (dies < 1) and (dies > 10):
        dice_list = [6]
    '''If between 1 and 10 die'''
    if (dies > 0) and (dies < 11):
        for i in range(dies):
            new_dice = random.randint(1, 6)
            dice_list.append(new_dice)
    '''If nothing is input'''
    if (dices is None) and (random_number == 0):
        for i in range(4):
            new_dice = random.randint(1, 6)
            dice_list.append(new_dice)
    return dice_list


def are_valid(rand_list):
    """Validate Dice.

    Args:
        rand_list (list): The list of dies.

    Returns:
        True if the list is acceptable, False if the list is unacceptable.
    """
    acceptable_die = [1, 2, 3, 4, 5, 6]
    list_len = len(rand_list)
    counter_valid = 0

    '''Checks to see if the # of die are between 0~10'''
    if (list_len > 0) and (list_len < 10):
        for i in range(list_len):
            '''Checks to see if the die are between 1~6'''
            if rand_list[i] in acceptable_die:
                counter_valid += 1

    if counter_valid == list_len:
        return True

    if counter_valid != list_len:
        return False


def count_values(dies, check=None):
    """Counting Dice Occurrences.

    Args:
        dies (list): The list of dies.
        check (int): The number to check.

    Returns:
        counter _value (int): The amount of occurrences.
    """
    counter_value = 0
    '''Counting occurrences'''
    for i in range(len(dies)):
        if i == check:
            counter_value += 1

    if (len(dies) < 1) or (len(dies) > 10) or (check is None):
        counter_value = -1

    return counter_value


def add_values(dies_list):
    """Summing Dice.

    Args:
        dies_list (list): The list of dies.

    Returns:
        total_sum (int): The sum of dies.
    """
    if (len(dies_list) > 0) and (len(dies_list) < 11):
        if are_valid(dies_list) is True:
            total_sum = sum(dies_list)
        if are_valid(dies_list) is False:
            total_sum = -1
    return total_sum
