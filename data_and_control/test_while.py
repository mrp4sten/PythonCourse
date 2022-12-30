number = 0
while number < 10:
    number = int(input("Enter a number greater than 10 =>"))

answer = None
while answer != "b":
    answer = input("What's the definition about a Loop in programming? \n"
                   "a) A decision-making statement that allows code tobe executed only when a condition is true \n"
                   "b) A control flow statement that allows code to be executed repeatedly based on a condition \n"
                   "c) A collection of keys values  used to store data values like a map \n"
                   "=> ")

    if answer == "a" or answer == "c":
        print("Sorry study more about the loops :( \n")
    elif answer == "b":
        print("That's correct now you know the concept of loops! :D")
    else:
        print("Answer not supported, try again! \n")


