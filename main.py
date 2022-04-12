"""battleship.py: battleship game on CLI"""


# creates a grid size x size
def create_grid(size):
    result = []
    for i in range(size):
        result.append([])
        for j in range(size):
            result[i].append(" ")
    return result


# prints the grid with everything on it column by column
def show_grid(grid):
    size = range(len(grid))
    for i in size:
        for j in size:
            print(f"{grid[j][i]:5} |", end="")
        print("\n")


# prints the grid with only the hits or misses
# used to print the grid for the other player to see
def peek_grid(grid):
    size = range(len(grid))
    for i in size:
        for j in size:
            if grid[j][i] != "ship":
                print(f"{grid[j][i]:5} |", end="")
            else:
                print(f"      |", end="")
        print("\n")


# ask user for coordinates as one string and converts it to a list of tuples
# input example: "1,4 2,4 3,4" -> output: [(1, 4), (2, 4), (3, 4)]
def get_location():
    result = []

    # ask user for input
    location = str(input("Enter the coordinates: "))
    coordinates = location.split()

    for i in coordinates:
        (x_cord, y_cord) = (int(i.split(",")[0]), int(i.split(",")[1]))
        result.append((x_cord, y_cord))

    return result


# player a adds ships to the grid with the coordinates from get_location()
def add_ships():
    global grid_p1, grid_p2, played
    ships = 0  # where ships is a row of "ship" on the grid

    # checks whos turn it is
    if played:
        grid = grid_p1
        player = "1"
    else:
        grid = grid_p2
        player = "2"

    while ships < 5:
        available = True
        coord = get_location()

        # check if all coords are available
        for i in coord:
            if grid[i[0]][i[1]] != " ":
                available = False
                message = "Unvailable space. A ship is already there."

        # checks if coords are in a straigth line
        if available:
            if coord[0][0] == coord[1][0]:
                for i in range(1, len(coord) - 1):
                    if coord[i][0] != coord[i + 1][0]:
                        available = False
                        message = "The coordinates entered must be in a straight line."
            elif coord[0][1] == coord[1][1]:
                for i in range(1, len(coord) - 1):
                    if coord[i][1] != coord[i + 1][1]:
                        available = False
                        message = "The coordinates entered must be in a straight line."
            else:
                available = False
                message = "The coordinates entered must be in a straight line."

        # checks if coords are next to each other
        if available:
            for i in range(len(coord) - 1):
                sum_1 = coord[i][0] + coord[i][1]
                sum_2 = coord[i + 1][0] + coord[i + 1][1]
                if sum_1 + 1 != sum_2:
                    available = False
                    message = "Some of the coordinates entered are not next to each other. You have to enter them in order."

        # puts ships in the coords provided
        if available:
            for i in coord:
                grid[i[0]][i[1]] = "ship"
            print(
                f"-------------------------- Player {player}'s grid ---------------------------"
            )
            show_grid(grid)
            ships += 1
        else:
            print(message)


# asks each player to place their ships
def start():
    global grid_p1, grid_p2, played

    # starts with player 1 as True
    played = True

    grid_p1 = create_grid(10)
    grid_p2 = create_grid(10)

    # add ships to player 1
    print("Add your ships player 1")
    add_ships()
    played = False
    print(grid_p1)

    # add ships to player 2
    print("Add your ships player 2")
    add_ships()
    played = True


# player a attacks the other player at coordinate (x, y)
def attack():
    global grid_p1, grid_p2, played
    not_attacked = True

    # if True then its player 1's turn so attack on grid_p2
    if played:
        grid = grid_p2
        other_player = "2"
    else:
        grid = grid_p1
        other_player = "1"

    print("Your turn.")
    print(f"Player {other_player}'s grid")
    peek_grid(grid)

    while not_attacked:
        # gets coords to attack
        coord = get_location()[0]

        if grid[coord[0]][coord[1]] == "ship":
            grid[coord[0]][coord[1]] = "hit"
            not_attacked = False
        elif grid[coord[0]][coord[1]] == "hit" or grid[coord[0]][coord[1]] == "miss":
            print("You have already tried there. Try again.")
        else:
            grid[coord[0]][coord[1]] = "miss"
            not_attacked = False

        # passes the next turn to the openent
        played = not played

    print(f"Player {other_player}'s grid")
    peek_grid(grid)


# checks if the game is finished
# if all ships are sunk (5 + 4 + 3 + 3 + 2 = 17)
def finished():
    global grid_p1, grid_p2, played
    hits = 0
    i = 0
    j = 0
    result = False

    # if played is False player 1 just played so check grid_p2
    if played:
        grid = grid_p1
    else:
        grid = grid_p2

    while hits < 17 and i < 10:
        if grid[i][j] == "hit":
            hits += 1
        j += 1

        if j == 10:
            j = 0
            i += 1

    if hits == 17:
        result = True

    return result


def main():
    global grid_p1, grid_p2, played
    not_finished = True

    start()

    # # for testing
    # played = True
    # grid_p1 = [
    #     [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    #     [" ", "ship", "ship", "ship", "ship", "ship", " ", " ", " ", " "],
    #     [" ", " ", " ", " ", " ", " ", "ship", "ship", "ship", " "],
    #     [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    #     [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    #     [" ", "ship", " ", " ", " ", " ", " ", " ", " ", " "],
    #     [" ", "ship", " ", " ", " ", " ", "ship", "ship", "ship", "ship"],
    #     [" ", "ship", " ", " ", " ", " ", " ", " ", " ", " "],
    #     [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    #     [" ", " ", " ", " ", " ", " ", " ", "ship", "ship", " "],
    # ]
    # grid_p2 = [
    #     [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    #     [" ", "ship", "ship", "ship", "ship", "ship", " ", " ", " ", " "],
    #     [" ", " ", " ", " ", " ", " ", "ship", "ship", "ship", " "],
    #     [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    #     [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    #     [" ", "ship", " ", " ", " ", " ", " ", " ", " ", " "],
    #     [" ", "ship", " ", " ", " ", " ", "ship", "ship", "ship", "ship"],
    #     [" ", "ship", " ", " ", " ", " ", " ", " ", " ", " "],
    #     [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    #     [" ", " ", " ", " ", " ", " ", " ", "ship", "ship", " "],
    # ]

    while not_finished:
        attack()
        if finished():
            not_finished = False

    if played:
        player = "2"
    else:
        player = "1"

    print(f"Game Over. Player {player} won.")


if __name__ == "__main__":
    main()
