# Welcome To Your First (maybe) Python File!!

# This one is going to be fairly simple, so don't fret

# Below this line is going to be a "print" function
#print("Hello, World!")

# Right Click in this Window, and click "Run Hello_World.py"
# Then Look down to the bottom to see what happens!

# After your first run, try it out for yourself!

# YOUR CODE HERE #
"""Exercise 5.3 Date Types and Multiple Returns.

Author: Matrix Chen
Version: 02/23/2023

Honor Code and Acknowledgments:
    This work complies with the JMU Honor Code.
"""

wk = (2, 3, 4, 5, 6)

s1 = (9, 10, 11)
s2 = (1, 2, 12)
s3 = (3, 4, 5)
s4 = (6, 7, 8)


def date_analysis(, b, c):
    """Generate date responses based on day, # month, and # day.

    Args:
        day (str): The phrase to print what type of day it is.
        season (str): The phrase to print what season it is.
        quarter (str): The phrase to print what quarter it is

    """
    if (a == 1) or (a == 7):
        a1 = ('weekend')
    elif (a >= 2) and (a <= 6):
        a1 = ('weekday')
    else:
        a1 = ('invalid')

    if b in s1:
        b1 = ('Fall')
    elif b in s2:
        b1 = ('Winter')
    elif b in s3:
        b1 = ('Spring')
    elif b in s4:
        b1 = ('Summer')
    else:
        b1 = ('Invalid')

    if c <= 0:
        c1 = 0
    elif c > 0 and c <= 7:
        c1 = 1
    elif c > 7 and c <= 14:
        c1 = 2
    elif c > 14 and c <= 21:
        c1 = 3
    elif c > 21 and c <= 28:
        c1 = 4
    else:
        c1 = 5

    w = (a1, b1, c1)
    return w
