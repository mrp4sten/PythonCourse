welcome = "Welcome to my Currency converter"
print("\n" + "-" * len(welcome) + "\n" + welcome + "\n" + "-" * len(welcome))

valueToConvert = input("What's your type of currency?\n"
                       "a) Pounds \n"
                       "b) Euro \n"
                       "c) Dollar"
                       "=>")

if valueToConvert == "a" or valueToConvert == "A":
    pounds = float(input("Enter your Pounds(£): "))
    euro = pounds * 1.5
    dollar = pounds * 1.20
    print("{}£ is equal to {}€".format(pounds, euro))
    print("{}£ is equal to {}$".format(pounds, dollar))

elif valueToConvert == "b" or valueToConvert == "B":
    euro = float(input("Enter your Euro(€): "))
    pounds = euro * 0.88
    dollar = euro * 1.06
    print("{}€ is equal to {}£".format(euro, pounds))
    print("{}€ is equal to {}$".format(pounds, dollar))

elif valueToConvert == "c" or valueToConvert == "C":
    dollar = float(input("Enter your Dollar($): "))
    pounds = dollar * 0.83
    euro = dollar * 0.94
    print("{}$ is equal to {}£".format(dollar, pounds))
    print("{}$ is equal to {}€".format(dollar, euro))

else:
    print("Currency not supported for now")

