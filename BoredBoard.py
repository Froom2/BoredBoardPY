# Bored Board
# The program to solve your boredom issues!

import random

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

def introduction():
    # Introduction to the program
    print('Welcome to the Bored Board!')
    print("""
    1 - View activities
    2 - Add an activity
    3 - Remove and Activity
    4 - Change an activity
    5 - Get suggestions
    6 - Exit
    """)
    option = int(input("What would you like to do? "))
    return option

def printtasks():
    for i in tasks:
        print(i)

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

optionchoice = introduction()

if optionchoice == 1:
    printtasks()

elif optionchoice == 2:
    print("Function not added yet")

elif optionchoice == 3:
    print("Function not added yet")

elif optionchoice == 4:
    print("Function not added yet")

elif optionchoice == 5:
    suggest()

elif optionchoice == 6:
    input("Press any key to confirm exit")

else:
    print("Sorry that isn't a valid choice.")

# TODO Enable changing/adding/removing things



