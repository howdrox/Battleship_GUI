"""play_friend.py: Multiplayer battleship game 1v1"""


import pygame

# loads all the necessary things then calls set_ships() to allow the users to position their ships
# note: loads only things that are needed for all funcitons and stages of the game
def init(screen):
    global background, grid_img, parchment_img, font_h1, font_h2, player1_text, player2_text, error_img, error_img_2, error_img_3
    global ships_p1, ships_p2
    global P1, P2, WHO, RUN

    P1 = [["----" for x in range(10)] for x in range(10)]
    P2 = [["----" for x in range(10)] for x in range(10)]
    # who's turn it is with True being player 1
    WHO = True
    # global variable if pygame should be running
    RUN = True

    # background image
    background = pygame.image.load("./img/background3.jpg")

    # grid image (599 x 599)
    grid_img = pygame.image.load("./img/grid_white.png")

    # parchment image (122 x 590)
    parchment_img = pygame.image.load("./img/parchment.png")

    # ships images
    destroyer_img = pygame.image.load("./img/destroyer2.png")
    cruiser_img = pygame.image.load("./img/cruiser2.png")
    submarine_img = pygame.image.load("./img/submarine2.png")
    battleship_img = pygame.image.load("./img/battleship2.png")
    carrier_img = pygame.image.load("./img/carrier2.png")

    # error images (1000 x 600)
    error_img = pygame.image.load("./img/blue_screen.png")
    error_img_2 = pygame.transform.scale(error_img, (1000 * 1.3, 600 * 1.3))
    error_img_3 = pygame.transform.scale(error_img, (1000 * 1.6, 600 * 1.6))

    # fonts
    font_h1 = pygame.font.Font("freesansbold.ttf", 32)
    font_h2 = pygame.font.Font("freesansbold.ttf", 24)

    # Player 1 and 2 text
    player1_text = font_h1.render("Player 1's board", True, "#FFFFFF")
    player2_text = font_h1.render("Player 2's board", True, "#FFFFFF")

    # ship data for palyer 1
    # list of [[ships_img], [ships_rect], [if_picked], [number_of_rotations], [if_sunk]]
    # initial 10 px between each ship
    ships_p1 = [
        [
            destroyer_img,
            cruiser_img,
            submarine_img,
            battleship_img,
            carrier_img,
        ],
        [
            destroyer_img.get_rect(center=(41, 150)),
            cruiser_img.get_rect(center=(41, 310)),
            submarine_img.get_rect(center=(41, 500)),
            battleship_img.get_rect(center=(93, 210)),
            carrier_img.get_rect(center=(93, 490)),
        ],
        [False, False, False, False, False],
        [0, 0, 0, 0, 0],
        [False, False, False, False, False],
    ]

    # ship data for palyer 1
    # list of [[ships_img], [ships_rect], [if_picked], [number_of_rotations], [if_sunk]]
    # initial 10 px between each ship
    ships_p2 = [
        [
            destroyer_img,
            cruiser_img,
            submarine_img,
            battleship_img,
            carrier_img,
        ],
        [
            destroyer_img.get_rect(center=(1406, 150)),
            cruiser_img.get_rect(center=(1406, 310)),
            submarine_img.get_rect(center=(1406, 500)),
            battleship_img.get_rect(center=(1458, 210)),
            carrier_img.get_rect(center=(1458, 490)),
        ],
        [False, False, False, False, False],
        [0, 0, 0, 0, 0],
        [False, False, False, False, False],
    ]

    # set_ships(screen)
    # for testing P1 and P2 are set
    P1 = [
        [
            "hit-",
            "miss",
            "----",
            "----",
            "----",
            "----",
            "----",
            "----",
            "----",
            "----",
        ],
        [
            "----",
            "ship",
            "----",
            "----",
            "----",
            "----",
            "ship",
            "ship",
            "ship",
            "----",
        ],
        [
            "----",
            "ship",
            "----",
            "----",
            "----",
            "----",
            "ship",
            "----",
            "----",
            "----",
        ],
        [
            "----",
            "----",
            "----",
            "----",
            "----",
            "----",
            "ship",
            "----",
            "----",
            "----",
        ],
        [
            "----",
            "----",
            "----",
            "----",
            "----",
            "----",
            "ship",
            "----",
            "----",
            "----",
        ],
        [
            "----",
            "----",
            "----",
            "----",
            "----",
            "----",
            "----",
            "----",
            "ship",
            "----",
        ],
        [
            "----",
            "----",
            "----",
            "----",
            "----",
            "----",
            "----",
            "----",
            "ship",
            "----",
        ],
        [
            "----",
            "ship",
            "ship",
            "ship",
            "ship",
            "----",
            "----",
            "----",
            "ship",
            "----",
        ],
        [
            "----",
            "----",
            "----",
            "----",
            "----",
            "----",
            "----",
            "----",
            "ship",
            "----",
        ],
        [
            "----",
            "----",
            "----",
            "----",
            "----",
            "----",
            "----",
            "----",
            "ship",
            "----",
        ],
    ]
    P2 = [
        [
            "----",
            "----",
            "----",
            "----",
            "----",
            "----",
            "----",
            "----",
            "----",
            "----",
        ],
        [
            "----",
            "----",
            "----",
            "----",
            "----",
            "----",
            "----",
            "----",
            "----",
            "----",
        ],
        [
            "----",
            "----",
            "----",
            "----",
            "----",
            "----",
            "----",
            "----",
            "ship",
            "----",
        ],
        [
            "----",
            "----",
            "----",
            "ship",
            "ship",
            "ship",
            "----",
            "----",
            "ship",
            "----",
        ],
        [
            "----",
            "----",
            "----",
            "----",
            "----",
            "----",
            "----",
            "----",
            "ship",
            "----",
        ],
        [
            "----",
            "----",
            "----",
            "----",
            "ship",
            "ship",
            "----",
            "----",
            "ship",
            "----",
        ],
        [
            "----",
            "ship",
            "----",
            "----",
            "----",
            "----",
            "----",
            "----",
            "----",
            "----",
        ],
        [
            "----",
            "ship",
            "----",
            "----",
            "----",
            "----",
            "----",
            "----",
            "----",
            "----",
        ],
        [
            "----",
            "ship",
            "----",
            "----",
            "ship",
            "ship",
            "ship",
            "ship",
            "ship",
            "----",
        ],
        [
            "----",
            "----",
            "----",
            "----",
            "----",
            "----",
            "----",
            "----",
            "----",
            "----",
        ],
    ]
    # checks if the window was closed, if not then continue
    if RUN:
        play_game(screen)


