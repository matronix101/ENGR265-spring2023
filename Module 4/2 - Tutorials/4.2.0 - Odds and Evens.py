# For this tutorial, we will walk through how to find the odds and evens
# that are stored in a list, and count how many of each there are.

# Here are the two lists we will be working with:
list_one = [2, 23, 45, 64, 43, 3, 654, 57, 19, 38]
list_two = [1, -3, -64, 25, 70, 0, 74]

# Here are the counter variables for the evens and odds.
# In the For Loop, increase the appropriate one by one
# when an even or an odd is found!
one_evens = 0
one_odds = 0
evenz_1=[]
oddz_1=[]
evenz_2=[]
oddz_2=[]
# Hint: use if/else statements to set conditions in
# the For Loop to determine even or odd.


# Fill in this loop:
n=0
for element in list_one:
    if (list_one[n]) % 2 == 0:
        evenz_1.append(list_one[n])
        n = n + 1
    else:
        oddz_1.append(list_one[n])
        n = n + 1

# These statements can be used to check your work!
print("The number of odds in list_one is: " + str(oddz_1))
print("The number of evens in list_one is: " + str(evenz_1))

# Here are the counters for list_two:
two_evens = 0
two_odds = 0

# Now you do the rest!
w=0
for elementz in list_two:
    if (list_two[w]) % 2 == 0:
        evenz_2.append(list_two[w])
        w = w + 1
    else:
        oddz_2.append(list_two[w])
        w = w + 1

print("The number of odds in list_two is: " + str(oddz_2))
print("The number of evens in list_two is: " + str(evenz_2))












