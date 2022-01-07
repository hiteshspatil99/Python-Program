'''
@Author: Hitesh Patil

@Date: 04-01-2022 19:00:56

@Last Modified by: Hitesh Patil

@Last Modified time: 04-01-2022 22:00:00

@Title : Sum of three Integer adds to ZERO(Triplet sum)

'''

import math as m

def triplets(a,arr_size, sum):
    for i in range(0, arr_size - 2):                                      #start from 0 to -2 size
        for j in range(i + 1, arr_size - 1):                              # start from 1 to -1 size
            for k in range(j + 1, arr_size):                              #start from 1 to 0 size
                if (a[i] + a[j] + a[k] == 0):                             # print whose sum = 0
                 print("Getting Triplets:- ", a[i],", ", a[j], ", ", a[k])
     

a = list(map(int,input().split()))         #array taking user input.. value should spilted by cess                   
arr_size = len(a)                                              # measure length of array
sum=0                                                          # sum req
triplets(a,arr_size, sum)

exit

##Refractor