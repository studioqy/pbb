current_age = int(input('How old are you? '))
next_age = current_age + 1
print(f'On your next birthday, you will be {next_age}\n')
egg_cartons = int(input('How many egg cartons do you have? '))
eggs = egg_cartons*12
print(f'You have {eggs} eggs\n')
cookies = int(input('How many cookies do you have? '))
people = int(input('How many people are there? '))
cookies_per_person = cookies/people
print(f'Each person may have {cookies_per_person} cookies')