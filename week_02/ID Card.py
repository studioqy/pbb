'''
Week 2 Checkpoint ID Card
Takes information from a user and prints it formated as an ID card
Sept 22 2020
'''

first_name = input('What is you first name? ')
last_name = input('What is your last name? ')
email = input('What is your email address? ')
phone_number = input('What is your phone number? ')
job_title = input('What is your job title? ')
id_number = input('What is your ID number? ')
hair_color = input('What is your hair color? ')
eye_color = input('What is your eye color? ')
month = input('What is the month you started? ')
training = input('Have you completed the training? ')

print('The ID Card is:')
print('---------------------------------------')
print(last_name.upper() + ', ' + first_name.capitalize())
print(job_title.title())
print('ID: ' + id_number)
print()
print(email.lower())
print(phone_number)
print()
print(f'Hair: {hair_color.capitalize():15} Eyes: {eye_color.capitalize()}')
print(f'Month: {month.capitalize():14} Training: {training.capitalize()}')
print('---------------------------------------')
