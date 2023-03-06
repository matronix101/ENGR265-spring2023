# Welcome To Your First (maybe) Python File!!

# This one is going to be fairly simple, so don't fret

# Below this line is going to be a "print" function
#print("Hello, World!")

# Right Click in this Window, and click "Run Hello_World.py"
# Then Look down to the bottom to see what happens!

# After your first run, try it out for yourself!

# YOUR CODE HERE #

"""Exercise 6.4 Street Addresses.

Author: Matrix Chen
Version: 03/05/2023

Honor Code and Acknowledgments:
    This work complies with the JMU Honor Code.
"""


def encode(name, move):
    """Printing out JMU basketball player stats.

    Args:
        name (str): The name of the adress.
        move (int): The shift in the string.

    Returns:
        neo (str): The inital string shifted.
    """
    blank = ''
    for count in name:
        if ord(count) > 65 and ord(count) < 91:
            blank = blank + chr(((ord(count) - 97 + move) % 26) + 97)
        if ord(count) > 96 and ord(count) < 123:
            blank = blank + chr(((ord(count) - 97 + move) % 26) + 97)
        else:
            blank = blank + count

    neo = blank
    return neo
if __name__ == "__main__":
    print(encode("this shouldn't change", 0))