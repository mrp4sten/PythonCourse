import os
import random

import readchar as readchar

# Constants
POSITION_X = 0
POSITION_Y = 1

MAP_WIDTH = 20
MAP_HEIGHT = 15

NUM_OF_MAP_OBJECTS = 11

# Position
my_position = [3, 1]
tail_length = 0
tail = []

# Objects
map_objects = []

# Settings
game_over = False
snake_died = False

while not game_over:
    while len(map_objects) < NUM_OF_MAP_OBJECTS:
        new_position = [random.randint(0, MAP_WIDTH), random.randint(0, MAP_HEIGHT)]
        if new_position not in map_objects and new_position != my_position:
            map_objects.append(new_position)

    # Map
    print("+" + "-" * MAP_WIDTH * 3 + "+")

    for coordination_y in range(MAP_HEIGHT):
        print("|", end="")

        for coordinate_x in range(MAP_WIDTH):
            chart_object = " "
            object_in_cell = None
            tail_in_cell = None

            for map_object in map_objects:
                if map_object[POSITION_X] == coordinate_x and map_object[POSITION_Y] == coordination_y:
                    chart_object = "•"
                    object_in_cell = map_object

            for tail_piece in tail:
                if tail_piece[POSITION_X] == coordinate_x and tail_piece[POSITION_Y] == coordination_y:
                    chart_object = "×"
                    tail_in_cell = tail_piece

            if my_position[POSITION_X] == coordinate_x and my_position[POSITION_Y] == coordination_y:
                print(" X ", end="")

                if object_in_cell:
                    map_objects.remove(object_in_cell)
                    tail_length += 1

                if tail_in_cell:
                    game_over = True
                    snake_died = True

            else:
                print(" {} ".format(chart_object), end="")

        print("|")

    print("+" + "-" * MAP_WIDTH * 3 + "+")

    # Ask user where he wants to move
    direction = readchar.readchar()

    if direction == "w":
        tail.insert(0, my_position.copy())
        tail = tail[:tail_length]
        my_position[POSITION_Y] -= 1
        my_position[POSITION_Y] %= MAP_HEIGHT
    elif direction == "s":
        tail.insert(0, my_position.copy())
        tail = tail[:tail_length]
        my_position[POSITION_Y] += 1
        my_position[POSITION_Y] %= MAP_HEIGHT
    elif direction == "d":
        tail.insert(0, my_position.copy())
        tail = tail[:tail_length]
        my_position[POSITION_X] += 1
        my_position[POSITION_X] %= MAP_WIDTH
    elif direction == "a":
        tail.insert(0, my_position.copy())
        tail = tail[:tail_length]
        my_position[POSITION_X] -= 1
        my_position[POSITION_X] %= MAP_WIDTH
    elif direction == "q":
        game_over = True

    os.system("clear")

if snake_died:
    print("===GAME OVER===")
