__author__ = 'waf04'
import math


def simpleLinearRegressionForXY(x, y):

    """
    Simple function to calculate the actual linear regression formula for the data given
    Prints the b0 +b1x formula with the r (correlation) coefficient
    Returns the linear function ready for use
    :param x (list of x values):
    :param y (list of y values):
    :return linearFunction:
    """
    #get sums of squares
    sxy = multBeforeSum(x, y)-((sum(x)*sum(y))/len(x))
    sxx = squareBeforeSum(x)-((sum(x)*sum(x))/len(x))
    syy = squareBeforeSum(y)-((sum(y)*sum(y))/len(y))

    #calculate b1 (slope of line)
    b1 = sxy/sxx

    #calculate b0 (y int)
    xBar = sum(x)/len(x)
    yBar = sum(y)/len(y)
    b0 = yBar - (b1*xBar)

    #correlation
    r = sxy/(math.sqrt(sxx)*math.sqrt(syy))

    print('Linear regression equation = ' + str(b0) + ' + ' + str(b1) + '(x)')
    print('R factor (correlation) = ' + str(r))

    #make the function out of the coefficients
    def linearFunction(xVal):
        return b0 + (b1*xVal)

    #return the function
    return linearFunction


def multBeforeSum(x, y):

    total = 0
    for xv, yv in zip(x, y):
        total += xv*yv

    return total


def squareBeforeSum(x):

    total = 0
    for xv in x:
        total += xv*xv

    return total