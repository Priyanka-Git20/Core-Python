'''
@Author : Priyanka
@Date : 2022-04-05  12:00:00
@Last Modified by : Priyanka
@Last Modified Time : 2022-04-05  20:20:00
@Title : Replace String Template  .
'''

def replaceString ():
    """
       Description:
           Function is used to replace the string
       Parameter:
           None
       Return:
           Returning nothing but print the message.
    """

    oldTemplete = "Hello name How are you!"
    print("Enter the user name")
    userName = input()

    if len(userName) < 3:
         print("Please enter the string with more three characters.")
    else:
         newTemplete = oldTemplete.replace("name",userName)
         print(newTemplete)

replaceString()
