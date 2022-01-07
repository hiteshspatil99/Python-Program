'''

@Author: Hitesh Patil


@Date: 01-01-2022 10:00:56


@Last Modified by: Hitesh Patil


@Last Modified time: 03-01-2022 17:00:00


@Title : Harmonic Number

'''

Num=int(input("Enter iteger value: "))
if Num>=0:
 def Harmonic_No(Num):
    if Num<2:
        return 1
    else:
        return 1/Num + Harmonic_No(Num-1)
 print(Harmonic_No(Num))
else:
    print("Number should Positive integer & Not be Equal to Zero ")
exit
