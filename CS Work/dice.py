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
    if (dies < 1) or (dies > 10):
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
    list_len = 20
    acceptable_die = [1, 2, 3, 4, 5, 6]
    if rand_list is not None:
        list_len = len(rand_list)
    counter_valid = 0

    '''Checks to see if the # of die are between 0~10'''
    if (list_len > 0) and (list_len < 10):
        for i in range(list_len):
            '''Checks to see if the die are between 1~6'''
            if rand_list[i] in acceptable_die:
                counter_valid += 1
            if rand_list[i] not in acceptable_die:
                return False

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
    adding_sum = 0
    '''Counting occurrences'''
    for i in dies:
        if i == check:
            adding_sum += 1

    if (len(dies) < 1) or (len(dies) > 10) or (are_valid(dies) is False):
        adding_sum = -1
    if check is None:
        adding_sum = 0

    return adding_sum


def add_values(dies_list):
    """Summing Dice.

    Args:
        dies_list (list): The list of dies.

    Returns:
        total_addval (int): The sum of dies.
    """
    total_addval = -1
    if (len(dies_list) > 0) and (len(dies_list) < 11):
        if are_valid(dies_list) is True:
            total_addval = sum(dies_list)
    return total_addval
