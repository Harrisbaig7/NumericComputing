import math

def given_function(x):
    return math.pow(x, 4)+ (3*(math.pow(x, 3)))- (15*(math.pow(x, 2))) -(2*x) +9

def derivative(x):
    return (4*math.pow(x, 3))+ (9*math.pow(x, 2))- (30*x) -2

def NR(x0, e):
    i = 0
    condition = True
    print('n  |      x0      |      f(x0)      |      f`(x0))      |      xn')
    while condition and i<10:
        if derivative(x0) == 0.0:
            print('Divide by zero error!')
            break

        xn = x0 - given_function(x0) / derivative(x0)

        print(i, ' |  %0.6f' % x0, '   |   %0.6f ' % given_function(x0), '   |   %0.6f  ' % derivative(x0), '   |   %0.6f' % xn)
        x0 = xn
        i = i + 1

        condition = abs(given_function(xn)) > e

    print('\n')
    print('Approximate root is: %0.6f' % xn)

x0 = 0.7
e = 0.000001

NR(x0, e)
