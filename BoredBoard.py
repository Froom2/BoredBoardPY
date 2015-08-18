import random

print('Welcome to the Bored Board!')

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

print("You should", random.choice(tasks))
answer = str.lower(input("Do you want to do that?"))

while answer != "yes":
    print("You should", random.choice(tasks))
    answer = str.lower(input("Do you want to do that?"))
    if answer == "yes":
        break

print("So now go do that!")

