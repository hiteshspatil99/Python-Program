'''
@Author: Hitesh Patil

@Date: 29-12-2021 10:00:56

@Last Modified by: Hitesh Patil

@Last Modified time: 30-12-2021 17:00:00

@Title : Flip Coin and print percentage of Heads and Tails

'''

print ("Program For Flip coin & get Percentage of Heads & tail")

import random
tail,head = 0,0
count = int(input("\n Enter Number of times to Flip Coin: "))
tailpercentage, headpercentage = 0,0

if count>0:
    for flip in range (count):
        flip = random.random()

        if flip<0.5:
            print("Tail")
            tail =tail + 1
            
        

        else:
            print("Head")
            head = head + 1

    tailpercentage = int(tail/count * 100)
    headpercentage = int(head/count * 100)
            
    print ("Tails Percentage is:", tailpercentage ,"%" " and" " Head Percentage is:", headpercentage , "%")

else:
    print ("Ensure Entered positive & Integer Value ")
    
exit