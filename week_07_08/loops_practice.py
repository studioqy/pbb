colors = ["red", "blue", "green", "yellow"]

for color in colors:
    print(color)

for numbers in range(1, 9):
    print(numbers)

answer = "no"
while answer.lower() != "yes":
    answer = input("May I have a piece of candy? ")
print("Thank you.")