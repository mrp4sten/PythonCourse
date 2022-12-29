welcome = "Welcome to my Test for buy a Smartphone"
print("\n" + "-" * len(welcome) + "\n" + welcome + "\n" + "-" * len(welcome))

ERROR_MESSAGE = "Option not supported ty again! :D"
RECOMMENDATION_MESSAGE = "You should buy some of this Smartphones: \n"

firstQuestion = input("What do you like? \n"
                      "A) Apple \n"
                      "B) Android \n"
                      "=>")

secondQuestion = input("Do you have money?\n"
                       "A) Yes \n"
                       "B) No \n")

if firstQuestion == "A" and secondQuestion == "A":
    thirdQuestion = input("Do you use each day the camera? \n"
                          "A) Yes \n"
                          "B) No \n"
                          "=>")
    if thirdQuestion == "A":
        print(RECOMMENDATION_MESSAGE +
              "1.- IPhone 14 Pro Max\n"
              "2.- IPhone 14 Pro\n")
    elif thirdQuestion == "B":
        print(RECOMMENDATION_MESSAGE +
              "1.- IPhone 13 Pro Max \n"
              "2.- IPhone 13 Pro \n")
    else:
        print(ERROR_MESSAGE)

elif firstQuestion == "A" and secondQuestion == "B":
    print(RECOMMENDATION_MESSAGE +
          "1.- IPhone 12 Pro Max \n"
          "2.- IPhone 12 Pro \n")

elif firstQuestion == "B" and secondQuestion == "A":
    thirdQuestion = input("Do you use each day the camera? \n"
                          "A) Yes \n"
                          "B) No \n"
                          "=>")
    if thirdQuestion == "A":
        print(RECOMMENDATION_MESSAGE +
              "1.- Samsung S22 Ultra \n"
              "2.- Samsung S22 pro \n")
    elif thirdQuestion == "B":
        print(RECOMMENDATION_MESSAGE +
              "1.- Samsung S22 \n"
              "2.- Samsung S21 \n")
    else:
        print(ERROR_MESSAGE)

elif firstQuestion == "B" and secondQuestion == "B":
    print(RECOMMENDATION_MESSAGE +
          "1.- Samsung S21 FE \n"
          "2.- Samsung S20 FE \n")

else:
    print(ERROR_MESSAGE)