def set_ships(screen):
    global background, grid_img, parchment_img, font_h1, font_h2, player1_text, player2_text
    global ships_p1, ships_p2
    global P1, P2, WHO, RUN
    global SIZE

    PICKED = False  # variable for drag and drop

    # grid rects (599 x 599)
    grid_p1 = grid_img.get_rect(center=(439, 359))
    grid_p2 = grid_img.get_rect(center=(1059, 359))

    # parchment rects (122 x 590)
    parchment_p1 = parchment_img.get_rect(center=(71, 365))
    parchment_p2 = parchment_img.get_rect(center=(1428, 365))

    # "validate" text
    validate_text = font_h2.render("Validate", True, "#FFFFFF")

    # validate button rect for player 1
    validate_p1 = pygame.Rect((0, 0), (115, 35))
    validate_p1.center = 650, 680

    # validate button rect for player 2
    validate_p2 = pygame.Rect((0, 0), (115, 35))
    validate_p2.center = 1240, 680

    # game loop
    run = True
    while run:
        # blits background
        screen.blit(background, (0, 0))

        # blits grids and parchment for player 1 and 2
        screen.blit(grid_img, grid_p1)
        screen.blit(grid_img, grid_p2)
        screen.blit(parchment_img, parchment_p1)
        screen.blit(parchment_img, parchment_p2)

        # blits player 1 and player 2 text
        screen.blit(player1_text, (313, 20))
        screen.blit(player2_text, (943, 20))

        # differentiates who's turn it is
        if WHO:
            # blits ships for player 1
            for i in range(5):
                screen.blit(ships_p1[0][i], ships_p1[1][i])

            # blits button to validate
            pygame.draw.rect(screen, "#D74B4B", validate_p1, border_radius=12)
            screen.blit(validate_text, (600, 668))
        else:
            # blits ships for player 1
            for i in range(5):
                screen.blit(ships_p2[0][i], ships_p2[1][i])

            # blits button to validate
            pygame.draw.rect(screen, "#D74B4B", validate_p2, border_radius=12)
            screen.blit(validate_text, (1190, 668))

        # gets mouse position
        pos = pygame.mouse.get_pos()

        # event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # stop this while loop
                run = False
                # prevents other loop to start as pygame.quit() is called just after this while loop
                RUN = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:

                    # to make sure only one ship is picked
                    picked_one = False

                    # checks which ships is clicked and snaps its position to mouse
                    for i in range(5):
                        # for player 1
                        if WHO and ships_p1[1][i].collidepoint(pos) and not picked_one:
                            ships_p1[1][i].center = pos
                            ships_p1[2][i] = True
                            picked_one = True
                        # for player 2
                        elif (
                            not WHO
                            and ships_p2[1][i].collidepoint(pos)
                            and not picked_one
                        ):
                            ships_p2[1][i].center = pos
                            ships_p2[2][i] = True
                            picked_one = True
                    PICKED = True

                    # checks if it's player 1's turn and mouse is on validate button
                    if WHO and validate_p1.collidepoint(pos):
                        valid = validate(ships_p1, grid_p1)
                        if not valid:
                            show_error(screen)
                        else:
                            WHO = False

                    elif not WHO and validate_p2.collidepoint(pos):
                        valid = validate(ships_p2, grid_p2)
                        if not valid:
                            show_error(screen)
                        else:
                            WHO = True
                            run = False

                elif event.button == 3:
                    for i in range(5):
                        if ships_p1[2][i] == True:
                            # rotates image
                            ships_p1[0][i] = pygame.transform.rotate(ships_p1[0][i], 90)
                            # gets position of rect
                            position = ships_p1[1][i].center
                            # sets rect as a new rect of rotated image
                            ships_p1[1][i] = ships_p1[0][i].get_rect()
                            # sets center of new rect
                            ships_p1[1][i].center = position
                            # counts the number of rotation
                            ships_p1[3][i] += 1
                        elif ships_p2[2][i] == True:
                            # rotates image
                            ships_p2[0][i] = pygame.transform.rotate(ships_p2[0][i], 90)
                            # gets position of rect
                            position = ships_p2[1][i].center
                            # sets rect as a new rect of rotated image
                            ships_p2[1][i] = ships_p2[0][i].get_rect()
                            # sets center of new rect
                            ships_p2[1][i].center = position
                            # counts the number of rotation
                            ships_p2[3][i] += 1

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1 and PICKED:
                    for i in range(5):
                        if ships_p1[2][i] == True:
                            ships_p1[2][i] = False
                            # snaps ship in place
                            ships_p1[1][i].center = snap(grid_p1, ships_p1, i)
                        elif ships_p2[2][i] == True:
                            ships_p2[2][i] = False
                            # snaps ships in place
                            ships_p2[1][i].center = snap(grid_p2, ships_p2, i)
                    PICKED = False

            elif event.type == pygame.MOUSEMOTION:
                # checks if a ship is picked
                if PICKED:
                    for i in range(5):
                        if ships_p1[2][i] == True:
                            if pos[0] > (SIZE[0] / 2):
                                ships_p1[1][i].center = (SIZE[0] / 2), pos[1]
                            else:
                                ships_p1[1][i].center = pos
                        elif ships_p2[2][i] == True:
                            if pos[0] < (SIZE[0] / 2):
                                ships_p2[1][i].center = (SIZE[0] / 2), pos[1]
                            else:
                                ships_p2[1][i].center = pos

            elif event.type == pygame.MOUSEWHEEL:
                if event.y != 0:
                    for i in range(5):
                        if ships_p1[2][i] == True:
                            # rotates image
                            ships_p1[0][i] = pygame.transform.rotate(ships_p1[0][i], 90)
                            # gets position of rect
                            position = ships_p1[1][i].center
                            # sets rect as a new rect of rotated image
                            ships_p1[1][i] = ships_p1[0][i].get_rect()
                            # sets center of new rect
                            ships_p1[1][i].center = position
                            # counts the number of rotation
                            ships_p1[3][i] += 1
                        elif ships_p2[2][i] == True:
                            # rotates image
                            ships_p2[0][i] = pygame.transform.rotate(ships_p2[0][i], 90)
                            # gets position of rect
                            position = ships_p2[1][i].center
                            # sets rect as a new rect of rotated image
                            ships_p2[1][i] = ships_p2[0][i].get_rect()
                            # sets center of new rect
                            ships_p2[1][i].center = position
                            # counts the number of rotation
                            ships_p2[3][i] += 1

        pygame.display.update()
    ### NEED TO FIGURE OUT HOW TO QUIT
    if not RUN:
        pygame.quit()


