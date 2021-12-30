rider_num = int(input("How many riders are there?"))
if rider_num == 1:
    solo_rider_height = int(input("What is the height of the rider in inches?"))
    if solo_rider_height <= 62:
        print("Rider cannot ride")
    else:
        solo_rider_age = int(input("What is the age of the rider?"))
        if solo_rider_age <= 18:
            print("Rider cannot ride")
        else:
            print("Rider can ride")
            
elif rider_num == 2:
    many_riders_age = int(input("What is the age of the oldest rider?"))
    if many_riders_age <= 18:
        if many_riders_age <= 17 and many_riders_age >= 12:
            golden_passport = input("Do any riders have a golden passport? (y/n)")
            if golden_passport == "y":
                many_riders_height = int(input("What is the height of the shortest rider in inches?"))
                if many_riders_height <= 36:
                    print("Riders cannot ride")
                else:
                    print("Riders can ride")
            else:
                youngest_rider = int(input("What is the age of the youngest rider?"))
                if youngest_rider >= 12:
                    if many_riders_age >= 16 and youngest_rider >= 14:
                        print("Riders can ride")
                    else:
                        shortest_rider = int(input("What is the height of the shortest rider in inches?"))
                        if shortest_rider >= 52:
                            print("Riders can ride")
                        else:
                            print("Riders cannot ride")
                else:
                        print("Riders cannot ride")
    else:
        many_riders_height = int(input("What is the height of the shortest rider in inches?"))
        if many_riders_height <= 36:
            print("Riders cannot ride")
        else:
            print("Riders can ride")