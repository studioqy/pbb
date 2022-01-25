'''
Week 8 Checkpoint Integer Sums
Asks the user for a number and computer the sum of all positive integers
up to that number
Nov 3 2020
'''

your_num = int(input("What is your favorite number? "))

added_num = 0

for the_num in range(0, your_num + 1):
    added_num += the_num
print(added_num)
