# Author: mrp4sten

welcome = "Welcome to Realist Game"
print("\n" + "=" * len(welcome) + "\n" + welcome + "\n" + "=" * len(welcome))

print("You wake up from a large sleep in a forest")
question = input("What do you do? \n"
                 "a) Drink Water \n"
                 "b) To pee \n"
                 "c) Sleep again \n"
                 "=>")

if question == "a":
    print("Not Water in any place!")
    question = input("What do you do? \n"
                     "a) Search water \n"
                     "b) Sleep again \n"
                     "c) Walk in the forest \n"
                     "=>")
    if question == "a":
        print("There isn't any water")
        question = input("What do you do? \n"
                         "a) Search water \n"
                         "b) Sleep \n "
                         "=>")

        if question == "a":
            print("There isn't any water, you are dead")

        elif question == "b":
            print("Oh no a bear already found his food \n"
                  "Exactly You are the Food \n"
                  "Game Over :(")

    elif question == "b":
        print("Oh no a bear already found his food \n"
              "Exactly You are the Food \n"
              "Game Over :(")

    elif question == "c":
        print("Your found a Village, you are safe :D")


elif question == "b":
    question = input("Good, now what do you do now? \n"
                     "a) Walk in the forest \n"
                     "b) Search food and water \n"
                     "c) Do it Exercise and made a weapon with stone and branches \n"
                     "=>")

    if question == "a":
        question = input("More forest \n"
                         "What do yo do? \n"
                         "a) Walk more \n "
                         "b) Make a Weapon \n"
                         "=>")
        if question == "a":
            print("Your found a Village, you are safe :D")
        elif question == "b":
            print("You make a Weapon and Kill a Bear, Now you have Food and some Water from a river \n"
                  "You wake up, is only a bad dream, Sleep \n"
                  "Game Over :D")

    elif question == "b":
        question = input("More forest, but you found food and water from a river \n"
                         "What do yo do? \n"
                         "a) Drink water and eat \n "
                         "b) Sleep again because you are exhausted \n"
                         "=>")
        if question == "a":
            print("Oh no, the food  is poisoned and the water was contaminated \n"
                  "You are dead! \n"
                  "Game Over \n")

        elif question == "b":
            print("Congratulations! that's only a dream you are in your Bed!! "
                  "Sweat Dreams!\n")

    elif question == "c":
        print("You make a Weapon and Kill a Bear, Now you have Food and some Water from a river \n"
              "You wake up, is only a bad dream, Sleep \n"
              "Game Over :D")

elif question == "c":
    print("Congratulations! that's only a dream you are in your Bed!! "
          "Sweat Dreams!\n")

else:
    print("Oh no a bear already found his food \n"
          "Exactly You are the Food \n"
          "Game Over :(")
