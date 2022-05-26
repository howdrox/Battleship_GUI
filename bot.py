"""Bot brains for battleship."""

import random


def rand_coord():
    """
    Generates random coordinates.

    Returns:
        (x, y) (tuple[int, int]): Coords.
    """
    x = random.randint(0, 9)
    y = random.randint(0, 9)
    return (x, y)


def guess(mat):
    """
    Generates random coords which have not been guessed before.

    Parameters:
        mat (list[list[str]]): Player 1 matrice.

    Returns:
        (x, y) (tuple[int, int]): Coords.
    """

    value = "hit-"
    while value == "hit-" or value == "miss":
        x, y = rand_coord()
        value = mat[x][y]

    return (x, y)


def set_ships():
    """
    Randomly sets ships.

    Checks if ship fits on matrix and does not overlap another ship.

    Returns:
        mat (list[list[str]]): Matrix with ships on it.
    """

    mat = [["----" for x in range(10)] for x in range(10)]
    ship_id = 0

    # while not all ships are placed
    while ship_id < 5:
        # generates randomly coordinates and if ship should be rotated
        rot = rotated()
        x, y = rand_coord()

        # for destroyer (2 long)
        if ship_id == 0:
            if not rot:
                # checks if ship fits on matrix and does not overlap another ship
                if y < 9 and not check_if_ship(mat, (x, y), 2, rot):
                    for i in range(2):
                        mat[x][y + i] = "ship"
                    ship_id += 1
            else:
                # checks if ship fits on matrix and does not overlap another ship
                if x < 9 and not check_if_ship(mat, (x, y), 2, rot):
                    for i in range(2):
                        mat[x + i][y] = "ship"
                    ship_id += 1
        # for cruiser and submarine (3 long)
        elif ship_id == 1 or ship_id == 2:
            if not rot:
                # checks if ship fits on matrix and does not overlap another ship
                if y < 8 and not check_if_ship(mat, (x, y), 3, rot):
                    for i in range(3):
                        mat[x][y + i] = "ship"
                    ship_id += 1
            else:
                # checks if ship fits on matrix and does not overlap another ship
                if x < 8 and not check_if_ship(mat, (x, y), 3, rot):
                    for i in range(3):
                        mat[x + i][y] = "ship"
                    ship_id += 1
        # for battleship (4 long)
        elif ship_id == 3:
            if not rot:
                # checks if ship fits on matrix and does not overlap another ship
                if y < 7 and not check_if_ship(mat, (x, y), 4, rot):
                    for i in range(4):
                        mat[x][y + i] = "ship"
                    ship_id += 1
            else:
                # checks if ship fits on matrix and does not overlap another ship
                if x < 7 and not check_if_ship(mat, (x, y), 4, rot):
                    for i in range(4):
                        mat[x + i][y] = "ship"
                    ship_id += 1
        # for carrier (5 long)
        elif ship_id == 4:
            if not rot:
                # checks if ship fits on matrix and does not overlap another ship
                if y < 6 and not check_if_ship(mat, (x, y), 5, rot):
                    for i in range(5):
                        mat[x][y + i] = "ship"
                    ship_id += 1
            else:
                # checks if ship fits on matrix and does not overlap another ship
                if x < 6 and not check_if_ship(mat, (x, y), 5, rot):
                    for i in range(5):
                        mat[x + i][y] = "ship"
                    ship_id += 1
    return mat


def check_if_ship(mat, coord, l, rotated):
    """
    Checks if ship does not overlap another previously place ship.

    Parameters:
        mat (list[list[str]]): Matrix.
        coord (tuple[int, int]): Coordinate.
        l (int): Lenght of ship.
        rotated (bool): If rotated.

    Returns:
        if_ship (bool): If there is a ship already there.
    """
    if_ship = False
    x, y = coord

    for i in range(l):
        if not rotated and mat[x][y + i] == "ship":
            if_ship = True
        elif rotated and mat[x + i][y] == "ship":
            if_ship = True

    return if_ship


def rotated():
    """
    Randomly generates a `bool`.

    Returns:
        result (bool): Random.
    """

    result = bool(random.getrandbits(1))

    return result
