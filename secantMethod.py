import math

def given_function(x):
    return (2*math.cosh(x) * math.sin(x))-1

def Secant_Method(x0, x1, e):
    i = 1
    condition = True
    print('n   |   x0        |   f(x0)     |   x1        |   f(x1)      |   x2        |   f(x2)')
    print('-------------------------------------------------------------------------------------')
    while condition:
        if given_function(x0) == given_function(x1):
            print('Divide by zero error!')
            break
            
        x2 = x0 - (x1 - x0) * given_function(x0) / (given_function(x1) - given_function(x0))

        print(i, '  |   %0.5f  ' % x0, '|   %0.5f  ' % given_function(x0), '|   %0.5f  ' % x1,'|   %0.5f  ' % given_function(x1),'|   %0.5f  ' % x2,'|%0.5f' % given_function(x2))
        # print('Iteration-%d, x2 = %0.6f and f(x2) = %0.6f' % (step, x2, given_function(x2)))
        x0 = x1
        x1 = x2

        i = i + 1

        condition = abs(given_function(x2)) > e

    print('\n')
    print('Approximate root is: %0.5f' % x2)

x0 = 0.4
x1 = 0.5
e = 0.0001

Secant_Method(x0, x1, e)
