import random

"""
THIS SECTION IS DR. FORSYTH'S CODE. DO NOT MODIFY. BUT KEEP READING.
"""

# randomly sample a distribution between 2 and 6
random_number = int(random.uniform(2, 6))

# any number times 2 is even
an_odd_number = 2 * random_number

# generate a random list of odd length containing values up to 100
even_list = random.sample(range(100), an_odd_number)

# print out the list contents
print("Your list is: ", even_list)

"""
YOUR CODE BEGINS BELOW HERE. FILL IN THE MISSING OPERATIONS / CODE
"""
#2.4.2 Even Lists
#len(list_yeah)
list_yeah=even_list
x=(len(list_yeah)//2)
y=(list_yeah[x-1])
z=(list_yeah[x])
a=((y+z)/2)

# this is the final result. Modify this line, and the empty lines above, to solve the assignment
middle_average = a

# the average of middle elements is
print("The average is: ", middle_average)
