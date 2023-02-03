import random

"""
THIS SECTION IS DR. FORSYTH'S CODE. DO NOT MODIFY. BUT KEEP READING.
"""
# randomly sample a distribution between 1 and 5
random_number = int(random.uniform(1, 5))

# any number times 2 is even, add one to make it odd
an_odd_number = 2 * random_number + 1

# generate a random list of odd length containing values up to 100
odd_list = random.sample(range(100), an_odd_number)

# print out the list contents
print("Your list is: ", odd_list)

"""
YOUR CODE BEGINS BELOW HERE. FILL IN THE MISSING OPERATIONS / CODE
"""
#2.4.1 Odd Lists
list_yeah=odd_list #[8, 2, 6 ,4 ,1 ,5 ,1 ,4 ,8 ,4]
#len(list_yeah)
w=(len(list_yeah)//2)+1
a=(list_yeah[w-1])

# use len() to find the length of the list
list_length = len(list_yeah) #modify this line to perform the correct operation

# now calculate the middle index of the list
middle_index = w #modify this line to perform the correct operation

# use [] to access the middle element. Set it equal to middle_element
middle_element = a  #modify this line to perform the correct operation

# print out the middle_element
print("The middle element is: ", middle_element)
