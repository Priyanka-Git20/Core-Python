'''
   @Author : Priyanka
   @Date : 2022-04-06  17:40:00
   @Last Modified by : Priyanka
   @Last Modified Time : 2022-04-06  18:30:00
   @Title : Gambler Simulation.
'''


import random


def gamblerGame():
    """
        Description:
            Printing the number of Wins and Percentage of Win and Loss.
        Parameter:
            None
        Return:
            Returning nothing printing the percentage of win and loss.
    """

    AmountOfBet = 1
    wins = 0

    for i in range(numOfTimes):
        cashOfThePlayer = stake

        while (cashOfThePlayer > 0) and (cashOfThePlayer < goal):
            betCheck = random.randint(0,1)
            if betCheck == 1 :
                cashOfThePlayer += AmountOfBet
            else:
                cashOfThePlayer -= AmountOfBet

        if cashOfThePlayer == goal:
            wins += 1

    print("{} wins out of {} trials".format(wins,numOfTimes))
    winPercentage = (wins/numOfTimes)*100
    print("Percentage of Won Game Is: ", winPercentage)
    print("Percentage of Loss Game Is: ", 100 - winPercentage)

if __name__ == '__main__':
    stake = int(input("Enter Stake: "))
    goal = int(input("Enter Goal You Want Achieve: "))
    numOfTimes = int(input("Enter Number Of Times You Want To Try: "))
    gamblerGame()





