"""Bot brains for battleship."""

import random
import pygame


def rand_coord():
    """
    Generates random coordinates.

    Returns:
        (x, y) (tuple[int, int]): Coords.
    """
    x = random.randint(0, 9)
    y = random.randint(0, 9)
    return (x, y)


def guess(mat, ships_p1, ship_coords):
    """
    Generates random coords which have not been guessed before.

    Parameters:
        mat (list[list[str]]): Player 1 matrice.

    Returns:
        (x, y) (tuple[int, int]): Coords.
    """

    hit_ships = hit_coords(mat)
    sunk_ships = sunk_coords(ships_p1, ship_coords)

    # hunts (tries to find the most probable position of a ship)
    heat_map = pdf(mat, ships_p1, hit_ships, sunk_ships)
    # eliminates position that have already been guessed
    for coord in hit_ships:
        heat_map[coord[0]][coord[1]] = 0
    show_mat(heat_map)
    x, y = max_coord(heat_map)
    print(f"Guess is {x}, {y}")
    print(hit_ships)
    print(sunk_ships)

    return (x, y)


def pdf(mat, ships, hit_ships, sunk_ships):
    heat_map = [[0 for x in range(10)] for x in range(10)]

    # determines which ships are not sunk and appends their length to ship_lenght
    ship_length = []
    for i in range(5):
        if ships[4][i] == False:
            # for destroyer
            if i == 0:
                ship_length.append(2)
            # for cruiser and submarine
            elif i == 1 or i == 2:
                ship_length.append(3)
            # for battleship
            elif i == 3:
                ship_length.append(4)
            # for carrier
            elif i == 4:
                ship_length.append(5)

    # if all ships it hit are sunk -> hunt mode
    if len(hit_ships) == len(sunk_ships):
        hit_not_sunk = [(-1, -1)]
    else:
        hit_not_sunk = []
        for coord in hit_ships:
            if coord not in sunk_ships:
                hit_not_sunk.append(coord)

    for coord in hit_not_sunk:
        # determines all the possible ship positions
        for length in ship_length:
            # restrains from guessing outside the grid
            for i in range(11 - length):
                for j in range(10):
                    # checks if horizontal (rotated) ships can be there
                    if available(mat, (i, j), length, True, coord, sunk_ships):
                        # add one to all the positions
                        add_one(heat_map, (i, j), length, True)
                    # checks if vertical (unrotated) ships can be there
                    if available(mat, (j, i), length, False, coord, sunk_ships):
                        # add one to all the positions
                        add_one(heat_map, (j, i), length, False)

    return heat_map


def available(mat, coord, length, rotated, contains, sunk_ships):
    result = True
    contains_hit = False

    for i in range(length):
        if rotated:
            if contains == (-1, -1):
                if (
                    mat[coord[0] + i][coord[1]] == "hit-"
                    or mat[coord[0] + i][coord[1]] == "miss"
                ):
                    result = False
            else:
                if (coord[0] + i, coord[1]) in sunk_ships or mat[coord[0] + i][
                    coord[1]
                ] == "miss":
                    result = False
                else:
                    if (coord[0] + i, coord[1]) == contains:
                        contains_hit = True
        else:
            if contains == (-1, -1):
                if (
                    mat[coord[0]][coord[1] + i] == "hit-"
                    or mat[coord[0]][coord[1] + i] == "miss"
                ):
                    result = False
            else:
                if (coord[0], coord[1] + 1) in sunk_ships or mat[coord[0]][
                    coord[1] + i
                ] == "miss":
                    result = False
                else:
                    if (coord[0], coord[1] + i) == contains:
                        contains_hit = True

    if contains != (-1, -1):
        # if does not contains hit
        if result and not contains_hit:
            result = False

    return result


def add_one(mat, coord, length, rotated):
    for i in range(length):
        if rotated:
            mat[coord[0] + i][coord[1]] += 1
        else:
            mat[coord[0]][coord[1] + i] += 1


def max_coord(mat):
    num = mat[0][0]
    coord = (0, 0)
    for i in range(10):
        for j in range(10):
            if mat[i][j] > num:
                num = mat[i][j]
                coord = (i, j)
    return coord


def hit_coords(mat):
    result = []
    for i in range(10):
        for j in range(10):
            # if hit appends its coordinates to list
            if mat[i][j] == "hit-":
                result.append((i, j))
    return result


def sunk_coords(ships, ship_coord):
    result = []
    for i in range(5):
        # if sunk
        if ships[4][i] == True:
            # appends its coordinates to list
            for coord in ship_coord[i]:
                result.append(coord)
    return result