def play_game(screen):
    global background, grid_img, font_h1, font_h2, player1_text, player2_text, circle_img, cross_img
    global ships_p1, ships_p2
    global P1, P2, WHO, RUN
    # global SIZE

    # grid (599 x 599)
    grid_p1 = grid_img.get_rect(center=(309, 359))
    grid_p2 = grid_img.get_rect(center=(1189, 359))

    # torpedo (182 x 58)
    torpedo_img = pygame.image.load("./img/torpedo.png")
    torpedo = torpedo_img.get_rect(center=(750, 359))

    # cirlce and cross img
    circle_img = pygame.image.load("./img/circle.png")
    cross_img = pygame.image.load("./img/cross2.png")

    # blits all the circles and crosses on hits or misses for both players
    show_if_hit(screen)

    # game loop
    run = True
    while run:
        # blits background
        screen.blit(background, (0, 0))

        # blits grids and parchment for player 1
        screen.blit(grid_img, grid_p1)

        # blits grids and parchment for player 2
        screen.blit(grid_img, grid_p2)

        # add player 1 and player 2 text
        screen.blit(player1_text, (183, 20))
        screen.blit(player2_text, (1073, 20))

        # adds torpedo
        screen.blit(torpedo_img, torpedo)

        pos = pygame.mouse.get_pos()

        # event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                RUN = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if WHO and grid_p1.collidepoint(pos):
                        # converts mouse position as coordinates of a matrice
                        coord = mouse_to_coord(pos, grid_p1)
                        update_matrice(coord, P1)
                    elif not WHO and grid_p2.collidepoint(pos):
                        # converts mouse position as coordinates of a matrice
                        coord = mouse_to_coord(pos, grid_p2)
                        update_matrice(coord, P2)

        pygame.display.update()


