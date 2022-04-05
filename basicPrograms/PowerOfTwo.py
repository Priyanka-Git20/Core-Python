'''
@Author : Priyanka
@Date : 2022-04-05  14:00:00
@Last Modified by : Priyanka
@Last Modified Time : 2022-04-05  14:35:00
@Title : Computes the power of two.
'''

import math
import sys


def computePowerOfTwo():
    """
       Description:
           Function is used to compute the power of two.
       Parameter:
           None
       Return:
           Returning nothing but print the message.
    """

    exponent = int(sys. argv[1])

    if (exponent >= 0) and (exponent < 31):
            value = int(math.pow(2,exponent))
            print("Value of 2^{} is {}".format(exponent,value))
    else:
            print("Enter the exponent between 0 to 31")


computePowerOfTwo()
