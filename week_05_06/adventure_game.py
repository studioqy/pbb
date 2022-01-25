'''
Week 05-06 Assignment Adventure Game
A text game users can play with 9 endings!
October 24 2020
'''

'''
Extra:
Aside from the if/else statements, I also added a while loop and series of if/else
statements so that after reaching an ending, the user could continue the game
by starting back at any choice they had previous made. Also, there is a while
loop displaying an error at every place the user can give input, so if the
enter something other than the listed options, it will simply ask them to
enter one of the listed options.
'''

# Handy variables

skip_level = "00000"
# Used to determine what choice to skip to if the user decides to retry the
# game at a specific choice. By default, it's set to 00000 so that the game
# doesn't skip any choices

input_error = "Invalid input, please enter one of listed options."
# used as a shorthand for the error message that displays every time a user
# enters something other than the listed option

# Title and instructions for the user. Kept outside the while loop so it only
# displays the first time, not when users retry choices
print("The Ghost in the Forest")
print("\nInstructions:\n"
      "\nThe following is a Choose Your Own Adventure style game written and "
      "created by yours truly. After each story segment, there will be a "
      "question with two or more possible choices written in CAPS. Type one "
      "of the choices to select that option.\n")
player_ready = input("Are you ready? YES or NO\n")

# This while loop pops up every time the user can put in input. It prevents
# them from entering something other than the listed option. If they do, it
# sends the input error and allows them to enter another value.
while player_ready.lower() != "yes" and player_ready.lower() != "no":
    print(input_error)
    player_ready = input("")