def snap(grid, ships, id):
    position = ships[1][id].center
    g_x = grid.left
    g_y = grid.top

    # checks for rotation
    rotated = False
    if ships[3][id] % 2 == 1:
        rotated = True

    # checks if middle of ship should be a line
    if id == 0 or id == 3:
        if rotated:
            coord_x = ((position[0] - g_x + 30) // 60) * 60 + g_x
            coord_y = ((position[1] - g_y) // 60) * 60 + g_y + 30
        else:
            coord_x = ((position[0] - g_x) // 60) * 60 + g_x + 30
            coord_y = ((position[1] - g_y + 30) // 60) * 60 + g_y
    # ships whose middle is in the center of a square
    else:
        coord_x = ((position[0] - g_x) // 60) * 60 + g_x + 30
        coord_y = ((position[1] - g_y) // 60) * 60 + g_y + 30
    return (coord_x, coord_y)


def validate(ships, grid):
    global P1, P2, WHO
    valid = True

    """DO I NEED 2 CHECKS OR JUST ONE"""
    # checks if center of ships are on grid
    for i in range(5):
        if not grid.collidepoint(ships[1][i].center):
            valid = False

    # if still valid checks if whole ship on grid
    if valid:
        for i in range(5):
            if ships[1][i].left < grid.left:
                valid = False
            # add + 1 as grid is (599 x 599)
            elif ships[1][i].right > grid.right + 1:
                valid = False
            elif ships[1][i].top < grid.top:
                valid = False
            # add + 1 as grid is (599 x 599)
            elif ships[1][i].bottom > grid.bottom + 1:
                valid = False

    if valid:
        to_mat(ships, grid)
    else:
        print("Not all ships are on the grid")

    # if number of ships < 17 -> ships are on top of each other
    if num_ships() < 17:
        # resets players matrice as blank
        if WHO:
            P1 = [["----" for x in range(10)] for x in range(10)]
        else:
            P2 = [["----" for x in range(10)] for x in range(10)]
        valid = False
        print("Some ships are overlapping")

    return valid


def to_mat(ships, grid):
    global P1, P2, WHO

    # determines which matrice is being changed
    if WHO:
        mat = P1
    else:
        mat = P2

    g_x = grid.left
    g_y = grid.top

    for i in range(5):
        # gets ship center
        x = ships[1][i].center[0]
        y = ships[1][i].center[1]

        # checks if ship was rotated
        rotated = False
        if ships[3][i] % 2 == 1:
            rotated = True

        if i == 0:
            if rotated:
                coord_x = (x - g_x) // 60 - 1
                coord_y = (y - g_y) // 60
                mat[coord_x][coord_y] = "ship"
                mat[coord_x + 1][coord_y] = "ship"
            else:
                coord_x = (x - g_x) // 60
                coord_y = (y - g_y) // 60 - 1
                mat[coord_x][coord_y] = "ship"
                mat[coord_x][coord_y + 1] = "ship"
        elif i == 1 or i == 2:
            coord_x = (x - g_x) // 60
            coord_y = (y - g_y) // 60
            if rotated:
                mat[coord_x - 1][coord_y] = "ship"
                mat[coord_x][coord_y] = "ship"
                mat[coord_x + 1][coord_y] = "ship"
            else:
                mat[coord_x][coord_y - 1] = "ship"
                mat[coord_x][coord_y] = "ship"
                mat[coord_x][coord_y + 1] = "ship"
        elif i == 3:
            if rotated:
                coord_x = (x - g_x) // 60 - 1
                coord_y = (y - g_y) // 60
                # checks if the battleship (4 long) is longer to the right or left
                if (ships_p1[3][3] - 1) % 2 == 0:
                    mat[coord_x - 1][coord_y] = "ship"
                    mat[coord_x][coord_y] = "ship"
                    mat[coord_x + 1][coord_y] = "ship"
                    mat[coord_x + 2][coord_y] = "ship"
                else:
                    mat[coord_x - 2][coord_y] = "ship"
                    mat[coord_x - 1][coord_y] = "ship"
                    mat[coord_x][coord_y] = "ship"
                    mat[coord_x + 1][coord_y] = "ship"
            else:
                coord_x = (x - g_x) // 60
                coord_y = (y - g_y) // 60 - 1
                mat[coord_x][coord_y - 1] = "ship"
                mat[coord_x][coord_y] = "ship"
                mat[coord_x][coord_y + 1] = "ship"
                mat[coord_x][coord_y + 2] = "ship"
        elif i == 4:
            coord_x = (x - g_x) // 60
            coord_y = (y - g_y) // 60
            if rotated:
                mat[coord_x - 2][coord_y] = "ship"
                mat[coord_x - 1][coord_y] = "ship"
                mat[coord_x][coord_y] = "ship"
                mat[coord_x + 1][coord_y] = "ship"
                mat[coord_x + 2][coord_y] = "ship"
            else:
                mat[coord_x][coord_y - 2] = "ship"
                mat[coord_x][coord_y - 1] = "ship"
                mat[coord_x][coord_y] = "ship"
                mat[coord_x][coord_y + 1] = "ship"
                mat[coord_x][coord_y + 2] = "ship"


# prints a matrice
def show_mat(m):
    for i in range(10):
        for j in range(10):
            print(f"{m[j][i]}", end=" ")
        print("\n")
    print("\n")


# counts the number of ships on the respective players grid
def num_ships():
    global P1, P2, WHO

    if WHO:
        mat = P1
    else:
        mat = P2

    counter = 0
    for i in range(10):
        for j in range(10):
            if mat[i][j] == "ship":
                counter += 1
    return counter


# blits error_img centered on the screen 3 times with delay in between
def show_error(screen):
    global error_img, error_img_2, error_img_3, SIZE

    screen.blit(
        error_img,
        (SIZE[0] / 2 - 1000 / 2, SIZE[1] / 2 - 600 / 2),
    )
    pygame.display.update()
    pygame.time.wait(150)

    screen.blit(
        error_img_2,
        (
            SIZE[0] / 2 - (1000 * 1.3) / 2,
            SIZE[1] / 2 - (600 * 1.3) / 2,
        ),
    )
    pygame.display.update()
    pygame.time.wait(150)

    screen.blit(
        error_img_3,
        (
            SIZE[0] / 2 - (1000 * 1.6) / 2,
            SIZE[1] / 2 - (600 * 1.6) / 2,
        ),
    )
    pygame.display.update()
    pygame.time.wait(150)


# returns the matrice coordinates the mouse is on depending on which grid is inputed
def mouse_to_coord(pos, grid):
    g_x = grid.left
    g_y = grid.top

    coord_x = (pos[0] - g_x) // 60
    coord_y = (pos[1] - g_y) // 60

    return (coord_x, coord_y)


# returns the top left of the square on the respective grid
def coord_to_pos(coord, grid_left_top):
    g_x = grid_left_top[0]
    g_y = grid_left_top[1]

    pos_x = coord[0] * 60 + g_x
    pos_y = coord[1] * 60 + g_y

    return (pos_x, pos_y)


# blits all circles (miss) and crosses (hit) on both grids
def show_if_hit(screen):
    global circle_img, cross_img
    global P1, P2
    for i in range(10):
        for j in range(10):
            if P1[i][j] == "hit-":
                screen.blit(cross_img, coord_to_pos((j, i), (10, 60)))
                print("hit")
            elif P1[i][j] == "miss":
                screen.blit(circle_img, coord_to_pos((j, i), (10, 60)))
                print("misss")


# update the players matrice at the coords inputed
def update_matrice(coord, mat):
    coord_x = coord[0]
    coord_y = coord[1]

    value = mat[coord_x][coord_y]
    if value == "ship":
        mat[coord_x][coord_y] = "hit-"
    elif value == "----":
        mat[coord_x][coord_y] = "miss"
    show_mat(mat)


# sets up the display for solo testing
# main menu is supposed to call the init() function when the "Play Against a Friend" button is pressed
def main():
    global SIZE
    pygame.init()

    # screen
    SIZE = 1500, 700
    screen = pygame.display.set_mode(SIZE)

    # title and caption
    pygame.display.set_caption("Battleship")
    icon = pygame.image.load("./img/icon.png")
    pygame.display.set_icon(icon)

    init(screen)


if __name__ == "__main__":
    main()
