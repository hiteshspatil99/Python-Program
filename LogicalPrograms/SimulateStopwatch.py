'''
@Author: Hitesh Patil
@Date: 05-01-2022 18:05:46
@Last Modified by: Hitesh Patil
@Last Modified time: 05-01-2022 16:00:00
@Title : Simulate Stopwatch Program
'''
import time

while True:
    try:
        input("Press Enter to Continue, ctrl-c To exit ")
        start_time=time.time()
        print("Timer has Started")

    except KeyboardInterrupt:
        print("Timer has stopped")
        end_time=time.time()
        print("Time Elapsed: ", (end_time-start_time), "secs")
        break


import subprocess

while True: 
    start_Again = int(input("Do you want to play again? \n 1 Yes  \n 2 No \n "))
    if start_Again== 1:
        subprocess.run(["Python", "SimulateStopwatch.py"])
        break
    else:
        print("\n....Thank You.... & ...Revisit....")

    break