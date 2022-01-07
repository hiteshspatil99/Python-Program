'''
@Author: Hitesh Patil
@Date: 04-01-2022 15:05:46
@Last Modified by: Hitesh Patil
@Last Modified time: 04-01-2022 23:00:00
@Title : Gambler
'''

import random

stake = int(input("Enter amount for Invest: "))
times = int(input("Enter Count for Play: "))
setgoal = int(input("Set a Goal point: "))

bet = 1
win =loss=temp=0

for t in range(1,times+1):
    if (random.random() >= 0.5):  
                win = win + 1
                stake = stake + bet
                if (stake == setgoal):
                    break
    else:  
                loss = loss + 1
                stake = stake - bet
                if (stake == 0):
                    break
    
    if (t <= times and stake == setgoal):  
        print("Got the Goal")          
        

    elif (t == times and stake != setgoal):  
        print("Times ,Unable to reach the Goal")

    else:                                   # if stake is zero then loop breaks
        break

winpercentage = win * 100 / t
losspercentage = loss * 100 / t

print("Win Count:", win)

print("Win percentage:", winpercentage)  # prints winning percentage

print("Loss Count:", loss)

print("Loss Percentage:", losspercentage)