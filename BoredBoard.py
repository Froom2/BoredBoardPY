# Bored Board
# The program to solve your boredom issues!

import random

def introduction():
    # Introduction to the program
    print('Welcome to the Bored Board!')
    print("""
    1 - Add an activity
    2 - Remove and Activity
    3 - Change an activity
    4 - Get suggestions
    5 - Exit
    """)
    option = int(input("What would you like to do? "))
    return option

def suggest():
    print("You should", random.choice(tasks))
    answer = str.lower(input("Do you want to do that?"))

    # TODO Insert yes/ no specifier and error check to catch.

    while answer != "yes":
        print("You should", random.choice(tasks))
        answer = str.lower(input("Do you want to do that?"))
        if answer == "yes":
            break

    print("So now go do that!")

tasks = ["study Java.",
         "wash up.",
         "listen to a podcast.",
         "empty a box!",
         "read a book.",
         "do your dailies on GuildWars.",
         "hoover.",
         "clean the bathtub and sink.",
         "clean the toilet.",
         "clean the kitchen surfaces.",
         "mop a floor.",
         "do some decorating.",
         "play guitar.",
         "Learn Python!"]

optionchoice = introduction()

if optionchoice == 4:
    suggest()

# TODO Enable changing/adding/removing things



