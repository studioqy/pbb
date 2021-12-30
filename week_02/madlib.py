'''
Thing
'''

print('Please enter the following: \n')

# Asks user for random words

first_adjective = input('Adjective: ')
first_animal = input('Animal: ')
first_verb = input('Present Tense Verb: ')
first_exclamation = input('Exclamation: ')
second_verb = input('Present Tense Verb: ')
third_verb = input('Present Tense Verb: ')

# Extra input I added

second_exclamation = input('Exclamation: ')
first_number = input('Positive Number: ')
first_plural_noun = input('Plural Noun: ')
first_name = input('Name:  ')
first_noun = input('Noun: ')
second_adjective = input('Adjective: ')
first_place = input('Place: ')

# In the mad lib, a number is asked for and displayed with a -st, -nd, -rd, or -th ending. The following code determines which ending the number should have.

if first_number == '11':
    number_end = 'th'
elif first_number == '12':
    number_end = 'th'
elif first_number == '13':
    number_end = 'th'
elif first_number[-1] == '1':
    number_end = 'st'
elif first_number[-1] == '2':
    number_end = 'nd'
elif first_number[-1] == '3':
    number_end = 'rd'
else:
    number_end = 'th'

# prints the MadLib

print('\nYour story is: \n')
print(
    f'The other day, I was really in trouble. It all started when I saw a very {first_adjective} {first_animal} {first_verb} down the hallway. "{first_exclamation}!\" I yelled. But all I could think to do was to {second_verb} over and over. Miraculously, that caused it to stop, but not before it tried to {third_verb} right in front of my family.')

# Extra output I added

print(f'\nMy family was not pleased.\"{second_exclamation}!\" they exclaimed, and said, \"This is the {first_number}{number_end} time this has happened! All of these {first_plural_noun} can\'t be good for {first_name}\'s {first_noun}, especially when they\'re {second_adjective}.\" And so I put the {first_animal} back in the {first_place} where hopefully it would never come and {first_verb} in front of my family again.')
