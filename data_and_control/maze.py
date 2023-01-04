import os

import readchar as readchar

# Constants
POSITION_X = 0
POSITION_Y = 1

MAP_WIDTH = 20
MAP_HEIGHT = 15

# Position
my_position = [3, 1]

# Objects
map_objects = [[2, 3], [5, 4], [3, 4], [10, 6]]

while True:
    # Map
    print("+" + "-" * MAP_WIDTH * 3 + "+")

    for coordination_y in range(MAP_HEIGHT):
        print("|", end="")

        for coordinate_x in range(MAP_WIDTH):
            chart_object = " "
            object_in_cell = None

            for map_object in map_objects:
                if map_object[POSITION_X] == coordinate_x and map_object[POSITION_Y] == coordination_y:
                    chart_object = "×"
                    object_in_cell = map_object

            if my_position[POSITION_X] == coordinate_x and my_position[POSITION_Y] == coordination_y:
                print(" Ω ", end="")
                if object_in_cell:
                    map_objects.remove(object_in_cell)
            else:
                print(" {} ".format(chart_object), end="")

        print("|")

    print("+" + "-" * MAP_WIDTH * 3 + "+")

    # Ask user where he wants to move
    direction = readchar.readchar()

    if direction == "w":
        my_position[POSITION_Y] -= 1
        my_position[POSITION_Y] %= MAP_HEIGHT
    elif direction == "s":
        my_position[POSITION_Y] += 1
        my_position[POSITION_Y] %= MAP_HEIGHT
    elif direction == "d":
        my_position[POSITION_X] += 1
        my_position[POSITION_X] %= MAP_WIDTH
    elif direction == "a":
        my_position[POSITION_X] -= 1
        my_position[POSITION_X] %= MAP_WIDTH
    elif direction == "q":
        break

    os.system("clear")
