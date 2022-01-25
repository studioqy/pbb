'''
Week 12 Checkpoint Youngest Person
Uses a list of names and ages to determine who is the youngest
Dec 1 2020
'''

people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]

print(people)
youngest_age = 999
youngest_name = "idk"
for person in people:
    da_people = person.split(" ")
    person_name = da_people[0]
    person_age = int(da_people[1])
    if person_age < youngest_age:
        youngest_age = person_age
        youngest_name = person_name
    print(f"Name: {person_name} Age: {person_age}")
print(f"Youngest: {youngest_name} {youngest_age}")
