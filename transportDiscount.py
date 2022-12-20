age = int(input("Enter your age: "))
type_of_credential = \
    input("Enter your type of credential: (S) Student | (P) professional | (F) Big family | (N) no one\n")

# If 18 is less or equal to age and age is less or equal to 25 and type of credential is equal to "S"
# or age is less than 10 or age is more than 65 and also type of credential is equal to "P"
# or type of credential is equal to "F" then the user have discount
if (18 <= age <= 25 and type_of_credential == "S") \
        or age < 10 \
        or (age > 65 and type_of_credential == "P") \
        or (type_of_credential == "F"):
    print("Congratulations :D!! You have discount")

# if the previous conditions isn't true then you don't have discount
else:
    print("You don't have discount :(")
