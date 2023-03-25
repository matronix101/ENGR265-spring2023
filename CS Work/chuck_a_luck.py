"""Computes the payout for Chuck-a-luck.

Author: Matrix Chen
Version: 03/21/2023

Honor Code and Acknowledgments:
    This work complies with the JMU Honor Code.
"""

# Constants that specify bet types
SINGLE = 1
TRIPLE = 2
BIG = 3
SMALL = 4
FIELD = 5

# Constants that specify payout multipliers
SINGLE_ONE_ODDS = 1.0
SINGLE_TWO_ODDS = 2.0
SINGLE_THREE_ODDS = 10.0
TRIPLE_ODDS = 30.0
BIG_ODDS = 1.0
SMALL_ODDS = 1.0
FIELD_ODDS = 1.0


def calculate_payout(dice_list, bet_type, number, bet_amount):
    """Calculate the correct Chuck-a-luck payout based on the given arguments.

    Args:
        dice_list (list): A list of 3 dice values representing the outcome of the rolls.
        bet_type (int): The type of the bet, SINGLE, TRIPLE, BIG, etc.
        number (int): The number of the bet, 1-6.
        bet_amount (float): The amount of the bet in dollars.

    Returns:
        float: The payout amount in dollars. This will be a negative number for a losing bet.
    """
    total_return = 0.0

    """ Single Checker """
    if bet_type == 1:
        if number == dice_list[0]:
            total_return += (bet_amount * SINGLE_ONE_ODDS)
        if number == dice_list[1]:
            total_return += (bet_amount * SINGLE_TWO_ODDS)
        if number == dice_list[2]:
            total_return += bet_amount
    if total_return == 3 * bet_amount:
        total_return = SINGLE_THREE_ODDS * bet_amount

    """ Triple checker """
    if bet_type == 2:
        if ((sum(dice_list)) / 3) == (dice_list[0]):
            if ((sum(dice_list)) / 3) == (dice_list[1]):
                if ((sum(dice_list)) / 3) == (dice_list[2]):
                    bet_amount *= TRIPLE_ODDS

    """Big Check"""
    if bet_type == 3:
        if sum(dice_list) > 10:
            total_return += bet_amount

    """Small Check"""
    if bet_type == 4:
        if sum(dice_list) < 11:
            total_return += bet_amount

    """Field Check"""
    field_list = [3, 4, 5, 6, 7, 13, 14, 15, 16, 17, 18]
    if bet_type == 5:
        if sum(dice_list) in field_list:
            total_return += bet_amount

    """Final Work"""
    payout = float(total_return)

    if payout == 0.0:
        payout = -bet_amount

    # For any losing roll the payout will be a negative number equal to the value of the bet.
    # For example, on a losing $3.00 bet, the payout will be -$3.00.
    # Write an if/then/else conditional statement to evaluate the payout.
    # Cases that require more than a few lines of code should be handled
    # in separate methods below. Each case should set the value of the
    # payout variable, so that you will have only one return statement.
    return payout

