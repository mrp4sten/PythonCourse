a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for item in a:
    print(item)

vowels = ["a", "e", "i", "o", "u"]
phrase = "Hi I'm learn Python on Mastermind"
vowels_in_phrase = 0

for letter in phrase:
    if letter in vowels:
        print("Vowel founded: {}".format(letter))
        vowels_in_phrase += 1

print("Vowels in phrase: {}".format(vowels_in_phrase))

number_of_times = int(input("Enter a number of times that do you want repeat \n"
                            "Hello World => "))
for i in range(number_of_times):
    print("Hello world")
