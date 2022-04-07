'''
    @Author : Priyanka
    @Date : 2022-04-05  23:20:00
    @Last Modified by : Priyanka
    @Last Modified Time : 2022-04-05  23:30:00
    @Title : prints the Euclidean distance from the point (x, y) to the origin (0, 0).
'''

import math
import sys

x1 = 0
y1 = 0

x2 = int(sys. argv[1])
y2 = int(sys. argv[2])

distance = math.sqrt((math.pow(x2,x2)) +(math.pow(y2,y2)))
print("Distance from the point (x,y) to the origin is",distance)