import math

"""
Use the Gauss-Legendre Algorithm to estimate Pi. Perform 10 approximation loops. Once complete, return the approximation.
:return:
"""

# a variable to hold your returned estimate for PI. When you are done,
# set your estimated value to this variable. Do not change this variable name
pi_estimate = 3.141592653589793238462643383279502884197169399375105820974944
"""
Step 1: Declare and initialize all the values for the Gauss-Legendre algorithm
"""

# modify these lines to correct set the variable values
a = [1]
b = [1/math.sqrt(2)]
t = [1/4]
p = [1]
pp = []
# perform 10 iterations of this loop
for i in range(1, 10):
    """
    Step 2: Update each variable based upon the algorithm. Take care to ensure
    the order of operations and dependencies among calculations is respected. You
    may wish to create new "temporary" variables to hold intermediate results
    """

    ### YOUR CODE HERE ###
    a.append(((a[i-1])+(b[i-1]))/2)
    print(a)
    b.append(math.sqrt(a[i-1]*b[i-1]))
    print(b)
    t.append(t[i-1]-(p[i-1]*((a[i-1]-a[i])**2)))
    print(t)
    p.append(2*p[i-1])
    print(p)

    pp=(((a[i]+b[i])**2)/(4*t[i]))
    # print out the current loop iteration. This is present to have something in the loop.
    print("Loop Iteration: ", i)

"""
Step 3: After iterating 10 times, calculate the final value for PI
"""

# modify this line below to estimate PI
pi_estimate = pp

print("Final estimate for PI: ", pi_estimate)
print("Error on estimate: ", abs(pi_estimate - math.pi))
