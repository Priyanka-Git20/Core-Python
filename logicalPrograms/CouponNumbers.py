'''
   @Author : Priyanka
   @Date : 2022-04-07  12:40:00
   @Last Modified by : Priyanka
   @Last Modified Time : 2022-04-08  12:30:00
   @Title : Generate distinct coupon number.
'''


import random


def generateCoupon():
    """
        Description:
            Repeatedly choose a random number and check whether it's a new one and print the code.
        Parameter:
            None
        Return:
            Returning nothing printing the coupon code.
    """

    lengthOfCoupon = int(input("Enter the length of the coupon less than 10 :\n"))
    list_int = random.sample(range(0,10),lengthOfCoupon)
    print("Coupon code is ",list_int)

generateCoupon()

