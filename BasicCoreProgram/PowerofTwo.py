'''

@Author: Hitesh Patil


@Date: 31-12-2021 10:00:56


@Last Modified by: Hitesh Patil


@Last Modified time: 01-01-2022 11:00:00


@Title : Power of Two

'''

print("Program For Getting Power of Two\n")

num=int(input("Enter Power Value: "))
i=0

if 31>num>=0:

 for i in range(num):
    print("2 raised to the power ", i, " is ", 2 ** i)

else:
        print ("Number Entered not a power of Two ")
