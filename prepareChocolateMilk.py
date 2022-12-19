haveMilk = input("We have milk? (s/n) ")
haveChocolate = input("We have chocolate? (s/n) ")

if haveMilk != "s" or haveChocolate != "s":
    print("Go to Marketplace")
    if haveMilk != "s":
        print("Buy milk")
    if haveChocolate != "s":
        print("Buy chocolate")

print("Preparing milk with chocolate")
