'''
QY
November 3 2020
PBB

Week 08 Checkpoint
Focus: Loops
'''

your_num = int(input("What is your favorite number? "))

added_num = 0

for the_num in range(0, your_num + 1):
    added_num += the_num
print(added_num)
