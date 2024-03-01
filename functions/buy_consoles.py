EXIT = "Q"
items = [
    "Xbox One Series X",
    "Nintendo Switch",
    "Playstation 5",
    "Xbox Series S",
    "Playstation 4",
    "Xbox 360",
    "playstation 3",
    "nintendo wii",
    "playstation 2",
    "xbox one",
]


def ask_user():
    selected_item = input(
        "Add console to car , press {} to quit: "
    ).format(EXIT)
    while selected_item.lower() not in items and selected_item != EXIT:
        print("No poseemos stock de dicha consola")
        selected_item = input(
            "Add console to car , press {} to quit: "
        ).format(EXIT)
    return selected_item.lower


def save_file(lista):
    nombre_fichero = input("Enter the filename:")
    with open(nombre_fichero + ".txt", "w") as new_archive:
        new_archive.write("\n".join(lista))


def main():
    lista = []
    input_usuario = ask_user()
    while input_usuario != EXIT:
        lista.append(input_usuario)
        print("\n".join(lista))
        input_usuario = ask_user()
    save_file(lista)


if __name__ == "__main__":
    main()
