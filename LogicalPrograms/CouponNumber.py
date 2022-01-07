'''
@Author: Hitesh Patil
@Date: 04-01-2022 18:05:46
@Last Modified by: Hitesh Patil
@Last Modified time: 05-01-2022 11:00:00
@Title : Coupon Numbers
'''


import random

num=int(input("Enter digit:  "))

def coupon(num):
    number="0123456789"
    code= " "
    for i in range(0,num):
        start=random.randint(0,9)
        print(start)                       

        code=code+number[start:start+1]  #code increment and sliceoperator
    return code       

print(coupon(num))