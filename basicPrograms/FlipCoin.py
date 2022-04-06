'''
@Author : Priyanka
@Date : 2022-04-05  12:30:00
@Last Modified by : Priyanka
@Last Modified Time : 2022-04-05  12:45:00
@Title : Flip Coin and print percentage of Heads and Tails.
'''

import random


def flipPercentage():
    """
        Description:
            Calculate the percentage of heads and tails
        Parameter:
             none
        Return:
            Return the printing message
    """

    numberOfFlip = int(input("Enter the how many times want to flip the coin:\n"))
    tail = 0
    head = 0
    for i in range(1,numberOfFlip+1):
        flipCheck = random.uniform(0,1)
        if flipCheck < 0.5:
            tail += 1
        else:
            head += 1
    tailPercentage = (tail/numberOfFlip)*100
    print("Tail percentage is",tailPercentage)
    headPercentage = 100 - tailPercentage
    print("Head percentage is",headPercentage)


flipPercentage()