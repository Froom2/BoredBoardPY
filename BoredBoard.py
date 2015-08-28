# Bored Board
# The program to solve your boredom issues!

import random

tasks = ["study Java.",
         "wash up.",
         "listen to a podcast.",
         "empty a box!",
         "read a book.",
         "learn some more Python.",
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
    3 - Remove an Activity
    4 - Change an activity
    5 - Get suggestions
    6 - Exit
    """)
    option = int(input("What would you like to do? "))
    return option


def printtasks():
    # Print tasks
    for i in tasks:
        print(i)


def suggest():
    # Runs suggestion loop
    print("You should", random.choice(tasks))
    answer = str.lower(input("Do you want to do that? (yes/no) "))

    while answer != "yes":
        print("You should", random.choice(tasks))
        answer = str.lower(input("Do you want to do that? (yes/no) "))
        if answer != "yes":
            print("you said ", answer, "...")
        if answer == "yes":
            break

    print("So now go do that!")

# Introduction
optionchoice = introduction()

# Option 1 - Print tasks, then return to introduction
if optionchoice == 1:
    printtasks()

# Option 2 - Add an activity, then return to introduction
elif optionchoice == 2:
    print("Function not added yet")

# Option 3 - Remove activity, then return to introduction
elif optionchoice == 3:
    print("Function not added yet")

# Option 4 - Change an activity, then return to introduction
elif optionchoice == 4:
    print("Function not added yet")

# Option 5 - Run suggestions, then exit
elif optionchoice == 5:
    suggest()

# Option 6 - Exit
elif optionchoice == 6:
    # TODO functionalise this then put at the end of the other things it needs to be in
    input("Press any key to confirm exit")

# Other - Print error then return to introduction
else:
    print("Sorry that isn't a valid choice.")

# TODO Enable changing/adding/removing things
