import math

def given_function(x):
    return math.cos(x) - (5 * x) + 2

def regularFalsi(x0, x1, e):
    i = 0
    condition = True
    print('n   |   x0        |   f(x0)     |   x1        |   f(x1)      |   x2        |   f(x2)')
    print('-------------------------------------------------------------------------------------')
    while i<8:
        x2 = ((x0 * (given_function(x1))) - (x1 * (given_function(x0))) / (given_function(x1) - given_function(x0)))
        print(i,'  |   %0.4f   '%x0,'|   %0.4f   '%given_function(x0),'|   %0.4f   '%x1,'|   %0.4f   '%given_function(x1),'|   %0.4f   '%x2,'|   %0.4f'%given_function(x2))

        if given_function(x0) * given_function(x2) < 0:
            x1 = x2
        else:
            x0 = x2
        i = i + 1

    print('\n')
    print('Approximate root is: %0.8f' % x2)

x0 = 0.4
x1 = 0.6
e = 0.0001
regularFalsi(x0, x1, e)

