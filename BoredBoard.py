# Bored Board
# The program to solve your boredom issues!

import random

# Tasks now stored in separate text file.
# tasks = ["study Java.",
#         "wash up.",
#         "listen to a podcast.",
#         "empty a box!",
#         "read a book.",
#         "learn some more Python.",
#         "hoover.",
#         "clean the bathtub and sink.",
#         "clean the toilet.",
#         "clean the kitchen surfaces.",
#         "mop a floor.",
#         "do some decorating.",
#         "play guitar.",
#         "Learn Python!"]

# Open the text file containing the tasks
text_file = open("tasks.txt", "r")
# Read the tasks into a list
tasks = text_file.readlines()

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
    answer = "no"

    # Make suggestions until input is 'yes'
    while answer != "yes":
        # Suggest a random task from the list
        print("You should", random.choice(tasks))
        # prompt for input if person wants to do that task
        answer = str.lower(input("Do you want to do that? (yes/no) "))
        # If no, mirror response and continue loop
        if answer != "yes":
            print("you said ", answer, "...")
        # If yes, break loop
        if answer == "yes":
            print("So now go do that!")
            break

# Run introduction
optionchoice = introduction()

while optionchoice:

    # Option 1 - Print tasks, then return to introduction
    if optionchoice == 1:
        printtasks()

    # Option 2 - Add an activity, then return to introduction
    elif optionchoice == 2:
        print("Function not added yet")
        input("Press any key to return to the menu.")

    # Option 3 - Remove activity, then return to introduction
    elif optionchoice == 3:
        print("Function not added yet")
        input("Press any key to return to the menu.")

    # Option 4 - Change an activity, then return to introduction
    elif optionchoice == 4:
        print("Function not added yet")
        input("Press any key to return to the menu.")

    # Option 5 - Run suggestions, then exit
    elif optionchoice == 5:
        suggest()
        break

    # Option 6 - Exit
    elif optionchoice == 6:
        input("Press any key to confirm exit")
        break

    # Other - Print error then return to introduction
    else:
        # TODO catch characters!
        print("Sorry that isn't a valid choice.")
        input("Press any key to return to the menu.")

    optionchoice = introduction()

# Close the text file.
text_file.close()
