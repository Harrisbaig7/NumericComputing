import math

def given_function(x):
    return (2*x)- math.cos(x)- 3

def g(x):
    return (math.cos(x) +3) / 2

def Fixed_Point_Iteration(x0, e):
    i = 1
    condition = True
    print('n   |   xn')
    while condition and i<11:
        x1 = g(x0)
        print(i, '  |   %0.4f'%x1)
        x0 = x1

        i = i + 1

        condition = abs(given_function(x1)) > e

    print('\nRequired root is: %0.3f' % x1)

x0 = math.pi/2
e = 0.00001

Fixed_Point_Iteration(x0, e)
