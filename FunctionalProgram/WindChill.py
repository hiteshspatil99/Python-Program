'''
@Author: Hitesh Patil

@Date: 04-01-2022 13:00:56

@Last Modified by: Hitesh Patil

@Last Modified time: 04-01-2022 17:00:00

@Title : WindChill

'''
import sys

t = float(sys.argv[1])
v = float(sys.argv[2])


if t<50 or 120>v>3:

            w = 35.74 + 0.6215 * t + (0.4275 * t - 35.75) * (v ** 0.16)
            print("\n Effective Temperature Windchill to be: ", w)
else:
    print("\n Please Enter Temperature Value < 50 F Wind Speed in betn 3-120 miles/hrs\n")


## by function