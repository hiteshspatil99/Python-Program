'''
@Author: Hitesh Patil

@Date: 04-01-2022 11:00:56

@Last Modified by: Hitesh Patil

@Last Modified time: 04-01-2022 13:00:00

@Title : Quadratic Equation roots

'''
import math as m

a = float(input("Enter the coeficient of a: "))
b = float(input("Enter the coeficient of b: "))
c = float(input("Enter the coeficient of c: "))
delta = b * b - 4 * a * c
if delta>0:
        root1 = (-b + m.sqrt(delta)) / (2 * a)
        root2 = (-b - m.sqrt(delta)) / (2 * a)                          # Using Math.power function getting roots both roots
        print("Two Roots are real and unequal: ", root1, "and" , root2) 
elif delta==0:
        root1=root2 = -b/(2*a)
        print("Roots are real and same: ", root1)
else:
        real=-b/(2*a)
        imaginary= m.sqrt(-delta)/(2*a)                                  # Taking separate inmaiginary & real terms  by math.power function
        print("First Imginary roots", " root1 = ", real, " + ", imaginary, " i")
        print("Second Imginary roots"," root2 = ", real, " - ", imaginary, " i")


exit
