'''

@Author: Hitesh Patil


@Date: 28-12-2021 10:00:56


@Last Modified by: Hitesh Patil


@Last Modified time: 29-12-2021 17:00:00


@Title : User Input and Replace String Template “Hello <<UserName>>, How are you?”

'''


print ("Program For Replacing String User input with Template")

name = input("\nEnter Your Name: ")

if len(name)>=3:
    print ("\nHello",name ,end='\n' "How are you?")
else:
    print("Enter minimum Three Characters as Input  ")