def set_ships(ship_coord, ships, grid):
    """
    Randomly choses a ship position and places it's image correctly.

    Checks if ship fits on matrix and does not overlap another ship.

    Returns:
        mat (list[list[str]]): Matrix with ships on it.
    """

    mat = [["----" for x in range(10)] for x in range(10)]
    ship_id = 0
    # grid position
    g_x = grid.left
    g_y = grid.top

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
                        ship_coord[ship_id].append((x, y + i))
                    # sets ship_img center
                    ships[1][ship_id].center = (x * 60 + g_x + 30, y * 60 + g_y + 60)

                    ship_id += 1
            else:
                # checks if ship fits on matrix and does not overlap another ship
                if x < 9 and not check_if_ship(mat, (x, y), 2, rot):
                    for i in range(2):
                        mat[x + i][y] = "ship"
                        ship_coord[ship_id].append((x + i, y))
                    # sets ship_img center and rotates it
                    ships[0][ship_id] = pygame.transform.rotate(ships[0][ship_id], 90)
                    ships[1][ship_id] = ships[0][ship_id].get_rect()
                    ships[1][ship_id].center = (x * 60 + g_x + 60, y * 60 + g_y + 30)

                    ship_id += 1

        # for cruiser and submarine (3 long)
        elif ship_id == 1 or ship_id == 2:
            if not rot:
                # checks if ship fits on matrix and does not overlap another ship
                if y < 8 and not check_if_ship(mat, (x, y), 3, rot):
                    for i in range(3):
                        mat[x][y + i] = "ship"
                        ship_coord[ship_id].append((x, y + i))
                    # sets ship_img
                    ships[1][ship_id].center = (x * 60 + g_x + 30, y * 60 + g_y + 90)
                    ship_id += 1
            else:
                # checks if ship fits on matrix and does not overlap another ship
                if x < 8 and not check_if_ship(mat, (x, y), 3, rot):
                    for i in range(3):
                        mat[x + i][y] = "ship"
                        ship_coord[ship_id].append((x + i, y))
                    # sets ship_img center and rotates it
                    ships[0][ship_id] = pygame.transform.rotate(ships[0][ship_id], 90)
                    ships[1][ship_id] = ships[0][ship_id].get_rect()
                    ships[1][ship_id].center = (x * 60 + g_x + 90, y * 60 + g_y + 30)

                    ship_id += 1

        # for battleship (4 long)
        elif ship_id == 3:
            if not rot:
                # checks if ship fits on matrix and does not overlap another ship
                if y < 7 and not check_if_ship(mat, (x, y), 4, rot):
                    for i in range(4):
                        mat[x][y + i] = "ship"
                        ship_coord[ship_id].append((x, y + i))
                    # sets ship_img
                    ships[1][ship_id].center = (x * 60 + g_x + 30, y * 60 + g_y + 120)

                    ship_id += 1
            else:
                # checks if ship fits on matrix and does not overlap another ship
                if x < 7 and not check_if_ship(mat, (x, y), 4, rot):
                    for i in range(4):
                        mat[x + i][y] = "ship"
                        ship_coord[ship_id].append((x + i, y))
                    # sets ship_img center and rotates it
                    ships[0][ship_id] = pygame.transform.rotate(ships[0][ship_id], 90)
                    ships[1][ship_id] = ships[0][ship_id].get_rect()
                    ships[1][ship_id].center = (x * 60 + g_x + 120, y * 60 + g_y + 30)

                    ship_id += 1

        # for carrier (5 long)
        elif ship_id == 4:
            if not rot:
                # checks if ship fits on matrix and does not overlap another ship
                if y < 6 and not check_if_ship(mat, (x, y), 5, rot):
                    for i in range(5):
                        mat[x][y + i] = "ship"
                        ship_coord[ship_id].append((x, y + i))
                    # sets ship_img
                    ships[1][ship_id].center = (x * 60 + g_x + 30, y * 60 + g_y + 150)

                    ship_id += 1
            else:
                # checks if ship fits on matrix and does not overlap another ship
                if x < 6 and not check_if_ship(mat, (x, y), 5, rot):
                    for i in range(5):
                        mat[x + i][y] = "ship"
                        ship_coord[ship_id].append((x + i, y))
                    # sets ship_img center and rotates it
                    ships[0][ship_id] = pygame.transform.rotate(ships[0][ship_id], 90)
                    ships[1][ship_id] = ships[0][ship_id].get_rect()
                    ships[1][ship_id].center = (x * 60 + g_x + 150, y * 60 + g_y + 30)

                    ship_id += 1
    return (mat, ship_coord)


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


def show_mat(m):
    """
    Prints a matrix

    Debug function, not used in the code.

    Parameters:
        m (list[list[str]])
    """

    for i in range(10):
        for j in range(10):
            print(f"{m[j][i]:>2}", end=" ")
        print("\n")
