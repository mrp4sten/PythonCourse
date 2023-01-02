list_of_numbers = []
add_numbers = True

while add_numbers:
    number = int(input("Enter a number for your list \n"
                       "without points, only integer numbers \n"
                       "=> "))
    list_of_numbers.append(number)
    print("Number {} added to list".format(number))

    validation = str(input("Do yoy want add another number to list? [Y/N] \n"
                           "=> "))

    if validation == "N":
        add_numbers = False

print("The max number in your list is: {}".format(str(max(list_of_numbers))))
print("The min number in your list is: {}".format(str(min(list_of_numbers))))

new_list_of_numbers = input("Enter a list of numbers separated by commas \n"
                            "=> ")

# Saving numbers in the input separated by commas
string_list_of_numbers = new_list_of_numbers.split(",")

print("The list is: {}".format(string_list_of_numbers))

# Using list comprehension to convert list of strings to list of integers
list_of_numbers_parsed = [int(number) for number in string_list_of_numbers]

print("The list parsed is: {}".format(list_of_numbers_parsed))
