'''
@Author: Hitesh Patil

@Date: 04-01-2022 17:00:56

@Last Modified by: Hitesh Patil

@Last Modified time: 04-01-2022 20:00:00

@Title : 2D Array

'''

column=int(input("Enter Columns Count: "))
row=int(input("Enter Rows count: "))
matrix=[]                                                       ##
for i in range(row):
    h = []
    for j in range(column):
        elements=int(input("Enter one by one Matrix Elements: "))
        h.append(elements)                                       ## appending value to matrix & taking one by one element
    matrix.append(h)                                             

for i in range(row):                                             ##
    for j in range(column):
        print(matrix[i][j], end=" ")                             ##
    print()
exit
