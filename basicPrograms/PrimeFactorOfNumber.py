'''
@Author : Priyanka
@Date : 2022-04-05  18:10:00
@Last Modified by : Priyanka
@Last Modified Time : 2022-04-05  18:30:00
@Title : Computes the prime factor of number.
'''

import math
def computePrimeFactor():
    """
       Description:
           Function is used to compute the prime factors of the number.
       Parameter:
           None
       Return:
           Returning nothing but print the message.
    """

    print("Enter the number for calculating the prime factor")
    number = int(input())
    while number % 2 == 0:
        print(2),
        number = number / 2

    for i in range(3, int(math.sqrt(number))+ 1 ,2):

        while (number % i == 0):
            print(i)
            number = number / i

    if number > 2:
        print(number)

computePrimeFactor()


