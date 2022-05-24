"""bot.py: bot functions for battleship"""

import random


def rand_coord():
    x = random.randint(0, 9)
    y = random.randint(0, 9)
    return (x, y)


def guess(mat):
    value = "hit-"
    while value == "hit-" or value == "miss":
        x, y = rand_coord()
        value = mat[x][y]

    return (x, y)


def set_ships():
    mat = [["----" for x in range(10)] for x in range(10)]
    ship_id = 0

    while ship_id < 5:
        rot = rotated()
        x, y = rand_coord()

        # for destroyer
        if ship_id == 0:
            if not rot:
                if y < 9 and not check_if_ship(mat, (x, y), 2, rot):
                    for i in range(2):
                        mat[x][y + i] = "ship"
                    ship_id += 1
            else:
                if x < 9 and not check_if_ship(mat, (x, y), 2, rot):
                    for i in range(2):
                        mat[x + i][y] = "ship"
                    ship_id += 1
        # for cruiser and submarine
        elif ship_id == 1 or ship_id == 2:
            if not rot:
                if y < 8 and not check_if_ship(mat, (x, y), 3, rot):
                    for i in range(3):
                        mat[x][y + i] = "ship"
                    ship_id += 1
            else:
                if x < 8 and not check_if_ship(mat, (x, y), 3, rot):
                    for i in range(3):
                        mat[x + i][y] = "ship"
                    ship_id += 1
        # for battleship
        elif ship_id == 3:
            if not rot:
                if y < 7 and not check_if_ship(mat, (x, y), 4, rot):
                    for i in range(4):
                        mat[x][y + i] = "ship"
                    ship_id += 1
            else:
                if x < 7 and not check_if_ship(mat, (x, y), 4, rot):
                    for i in range(4):
                        mat[x + i][y] = "ship"
                    ship_id += 1
        # for carrier
        elif ship_id == 4:
            if not rot:
                if y < 6 and not check_if_ship(mat, (x, y), 5, rot):
                    for i in range(5):
                        mat[x][y + i] = "ship"
                    ship_id += 1
            else:
                if x < 6 and not check_if_ship(mat, (x, y), 5, rot):
                    for i in range(5):
                        mat[x + i][y] = "ship"
                    ship_id += 1
    return mat


def check_if_ship(mat, coord, l, rotated):
    if_ship = False
    x, y = coord

    for i in range(l):
        if not rotated and mat[x][y + i] == "ship":
            if_ship = True
        elif rotated and mat[x + i][y] == "ship":
            if_ship = True

    return if_ship


def rotated():
    result = False
    num = random.randint(1, 100)
    if num % 2 == 0:
        result = True

    return result
