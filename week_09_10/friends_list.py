'''
Week 9 Checkpoint Friends List
Asks user to list the names of their friends and prints them. Stops when the
user types 'end'
Nov 10 2020
'''

friends_end = "notend"
your_friends = []

while friends_end.lower() != "end":
    friends_end = input("Name a friends or type \"end\": ")
    if friends_end.lower() != "end":
        your_friends.append(friends_end)

for friend_item in your_friends:
    print(friend_item.capitalize())
