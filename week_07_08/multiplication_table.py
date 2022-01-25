'''
Week 8 Team Activity Multiplication Table
Asks to user for a number and prints the multiplication table with factors up
to that number
Nov 5 2020
'''
row_column = int(input("How many rows and columns do you want?"))

for y in range(1, row_column + 1):
    for x in range(1, row_column + 1):
        print(f"{x * y:3}", end=" ")
    print()
