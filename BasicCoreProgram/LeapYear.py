'''

@Author: Hitesh Patil


@Date: 31-12-2021 10:00:56


@Last Modified by: Hitesh Patil


@Last Modified time: 31-12-2021 17:00:00


@Title : Leap Year

'''

print("Program For Checking Leap Year\n")

year = int(input("Enter Four Digit Year: "))

if 9999>=year>999: 
   
   if ( year % 400 == 0 or year % 4 == 0 and year % 100 != 0):
      
      print("\nEntered Year is Leap Year: ",int(year))
   
   else:
      print("\nEntered Year is not Leap Year: ",int(year))

else: 
 print("\nYear Should be with Positive Four Digit")

exit