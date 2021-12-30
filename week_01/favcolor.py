'''
Week 1 Favorite Color
Takes user's favorite color, prints it, and prints the compliment if it's one of the
six main colors on the color wheel
'''

color = input('Please type your favorite color: ')
print('Your favorite color is ' + color + '.')

if color == 'red' or color == 'Red':
    comp = 'green'
    print('The compliment of ' + color + ' is ' + comp + '.')
elif color == 'orange' or color == 'Orange':
    comp = 'blue'
    print('The compliment of ' + color + ' is ' + comp + '.')
elif color == 'yellow' or color == 'Yellow':
    comp = 'purple'
    print('The compliment of ' + color + ' is ' + comp + '.')
elif color == 'green' or color == 'Green':
    comp = 'red'
    print('The compliment of ' + color + ' is ' + comp + '.')
elif color == 'blue' or color == 'Blue':
    comp = 'orange'
    print('The compliment of ' + color + ' is ' + comp + '.')
elif color == 'purple' or color == 'Purple':
    comp = 'yellow'
    print('The compliment of ' + color + ' is ' + comp + '.')
else:
    print(color + ' is an unusual color!')