if player_ready.lower() == "yes":
    # Main loop of the game that reruns if the user chooses to replay the game
    while True:

        # resets these values to nonsense phrases, so they aren't kept when
        # the user loops back
        invest_quiet = "nocontinue"
        leo_jack_together = "nocontinue"
        phone_flashlight = "nocontinue"
        school_forest = "nocontinue"
        leave_stay = "nocontinue"
        you_brian = "nocontinue"
        leave_look = "nocontinue"

        # where the skip_level variable is used to skip certain choices. This
        # statement reads the first charcter, and if it matches the key given
        # after the user selects a certain choice to restart from, then it
        # sets the correct value to invest_quiet and skips over the text
        if skip_level[0] == "q":
            invest_quiet = "QUIET"
        elif skip_level[0] == "i":
            invest_quiet = "INVESTIGATE"
        else:
            # Start of the story
            print("\nThere is a rumor spreading of a ghost that haunts the "
                  "forest behind your school. Your friends, Leo, Jack, and "
                  "Brian want to check out the woods that night and invite you "
                  "to come with them. You agree, certain it will be lots of "
                  "fun.\n"

                  "\nThat evening, as you are grabbing your things to leave, you "
                  "notice a flashlight on top of your kitchen cabinets. You were "
                  "planning to use the flashlight on your phone and you are "
                  "confident that your friends will too, but as your grandfather "
                  "would\'ve said, it never hurts to be too prepared. You grab "
                  "the flashlight and head outside.\n"

                  "\nYour friends are waiting for you just outside the woods. "
                  "They all use their phone\'s flashlights, and you switch on "
                  "the flashlight from your kitchen. The four of you meander "
                  "into the woods, chatting softly. After a few minutes, you "
                  "hear a loud \'crack\' past some trees.\n"

                  "\n\"What was that?\" Brian asks.\n")

            invest_quiet = input("Do you tell your friends to be QUIET or "
                                 "INVESTIGATE the sound?\n")

        # Another error loop for another place the user can input info.
        # I can't figure out how to get these loops under 80 characters
        # and still work right
        while invest_quiet.lower() != "quiet" and invest_quiet.lower() != "investigate":
            print(input_error)
            invest_quiet = input("")
        if invest_quiet.lower() == "quiet":
            # All places where input info is read is read with .lower() so the
            # code will still run with any capitalization

            # Text if the user chooses "quiet"
            print("\n\"Shhh!\" you tell your friends, listening intently "
                  "for any sound. deeper in the woods, you hear the faint "
                  "cracking of sticks and swishing of leaves. It could be "
                  "small animals and just forest noises, or it could be "
                  "something larger.\n"

                  "\nBefore you can make out what it is, you see a faint "
                  "light emanating from behind some trees. The figure of a "
                  "woman in a tattered gown appears, hovering just above the "
                  "forest floor. You and your friends turn your lights onto "
                  "it, but the ghost shrinks back and hides behind some of "
                  "the trees.\n"

                  "\n\"Hang on- it doesn\'t like the lights, turn them "
                  "off!\" you urge your friends. they all flip their "
                  "flashlights off or turn them to the ground, and you "
                  "slowly approach the ghost. It cautiously peers out from "
                  "behind the trees and approaches your group.\n"

                  "\nWhen it's only a dozen yards from you, the ghost leaps "
                  "out at you, shrieking and contorting into hideous "
                  "monster. You yell and scramble away, desperately trying "
                  "to turn your light back on. In your hesitation, the ghost "
                  "pounces on you, and you only wish that you had been a "
                  "little more careful.\n")

            # the key to what choices the user can skip back to after this
            # ending. Witch each choice, a string character is added. Each
            # charcter is later read after the story ends and the options
            # for choices to skip back to is displayed.
            end_key = "00000"
            print("THE END\n")
        elif invest_quiet.lower() == "investigate":
            end_key = "2"

            if skip_level[1] == "l":
                leo_jack_together = "leo"
            elif skip_level[1] == "j":
                leo_jack_together = "jack"
            elif skip_level[1] == "t":
                leo_jack_together = "together"
            else:
                # text if the user selects "investigate"
                print("\n\"Not sure,\" you reply. You shine your light near "
                      "the sound and step toward it cautiously. On one of "
                      "the trees is a deep claw mark etched into the wood.\n"

                      "\n\"Maybe we should leave,\" Leo says nervously. "
                      "\"There could be bears or other animals out here.\"\n"

                      "\n\"We\'ve already come this far,\" Jack says. \"I "
                      "want to see what all the fuss in school is about. I "
                      "can\'t imagine just some animals are causing those "
                      "stories, don\'t you guys want to see what this is "
                      "about?\"\n"

                      "\n\"Well, I'm heading back.\" Leo says.\n"

                      "\n\"Then I'm staying out here,\" Jack says, \"Are "
                      "you two with me?\" he asks, turning to you and "
                      "Brian.\n"

                      "\n\"Leave me out of this, I don't care what we do,\" "
                      "Brian says.\n")

                leo_jack_together = input("Do you go with LEO, go with JACK, "
                                          "or tell them both to chill out "
                                          "and stick TOGETHER?\n")

            # Another error loop. I'm fairly certain there's a simpler way
            # to do this, but I don't know what
            while leo_jack_together.lower() != "leo" and leo_jack_together.lower() != "jack" and leo_jack_together.lower() != "together":
                print(input_error)
                leo_jack_together = input("")

            if leo_jack_together.lower() == "leo":
                end_key = end_key + "1"

                if skip_level[2] == "p":
                    phone_flashlight = "phone"
                elif skip_level[2] == "f":
                    phone_flashlight = "flashlight"
                else:
                    # text if the user chooses to go with Leo
                    print("\n\"Leo’s right, it’s not worth risking our lives "
                          "for some dumb rumor,\" you tell you friends.\n"

                          "\n\"Whatever. Are you with me, Brian?\" Jack  "
                          "asks.\n"

                          "\n\"Sure, may as well.\" Brian replies. You and "
                          "Leo turn around and start trekking back to the "
                          "school. You wander around for several minutes "
                          "before realizing you are horribly lost.\n"

                          "\nAs you keep searching for the way out of the "
                          "forest, you see a light. \"Jack? Brian?\" you "
                          "call out. The light comes closer and the figure "
                          "of a woman in a tattered gown appears, glowing "
                          "brilliantly in front of you.\n"

                          "\n\"It's the ghost,\" you hear Leo whisper.\n"

                          "\nThe ghost slowly approaches you, and you shine "
                          "your light on it. Immediately it hisses, "
                          "shrinking back into the forest. You turn your "
                          "light to the ground and let it approach you.\n"

                          "\nLess than a dozen yards from you, the ghost "
                          "shrieks terribly, contorting visibly and rushes "
                          "toward you. You yell, grab Leo\'s arm and run.\n"

                          "\nAs you run, Leo\'s light begins flickering. The "
                          "light from the ghost catches up to you, and you "
                          "and Leo turn around. You shine light on it, and "
                          "it retracts. It begins advancing on Leo, and his "
                          "light goes out.\n"

                          "\n\"Battery\'s dead, help me out, dude!!\"\n")

                    phone_flashlight = input("Do you throw him your PHONE "
                                             "or toss him the FLASHLIGHT?\n")

                    # One more of those error loops
                while phone_flashlight.lower() != "phone" and phone_flashlight.lower() != "flashlight":
                    print(input_error)
                    phone_flashlight = input("")

                if phone_flashlight.lower() == "phone":
                    end_key = end_key + "10000"
                    # text if the user chooses "phone"
                    print("\nYou flip on the flashlight on your phone and "
                          "toss it to Leo. He fumbles it, and it falls to "
                          "the ground, its light going dim.\n"

                          "\n\"Grab the light, dude!\"\n"

                          "\n\"I can't find it, it landed face down!\" The "
                          "ghost rushes on top of him, and you know he is "
                          "gone. You stand, stunned, and run for your life. "
                          "You run circles in the forest, unable to find the "
                          "way out. As you stumble around, you accept that "
                          "there is no escape, and that the ghost will take "
                          "all of you. Without your phone, you cannot "
                          "contact anyone or even leave a final message. You "
                          "hear a shout of \"Help!\" further in the forest "
                          "and become convinced that the ghost has gotten "
                          "Jack and Brian too. You curl up on the forest "
                          "ground, losing all hope of escaping and wait for "
                          "the ghost to take you.\n")

                    print("THE END\n")
                elif phone_flashlight.lower() == "flashlight":

                    # Java has a shorthand, "+=2" that does this same thing
                    # but simpler, does that work in python too?
                    # So it'd be end_key += "2"
                    end_key = end_key + "2"

                    if skip_level[3] == "s":
                        school_forest = "school"
                    elif skip_level[3] == "f":
                        school_forest = "forest"
                    else:
                        # text if the user chooses "flashlight"
                        print("\nYou toss Leo your flashlight while pulling "
                              "out your phone and turning it on. Leo fumbles "
                              "the flashlight, but then picks it up and "
                              "shines it on the ghost. It backs away, "
                              "frightened, and you slowly circle around it "
                              "until you\'re standing next to Leo. Grabbing "
                              "his arm, you pull him back, whip around and "
                              "sprint as fast as you possibly can.\n"

                              "\nSoon, you reach the edge of the forest. The "
                              "school is in sight. Suddenly, you hear a loud "
                              "cry of \"Help!\" back in the forest.\n"

                              "\n\"Jack and Brian are still in there!\" Leo "
                              "exclaims.\n")

                        school_forest = input("Do run to the SCHOOL to seek "
                                              "safety there or run back into "
                                              "the FOREST to help your "
                                              "friends?\n")
                        # Error loop
                    while school_forest.lower() != "school" and school_forest.lower() != "forest":
                        print(input_error)
                        school_forest = input("")
                    if school_forest.lower() == "school":
                        end_key = end_key + "10000"
                        # Text if the user chooses "school"
                        print("\n\"Come on, we should be safe by the "
                              "school,\" you tell Leo. You run to the back doors "
                              "and try to open them, but they are locked tight. "
                              "Turning around, you watch the ghost leave the woods "
                              "and chase after you. You try to run, but it quickly "
                              "envelops you, and that is the last thing you "
                              "remember.\n")

                        print("THE END\n")
                    elif school_forest.lower() == "forest":
                        end_key = end_key + "20000"
                        # Text if the user chooses "forest"
                        print("\n\"We can\'t leave them, let\'s go!\" you "
                              "say to Leo and dash back into the forest. The ghost "
                              "is nowhere to be seen. You call out your friends\' "
                              "names as you go, desperately hoping to hear a "
                              "reply.\n"

                              "\n\"Here! Over here!\" You hear Brian\'s voice and "
                              "immediately start running towards it. Before long, "
                              "you stumble into Brian and Jack. Jack is sitting on "
                              "the ground, struggling to get his leg out of a "
                              "small crevice in the ground.\n"

                              "\n\"There was this- this thing!\" Brian sputters.\n"

                              "\n\"It was the ghost,\" Jack says. \"Nearly had us, "
                              "too- it was trying to kill us!\" Jack relays how he "
                              "fell into a narrow hole in the ground, and the "
                              "ghost appeared as he was trying to get out. His and "
                              "Brian\'s lights succeeded in scaring the ghost off "
                              "before it got to them, but they were more than "
                              "frightened.\n"

                              "\nYou tell the others about your own encounter with "
                              "the ghost. \"We should get out of here,\" Leo says. "
                              "\"It's not worth it, being out here with that.\"\n"

                              "\nYou agree, and Jack manages to pulls his leg from "
                              "the hole and stand up. The four of you start "
                              "heading back to the school when you hear a low "
                              "hissing. Turning around, you see the ghost\'s light "
                              "among the trees.\n"

                              "\"It's her, run!\" you yell, urging your friends "
                              "forward and sprinting for your life. You can see "
                              "the edge of the forest through the trees.\n"

                              "\nThe four of you burst out of the forest and run "
                              "down to the school. Turning back to the woods, you "
                              "train your lights on the ghost, who is hovering at "
                              "the edge of the forest. Frightened, the four of you "
                              "decide to never enter the woods at night again and "
                              "head back home, never to go back again.\n")

                        print("THE END\n")

            elif leo_jack_together.lower() == "jack":
                end_key = end_key + "20000"
                # text is the user chooses to go with jack
                print("\n\"Come on, we may as well explore a little more.\" "
                      "you tell them.\n"

                      "\n\"What? It\'s pitch black and my phone\'s nearly "
                      "dead, I\'m not going back alone!\" Leo exclaims.\n"

                      "\n\"I\'ll go back with you, dude,\" Brian says, and "
                      "the two head back the way you came. Meanwhile, you "
                      "and Jack walk further into the woods, hearing nothing "
                      "but the soft crunch of sticks and leaves beneath your "
                      "feet. You peer into the woods when your phone buzzes "
                      "and your ringtone plays, startling both you and Jack. "
                      "It\'s Brian.\n"

                      "\n\"Hey, you guys out of the woods yet?\" you say.\n"

                      "\n\"It got him, you've got to run, she got Leo!\" "
                      "Brian yells, nearly hysterical. \"He disappeared "
                      "right before my eyes, sucked into that THING-\"\n"

                      "\n\"Whoa there, calm down, what\'re you talking "
                      "about?\" you respond.\n"

                      "\n\"It\'s the ghost, she found us, Leo\'s gone, his "
                      "phone died and she went for him, oh gosh just get out "
                      "of the forest!!\" You\'ve scarcely heard Brian so "
                      "upset.\n"

                      "\nJack shouts to your phone, \"You trying to scare "
                      "us? Stop messing with us, I said we were going to "
                      "explore some more, and that\'s what we\'re going to "
                      "do. Give it a rest, will ya?\"\n"

                      "\nBrian shouts even louder. \"No, you don\'t get it, "
                      "it\'s real! She\'ll kill you!!\"\n"

                      "\n\"Whatever- ah ow!\" Jack starts, but stumbles and "
                      "falls to his knees. \"My foot's stuck,\" he grumbles. "
                      "he shines his flashlight over his leg, his shoe "
                      "wedged tightly in a narrow crack in the ground.\n"

                      "\n\"I've got to go,\" you tell Brian and hang up. "
                      "kneeling over Jack, you try to get his foot out but "
                      "to no avail. It\'s wedged in tightly.\n"

                      "\nAs you struggle, a dull light emerges from within "
                      "the trees. \"Brian?\" you call out, but what steps "
                      "out is the glowing figure of a woman, seemingly "
                      "hovering in mid air. You shine your light on it, "
                      "shocked, but immediately turn it back to Jack, "
                      "forcing his foot out of the hole. He protests, but "
                      "stops as soon as he sees the woman.\n"

                      "\n\"Run!\" You yell, sprinting away from the ghost. "
                      "Jack whips around and shines his flashlight on the "
                      "figure. It recoils, hissing and spitting. Trusting "
                      "Jack to keep it busy, you start dialing Brian\'s "
                      "number. He doesn\'t pick up.\n"

                      "\nAs you run, you hear a faint ringtone. It\'s "
                      "Brian\'s ringtone. Jack picks up a phone from off "
                      "the forest floor, abandoned and displaying your own "
                      "name. You feel sick to your stomach.\n"

                      "\n\"Don\'t stop, I can see the school!\" Jack yells "
                      "at you. You dash out of the woods and run down to the "
                      "school before turning around. The ghost hovers at the "
                      "edge of the woods, keeping its distance from your "
                      "flashlights. You can barely comprehend what just "
                      "happened.\n"

                      "\nThe following day, Leo and Brian are mysteriously "
                      "absent from school.\n")

                print("THE END\n")
            elif leo_jack_together.lower() == "together":
                end_key = end_key + "3"

                if skip_level[2] == "l":
                    leave_stay = "leave"
                elif skip_level[2] == "s":
                    leave_stay = "stay"
                else:
                    # text if the user chooses to stick together
                    print("\n\"There's no way we're splitting up in a forest "
                          "at night, what are you guys thinking?\" you tell "
                          "your friends. \"Let's just stick together.\"\n"

                          "\n\"Alright,\" Leo agrees, \"But I still think we "
                          "should go back. In a group or not, we'd be no "
                          "match for bears.\"\n"

                          "\n\"Yeah, right,\" Jack says. \"This was going to "
                          "be fun, and you\'re scared already? Let\'s "
                          "stay.\"\n"

                          "\n\"Like I said, I don\'t care either way,\" "
                          "Brian admits. Leo and Jack turn to you. \n"

                          "\n\"Well? What do you think?\" Jack asks.\n")

                    leave_stay = input("Do you STAY and explore the forest "
                                       "or LEAVE and head back to the "
                                       "school?\n")

                # Good 'ol while error loop
                while leave_stay.lower() != "leave" and leave_stay.lower() != "stay":
                    print(input_error)
                    leave_stay = input("")

                if leave_stay.lower() == "leave":
                    end_key = end_key + "30000"
                    # Text if the user chooses to leave, the first time.
                    # Somehow I think bears are the least of Jack's problems
                    print("\n\"That claw mark was the real deal, I\'m not "
                          "putting my life at risk here just for some "
                          "rumor.\" you tell them, and Leo agrees. The four "
                          "of you head back to the school, with Jack "
                          "grumbling along the way.\n"

                          "\nThe following day at school, Jack avoids the "
                          "three of you and hangs out with some of his other "
                          "friends. You overhear that he is planning to go "
                          "back into the woods that night with his other "
                          "friends instead. Meanwhile, after doing some "
                          "research, Leo discovers known bears in the area "
                          "and warns Jack, but he doesn't care. You hope "
                          "Jack is safe from the bears when he goes out "
                          "again.\n")

                    print("THE END\n")
                elif leave_stay.lower() == "stay":
                    end_key = end_key + "4"

                    if skip_level[3] == "y":
                        you_brian = "you"
                    elif skip_level[3] == "b":
                        you_brian = "brian"
                    else:
                        # Text if you stay instead of leaving
                        print("\n\"Let\'s look around a little more,\" you "
                              "concede, and your friends agree with varying "
                              "levels of enthusiasm. After looking around "
                              "for a while, you see a faint light in the "
                              "woods. It approaches you and you see that "
                              "it\'s  the figure of a woman, glowing "
                              "brilliantly in the dark woods.\n"

                              "\n\"Ha! I knew there was something out "
                              "here!\" Jack exclaims. The ghost backs away, "
                              "frightened by the noise and the light.\n"

                              "\n\"Shh!\" you say back at him and stare in "
                              "awe at the magnificent being.\n"

                              "\nSuddenly it leaps at the four of you, "
                              "contorting into a vicious monster. You "
                              "scramble and push each other back, "
                              "desperately running away from the ghost. The "
                              "ghost chases after you, flying through the "
                              "woods with amazing speed. As you run, Leo\'s "
                              "light begins flickering and fades into the "
                              "darkness.\n"

                              "\n\"My battery's dead!\" Leo shouts, turning "
                              "to the three of you as you run. The ghost "
                              "turns towards Leo and flies after him.\n"

                              "\n\"I have a spare flashlight!\" you say, "
                              "whipping out your phone and turning its "
                              "light on.\n"

                              "\n\"I got him!\" Brian calls out, shining "
                              "his light over Leo. He is closer to Leo, but "
                              "carries just his phone\'s light.\n")

                        you_brian = input("Do YOU give Leo your flashlight, "
                                          "or do you let BRIAN cover him?\n")

                    # Error loop
                    while you_brian.lower() != "you" and you_brian.lower() != "brian":
                        print(input_error)
                        you_brian = input("\n")

                    if you_brian.lower() == "you":
                        end_key = end_key + "30000"
                        # Text if you give Leo your own flashlight ("you")
                        print("\n\"Let me get it!\" You veer towards Leo "
                              "with both your lights, shining one on the "
                              "ghost and on on Leo. \"Here, use thi-\"\n"

                              "\nThe ghost whips around your lights and "
                              "flies over you, hovering directly behind you. "
                              "Its low growl and the screams of your friends "
                              "are the last things you can remember "
                              "hearing.\n")

                        print("THE END\n")
                    elif you_brian.lower() == "brian":
                        end_key = end_key + "4"

                        if skip_level[4] == "e":
                            leave_look = "leave"
                        elif skip_level[4] == "o":
                            leave_look = "look"
                        else:
                            # Text if you let Brian take care of it
                            print("\nYou keep running, and Brian shines his "
                                  "light at the ghost over Leo. It shrieks and "
                                  "falls back, but you keep running. After a "
                                  "minute, you and your friends take a moment to "
                                  "catch your breath, and you hand Leo your "
                                  "flashlight. Jack is exhilarated after seeing "
                                  "the ghost and wants to go back and get another "
                                  "look, as well as a picture to prove to your "
                                  "classmates that you saw the ghost. Leo tells "
                                  "him he\'s crazy, but Jack insists.\n"

                                  "\n\"How are we going to say we saw the ghost "
                                  "without any proof?\" he says. \"I just want one "
                                  "picture.\"\n")
                            leave_look = input("Do you LEAVE the forest now "
                                               "while you still can, or go "
                                               "back for another LOOK at "
                                               "the ghost?\n")

                        # Error loop
                        while leave_look.lower() != "leave" and leave_look.lower() != "look":
                            print(input_error)
                            leave_look = input("")

                        if leave_look.lower() == "leave":
                            end_key = end_key + "10000"
                            # Text if you leave, the second time
                            print("\n\"No way, I'm out of here.\" you say, "
                                  "and your friends can\'t argue with that. "
                                  "The four of you start walking back, but "
                                  "before long, you see the familiar glow "
                                  "behind you and break into a run. The "
                                  "ghost chases you all the way to the edge "
                                  "of the forest, but you manage to make it "
                                  "and run down to the school. Once there, "
                                  "you look back and see the ghost hovering "
                                  "at the edge of the forest, not daring to "
                                  "come out. Jack quickly takes a picture.\n"

                                  "\nThe next day at school, you profess "
                                  "about how you faced the famed ghost in "
                                  "the woods. Jack is particularly proud, "
                                  "showing off his photo of the ghost.\n")

                            print("THE END\n")

                        elif leave_look.lower() == "look":
                            end_key = end_key + "20000"
                            # Text if you look around some more
                            print("\n\"Just one, and I'm not staying out "
                                  "here longer than necessary,\" you tell "
                                  "Jack. Since you\'re near the edge of the "
                                  "forest, Leo and Brian decide to head out "
                                  "of the forest, while you and Jack ease "
                                  "back in for another look. While searching "
                                  "for the glow of the ghost, Jack trips and "
                                  "falls to his knees.\n"

                                  "\n\"Ow!\" he complains. \"My foot\'s "
                                  "stuck.\" he grumbles, leaning over to try "
                                  "and pull himself out. You kneel next to "
                                  "him and see that his shoe is wedged in a "
                                  "narrow crevice in the ground. He tries to "
                                  "pull his foot out, but it\'s wedged in "
                                  "tightly.\n"

                                  "\nAs you're struggling, you see the faint "
                                  "light within the woods. You urge Jack to "
                                  "get his foot out faster, but he starts "
                                  "pulling out the camera on his phone.\n"

                                  "\n\"Cover me!\" he says. The ghost is no "
                                  "more than a dozen yards away from you "
                                  "when you shine your light on it, but you "
                                  "fumble your phone and drop it. It falls "
                                  "deep into the crack Jack's foot it stuck "
                                  "in, taking its comforting light along "
                                  "with it.\n"

                                  "\nYou see one last camera flash from "
                                  "Jack\'s phone before you hear the ghost "
                                  "shriek and envelop the two of you.\n")
                            print("THE END\n")

        # After any ending, this asks the play if they want to keep playing.
        # If they don't, the program ends.
        keep_playing = input("Keep playing? YES or NO\n")

        # Yet another error loop
        while keep_playing.lower() != "yes" and keep_playing.lower() != "no":
            print(input_error)
            keep_playing = input("")

        # Calculates which choices the user can skip back to and which they
        # cannot based on the end_key. If the end_key states the user should
        # not be allowed to access a certain choice, it is marked as invalid,
        # and if the user tries to enter it, it will not work.
        if keep_playing.lower() == "yes":

            quiet_key = "qi"
            print("\nWhere would you like to start? Enter the "
                  "cooresponding two or three letter key to jump to an "
                  "option\n")

            print("QI: Do you tell your friends to be quiet or investigate "
                  "the sound?")
            if end_key[0] == "0":
                leo_jack_together_key = "invalid"
            elif end_key[0] == "1":
                print("LJT: Do you go with Leo, go with Jack, or tell both "
                      "chill out and stick together?")
                leo_jack_together_key = "ljt"
            elif end_key[0] == "2":
                leo_jack_together_key = "ljt"
                print("LJT: Do you go with Leo, go with Jack, or tell both "
                      "chill out and stick together?")

            if end_key[1] == "0":
                phone_flashlight_key = "invalid"
                leave_stay_key = "invalid"
            elif end_key[1] == "1":
                phone_flashlight_key = "pf"
                print("PF: Do you throw him the phone or toss him the "
                      "flashlight?")
                leave_stay_key = "invalid"
            elif end_key[1] == "2":
                phone_flashlight_key = "invalid"
                leave_stay_key = "invalid"
            elif end_key[1] == "3":
                phone_flashlight_key = "invalid"
                leave_stay_key = "sl"
                print("SL: Do you stay and explore the forest or leave and "
                      "head back to the school?")

            if end_key[2] == "0":
                school_forest_key = "invalid"
                you_brian_key = "invalid"
            elif end_key[2] == "2":
                school_forest_key = "sf"
                print("SF: Do run to the school to seek safety there or run "
                      "back into the forest to help your friends?")
                you_brian_key = "invalid"
            elif end_key[2] == "1":
                school_forest_key = "invalid"
                you_brian_key = "invalid"
            elif end_key[2] == "3":
                school_forest_key = "invalid"
                you_brian_key = "invalid"
            elif end_key[2] == "4":
                school_forest_key = "invalid"
                you_brian_key = "yb"
                print("YB: Do you give Leo your flashlight, or do you let "
                      "Brian cover him?")

            if end_key[3] == "0":
                leave_look_key = "invalid"
            elif end_key[3] == "1":
                leave_look_key = "invalid"
            elif end_key[3] == "2":
                leave_look_key = "invalid"
            elif end_key[3] == "3":
                leave_look_key = "invalid"
            elif end_key[3] == "4":
                leave_look_key = "ll"
                print("LL: Do you leave the forest now while you still can, "
                      "or go back from another look at the ghost?")

            end_input = input("")
            # Another while loop error, this time, if the user enters
            # "invalid", it trips the error as well so that the user
            # cannot use the key word "invalid" to go back to any choices
            # they should not be able to.
            while end_input.lower() == "invalid" or (end_input.lower() != leave_look_key and end_input.lower() != you_brian_key and end_input.lower() != leave_stay_key and end_input.lower() != school_forest_key and end_input.lower() != phone_flashlight_key and end_input.lower() != leo_jack_together_key and end_input.lower() != quiet_key):
                print(input_error)
                end_input = input("")
            # Calculates the skip_level value based on they key the user
            # enters, so they skip back to the correct choice
            if end_input.lower() == school_forest_key:
                skip_level = "ilf00"
            elif end_input.lower() == phone_flashlight_key:
                skip_level = "il000"
            elif end_input.lower() == leo_jack_together_key:
                skip_level = "i0000"
            elif end_input.lower() == quiet_key:
                skip_level = "00000"
            elif end_input.lower() == leave_look_key:
                skip_level = "itsb0"
            elif end_input.lower() == leave_stay_key:
                skip_level = "it000"
            elif end_input.lower() == you_brian_key:
                skip_level = "its00"

        # Printed if the user chooces to not keep playing and ends the program
        elif keep_playing.lower() == "no":
            print("\nGame successfully ended\n")
            break

# Printed if the user is not ready at the start, ending the program
elif player_ready.lower() == "no":
    print("\nGame successfully ended\n")
