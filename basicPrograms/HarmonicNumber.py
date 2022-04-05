'''
@Author : Priyanka
@Date : 2022-04-05  17:30:00
@Last Modified by : Priyanka
@Last Modified Time : 2022-04-05  17:50:00
@Title : Comupte the harmonic value.
'''


def harmonicValue():
    """
        Description:
            Prints the harmonic sum
        Parameter:
             none
        Return:
            Return the sum of nth harmonic number
    """
    print("Enter the harmonic value")
    harmonicValue = int(input())
    harmonicSum = 0

    for i in range(1,harmonicValue+1):
        if (harmonicValue != 0):
            harmonicSum += 1/i
    return harmonicSum


print(harmonicValue())

