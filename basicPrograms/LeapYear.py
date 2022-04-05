'''
@Author : Priyanka
@Date : 2022-04-05  13:08:00
@Last Modified by : Priyanka
@Last Modified Time : 2022-04-05  13:40:00
@Title : Check the year is leap or not  .
'''

def checkLeapYear ():
    """
       Description:
           Function is used to check year is leap or not.
       Parameter:
           None
       Return:
           Returning nothing but print the message.
    """

    if (year % 400 == 0) and (year % 100 == 0):
        print("{} is leap year".format(year))
    elif (year % 4 == 0) and (year % 100 != 0):
        print("{} is leap year".format(year))
    else:
        print("{} is not a leap year".format(year))


print("Enter the year you want to check is it leap or not")
year = int(input())

if (year > 9999) or (year < 1000):
    print("Enter the year with 4 digit number")
else:
    checkLeapYear()


