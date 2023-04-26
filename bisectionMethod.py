import math

def given_function(x):
    return math.pow(x, 4)+ (3*(math.pow(x, 3)))- (15*(math.pow(x, 2))) -(2*x) +9


def bisection_method(an, bn, e):
    i = 0
    condition = True
    print('n   |      an      |      bn      |      xn      |      f(xn)')
    while condition and i<10:
        xn = (an + bn) / 2

        print(i, '  |   %0.6f ' % an, ' |   %0.6f ' % bn, ' |   %0.6f ' % xn, ' |   %0.6f' % given_function(xn))

        if given_function(an) * given_function(xn) < 0:
            bn = xn
        else:
            an = xn

        i = i + 1
        condition = abs(given_function(xn)) > e

    print('\nRequired Root is : %0.6f' % xn)


an = 0.7
bn = 1
e = 0.000001

bisection_method(an, bn, e)
