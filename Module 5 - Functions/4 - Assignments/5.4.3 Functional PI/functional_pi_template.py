import math

a = [1]
b = [1 / math.sqrt(2)]
t = [1 / 4]
p = [1]
pp = []

def my_pi(target_error):
    """
    Implementation of Gauss–Legendre algorithm to approximate PI from https://en.wikipedia.org/wiki/Gauss%E2%80%93Legendre_algorithm

    :param target_error: Desired error for PI estimation
    :return: Approximation of PI to specified error bound
    """
    totalz = int(1/desired_error)
    for i in range (1,totalz):

        a.append(((a[i-1])+(b[i-1]))/2)
        b.append(math.sqrt(a[i-1]*b[i-1]))
        t.append(t[i-1]-(p[i-1]*((a[i-1]-a[i])**2)))
        p.append(2*p[i-1])
        pp.append(((a[i]+b[i])**2)/(4*t[i]))
        final = pp[-1]


    ### YOUR CODE HERE ###
    return final


desired_error = 1E-3


approximation = my_pi(desired_error)

print("Solution returned PI=", approximation)

error = abs(math.pi - approximation)

if error < abs(desired_error):
    print("Solution is acceptable")
else:
    print("Solution is not acceptable")
