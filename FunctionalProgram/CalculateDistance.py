'''
@Author: Hitesh Patil

@Date: 03-01-2022 18:05:46

@Last Modified by: Hitesh Patil

@Last Modified time: 04-01-2022 11:00:00

@Title : Distance Calculating Using Math.power Function

'''

import math as m
import sys

x = int(sys.argv[1])   
y = int(sys.argv[2])

print(sys.argv)                    #printing argv on Command line

distance = m.sqrt(x * x + y * y)   # using Math>sqrt Formulae Doing Calculation 

print("\nDistance Between Two Point Is: ",distance)     #o/p