# Welcome To Your First (maybe) Python File!!

# This one is going to be fairly simple, so don't fret

# Below this line is going to be a "print" function
#print("Hello, World!")

# Right Click in this Window, and click "Run Hello_World.py"
# Then Look down to the bottom to see what happens!

# After your first run, try it out for yourself!

# YOUR CODE HERE #

"""Exercise 6.3 Even More Basketball Stats.

Author: Matrix Chen
Version: 03/02/2023

Honor Code and Acknowledgments:
    This work complies with the JMU Honor Code.
"""


def print_stats(yes):
    """Printing out JMU basketball player stats.

    Args:
        yes (list): List of JMU womens basketball stats.

    Returns:
        s (str): Stats of JMU basketball and total stats.
    """
    totp = 0
    totr = 0
    tota = 0
    for among in range(len(yes)):
        part = yes[among]
        n = part[0]
        p = int(part[1])
        r = int(part[2])
        a = int(part[3])
        totp = totp + p
        totr = totr + r
        tota = tota + a
        p1 = f'{n} scored {p} points,'
        s1 = (f'{p1} grabbed {r} rebounds, and made {a} assists.')
        print(s1)
    s2 = (f'Total Points: {totp}')
    print(s2)
    s3 = (f'Total Rebounds: {totr}')
    print(s3)
    s4 = (f'Total Assists: {tota}')
    print(s4)


print_stats([('Emil',60,60,60)])