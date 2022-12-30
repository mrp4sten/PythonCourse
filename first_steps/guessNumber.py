import random

print("===Welcome to Guess number game===")

# the value is random between 1 and 10
winning_number = random.randint(1, 10)

input_number = int(input("Enter your number: "))

# This is some validations
if input_number < 1:
    print("Your number should be more than 1")
if input_number > 10:
    print("Your number should be less than 10")

if winning_number == input_number:
    print("You win!")
else:
    print("The winning number was: {}".format(winning_number))
