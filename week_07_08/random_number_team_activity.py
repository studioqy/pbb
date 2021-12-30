'''
Team 07-09
Week 8 Team Activity
Random Number Guessing Game
Focus: Loops
'''

import random
#While loop for the entire game- only ends if the user doesn't say yes to playing again
while True:

    #generates a random number between 1 and 100
    actual_num = random.randint(1, 100)
    #Tracks the number of guesses it takes for the user to guess the number
    tracker = 0

    guessed_num = int(input("\nGuess a number between 1 and 100: "))

    #Loops while the user's guess isn't the actual number
    while guessed_num != actual_num:
        if guessed_num < actual_num:
            print("Go higher!")
            guessed_num = int(input("\nGuess a number between 1 and 100: "))
        elif guessed_num > actual_num:
            print("Go lower!")
            guessed_num = int(input("\nGuess a number between 1 and 100: "))
        #Adds one to the tracker as long as the user didn't guess tha actual number
        tracker += 1
    #Plays if the guessed number is equal to the actual number
    print("\nYou got it!")
    print(f"The number was {actual_num}")
    print(f"You guessed the number after {tracker + 1} guesses\n")
    redo = input("Do you wish to play again? ")
    #If the user says yes, the original while loop loops again
    if redo.lower() == "yes":
        pass
    #If they say anything else, this breaks the while loop and ends the game
    else:
        print("Game successfully ended")
        break