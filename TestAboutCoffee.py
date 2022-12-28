welcome = "Welcome to my personal test about the Coffee"
print("=" * len(welcome) + "\n" + welcome + "\n" + "=" * len(welcome) + "\n")

print("===Answer the next questions to evaluate if you are a coffee lover!===")

score = 0
print("==Score: {}==".format(score))

question = input("Question 1: How often do you drink coffee?\n"
                 "a) Never \n"
                 "b) Some times\n"
                 "c) Each day \n")

if question == "A" or question == "a":
    # this is like score = score + 0
    score += 0
elif question == "B" or question == "b":
    score += 5
elif question == "C" or question == "c":
    score += 10
else:
    print("The options are a, b and c")
    exit()

question = input("Question 2: What's you method of making coffee?\n"
                 "a) Pour Over/Drip: Coffee Cone\n"
                 "b) Percolate: Stovetop Moka Pot\n"
                 "c) Pour Over/Drip: Chemex \n")

if question == "A" or question == "a":
    score += 0
elif question == "B" or question == "b":
    score += 5
elif question == "C" or question == "c":
    score += 10
else:
    print("The options are a, b and c")
    exit()

question = input("Question 3: Do you think that the soluble coffee is the best coffe?\n"
                 "a) Yes\n"
                 "b) Some times\n"
                 "c) Absolutely no! \n")

if question == "A" or question == "a":
    score += 0
elif question == "B" or question == "b":
    score += 5
elif question == "C" or question == "c":
    score += 10
else:
    print("The options are a, b and c")
    exit()

result = "your score is of {} ".format(score)
if score >= 25:
    print(result + " you really be a coffee lover")
elif score >= 10:
    print(result + " do you like the coffee")
elif score < 10:
    print(result + " you are a coffee heater")
