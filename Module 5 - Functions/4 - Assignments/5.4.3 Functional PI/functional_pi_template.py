import math

#a = [1]
#b = [1 / math.sqrt(2)]
#t = [1 / 4]
#p = [1]
#pp = []

a=1
b=1/math.sqrt(2)
t=1/4
p=1

def my_pi(target_error):
    """
    Implementation of Gauss–Legendre algorithm to approximate PI from https://en.wikipedia.org/wiki/Gauss%E2%80%93Legendre_algorithm

    :param target_error: Desired error for PI estimation
    :return: Approximation of PI to specified error bound
    """
    totalz = int(1/desired_error)
    current_error = 2*desired_error

    z=0
    a = 1
    b = 1 / math.sqrt(2)
    t = 1 / 4
    p = 1

    while current_error > desired_error:

        a_new = (a+b)/2
        b_new = math.sqrt(a*b)
        t_new = (t)-(p*((a_new - a)**2))
        p_new = (2*p)

        new_pi = (((a_new + b_new) ** 2) / (4 * t_new))

        a=a_new
        b=b_new
        t=t_new
        p=p_new

        current_error = abs(new_pi - math.pi)

        among = new_pi

    # for i in range (1,totalz):
    #
    #     a.append(((a[i-1])+(b[i-1]))/2)
    #     b.append(math.sqrt(a[i-1]*b[i-1]))
    #     t.append(t[i-1]-(p[i-1]*((a[i-1]-a[i])**2)))
    #     p.append(2*p[i-1])
    #     pp.append(((a[i]+b[i])**2)/(4*t[i]))
    #     final = pp[-1]
    #     current_error = abs(final - math.pi)


    ### YOUR CODE HERE ###
    return new_pi


desired_error = 1E-15



approximation = my_pi(desired_error)

print("Solution returned PI=", approximation)

error = abs(math.pi - approximation)

if error < abs(desired_error):
    print("Solution is acceptable")
else:
    print("Solution is not acceptable")
