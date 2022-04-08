'''
   @Author : Priyanka
   @Date : 2022-04-07  17:00:00
   @Last Modified by : Priyanka
   @Last Modified Time : 2022-04-07  17:30:00
   @Title : Calculate elapses time between start time and stop time of the timer.
'''


import time
import datetime


def elapsedTimeCalculation():
    """
        Description:
            Measuring the time that elapses between the start and end click
        Parameter:
            None
        Return:
            Returning nothing printing elasped time
    """
    start = input("Press Enter to start ")
    print("Timer has started")
    startTime = time.time()
    stop = input("Press Enter to stop ")
    print("Timer has stoped")
    endTime = time.time()
    elaspedTime = str(datetime.timedelta(seconds = endTime -startTime))
    print("Elasped time is ",elaspedTime)

elapsedTimeCalculation()