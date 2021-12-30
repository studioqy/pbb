#Week 9 Checkpoint

friends_end = "notend"
your_friends = []

while friends_end.lower() != "end":
    friends_end = input("Name a friends or type \"end\": ")
    if friends_end.lower() != "end":
        your_friends.append(friends_end)

for friend_item in your_friends:
    print(friend_item.capitalize())