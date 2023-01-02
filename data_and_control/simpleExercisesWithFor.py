import string

user_text = str(input("\n Enter a text \n"
                      "=> "))

# counter
spaces = 0
points = 0
commas = 0

for letter in user_text:
    if letter == " ":
        spaces += 1
    elif letter == ".":
        points += 1
    elif letter == ",":
        commas += 1

print("Number of spaces: {} \n"
      "Numbers of points: {} \n"
      "Number of commas: {} ".format(spaces, points, commas))

new_user_text = str(input("\n Enter a new text for count Uppercase letters \n"
                          "=> "))
# Counters
uppercase_letter = 0

for letter in new_user_text:
    if letter in string.ascii_uppercase:
        print("A uppercase letter founded {}".format(letter))
        uppercase_letter += 1

print("The number of uppercase letters in your text are {}".format(uppercase_letter))


number_of_user = int(input("Enter a number to show its multiplication table "
                           "=> "))

print("\n===Multiplication table===\n")
for number in range(1, 11):
    print(" {} x {} = {}".format(str(number),
                                 str(number_of_user),
                                 str(number_of_user * number)))
