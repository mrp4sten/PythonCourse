welcome = "Welcome to buy list"
print("\n" + "=" * len(welcome) + "\n" + welcome + "\n" + "=" * len(welcome) + "\n")

buy_list = []
product_to_list = None

while True:
    product_to_list = input("What do you want add to buy list? \n"
                            "(Press Q to Exit) \n"
                            "=> ")
    if product_to_list == "Q":
        break
    elif product_to_list in buy_list:
        print("{} is already added to list".format(product_to_list))

    else:
        validation = input("Are you sure that do you want to add {} ? \n"
                           "[Y/N] => ".format(product_to_list))
        if validation == "Y":
            buy_list.append(product_to_list)
            print("{} added to list".format(product_to_list))
        elif validation == "N":
            print("Operation cancelled")

if len(buy_list) < 0:
    print("The list is empty")
else:
    print("The buy list is: \n"
          "{}".format(buy_list))
