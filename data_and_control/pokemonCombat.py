from random import randint

PIKACHU_INITIAL_LIFE = 80
SQUIRTLE_INITIAL_LIFE = 90

pikachu_life = PIKACHU_INITIAL_LIFE
squirtle_life = SQUIRTLE_INITIAL_LIFE

while pikachu_life > 0 and squirtle_life > 0:
    # Start the combat

    # pikachu turn
    print("\n ===Pikachu Turn=== \n")
    attack_pikachu = randint(1, 2)
    if attack_pikachu == 1:
        # Volt ball
        print("Pikachu attack with volt ball")
        squirtle_life -= 10
    else:
        print("Pikachu attack with thunder shock")
        squirtle_life -= 11

    if squirtle_life < 0:
        squirtle_life = 0
    elif pikachu_life < 0:
        pikachu_life = 0

    pikachu_life_bar = int(pikachu_life * 10 / PIKACHU_INITIAL_LIFE)
    print("Pikachu: \t [{}{}] ({}/{})".format("=" * pikachu_life_bar, " " * (10 - pikachu_life_bar),
                                              pikachu_life, PIKACHU_INITIAL_LIFE))

    squirtle_life_bar = int(squirtle_life * 10 / SQUIRTLE_INITIAL_LIFE)
    print("Squirtle: \t [{}{}] ({}/{})".format("=" * squirtle_life_bar, " " * (10 - squirtle_life_bar),
                                              squirtle_life, SQUIRTLE_INITIAL_LIFE))

    # squirtle turn
    print("\n ===Squirtle Turn=== \n")
    attack_squirtle = None
    while attack_squirtle not in [1, 2, 3]:
        attack_squirtle = int(input("Enter your attack! \n"
                                    "1.- Tacke \n"
                                    "2.- Water gun \n"
                                    "3.- Bubble \n"
                                    "=> "))

    if attack_squirtle == 1:
        print("Squirtle attack with Tacke")
        pikachu_life -= 10
    elif attack_squirtle == 2:
        print("Squirtle attack with water gun")
        pikachu_life -= 12
    elif attack_squirtle == 3:
        print("Squirtle attack with bubble")
        pikachu_life -= 7

    if squirtle_life < 0:
        squirtle_life = 0
    elif pikachu_life < 0:
        pikachu_life = 0

    pikachu_life_bar = int(pikachu_life * 10 / PIKACHU_INITIAL_LIFE)
    print("Pikachu: \t [{}{}] ({}/{})".format("=" * pikachu_life_bar, " " * (10 - pikachu_life_bar),
                                              pikachu_life, PIKACHU_INITIAL_LIFE))

    squirtle_life_bar = int(squirtle_life * 10 / SQUIRTLE_INITIAL_LIFE)
    print("Squirtle: \t [{}{}] ({}/{})".format("=" * squirtle_life_bar, " " * (10 - squirtle_life_bar),
                                              squirtle_life, SQUIRTLE_INITIAL_LIFE))

if pikachu_life > squirtle_life:
    print("\n Pikachu is the Winner! \n")
else:
    print("\n Squirtle is the Winner! \n")
