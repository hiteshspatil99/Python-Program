'''

@Author: Hitesh Patil


@Date: 31-12-2021 10:00:56


@Last Modified by: Hitesh Patil


@Last Modified time: 01-01-2022 11:00:00


@Title : Computes the prime factorization of N using brute force.

'''

num=int(input("Enter Integer Value: "))

i=2
Number=num
while Number >1:
    if Number % i == 0:       # checking 1st input/2 if false then it will increament by 1
        print(i,end=" \n")    # when if bolck satisfied printing 1st factor
        Number=int(Number/i)  # then Number value will change with qoisent value & will start if bolck again 
    else:
        i=i+1 
