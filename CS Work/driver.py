"""Simple command-line version of the Chuck-a-luck game.

@Author Nathan Sprague python version Alvin Chao
@Version 2/17/2016 2/22/2023
"""

import dice
import chuck_a_luck


def one_bet():
    """Handle one betting interaction with the user.

    This method will ask the user what bet they want to place, and how much they want to wager.

    Returns:
        (double): Amount that the player won or lost on the bet
    """
    # create a set of dice which is a list with 3 random die values 1-6.
    chuck_dice = dice.roll_dice(3, None)
    die1 = chuck_dice[0]
    die2 = chuck_dice[1]
    die3 = chuck_dice[2]
    bet_type = 0
    number = -1  # This will be ignored unless the bet is SINGLE
    bet_amount = 0.0
    payout = 0.0
    bet_prompt = "\nWhat is your bet?\n" + str(chuck_a_luck.SINGLE) + "- Single\n"
    bet_prompt += str(chuck_a_luck.TRIPLE) + "- Triple\n"
    bet_prompt += str(chuck_a_luck.BIG) + "- Big\n" + str(chuck_a_luck.SMALL) + "- Small\n"
    bet_prompt += str(chuck_a_luck.FIELD) + "- Field\n" + "Bet: "
    bet_type = int(input(bet_prompt))
    if (bet_type == chuck_a_luck.SINGLE):
        number = int(input("Which number will you bet? (1-6) "))
    bet_amount = float(input("How much do you want to bet? "))
    print("You rolled: " + str(die1) + " " + str(die2) + " " + str(die3))
    payout = chuck_a_luck.calculate_payout(chuck_dice, bet_type, number, bet_amount)
    if (payout <= 0):
        print("Better luck next time!")
    else:
        print(f"Congratulations! You won ${payout:,.2f}!\n")
    return payout


if __name__ == "__main__":
    keep_playing = "y"
    total_winnings = 0.0
    print("Welcome to Chuck-a-luck!")
    while (keep_playing == "y" or keep_playing == "1"):
        total_winnings += one_bet()
        print(f"Your total winnings are ${total_winnings:,.2f}\n")
        keep_playing = input("Play again? (y/n) ").lower()
    print("Thanks for playing!")


