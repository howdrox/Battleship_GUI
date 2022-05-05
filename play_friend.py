"""play_friend.py: Multiplayer battleship game 1v1"""


import pygame

# loads all the necessary things then calls set_ships() to allow the users to position their ships
def init(screen):
    global background, grid_img, parchment_img, font_h1, font_h2, player1_text, player2_text, error_img, error_img_2, error_img_3
    global ships_p1, ships_p2
    global P1, P2, WHO

    P1 = [["----" for x in range(10)] for x in range(10)]
    P2 = [["----" for x in range(10)] for x in range(10)]
    # who's turn it is with True beign player 1
    WHO = True

    # background
    background = pygame.image.load("./img/background2.jpg")

    # grid (599 x 599)
    grid_img = pygame.image.load("./img/grid_white.png")

    # parchment (122 x 590)
    parchment_img = pygame.image.load("./img/parchment.png")

    # ships images
    destroyer_img = pygame.image.load("./img/destroyer.png")
    cruiser_img = pygame.image.load("./img/cruiser.png")
    submarine_img = pygame.image.load("./img/submarine.png")
    battleship_img = pygame.image.load("./img/battleship.png")
    carrier_img = pygame.image.load("./img/carrier.png")

    # error (1000 x 600)
    error_img = pygame.image.load("./img/blue_screen.png")
    error_img_2 = pygame.transform.scale(error_img, (1000 * 1.3, 600 * 1.3))
    error_img_3 = pygame.transform.scale(error_img, (1000 * 1.6, 600 * 1.6))

    # fonts
    font_h1 = pygame.font.Font("freesansbold.ttf", 32)
    font_h2 = pygame.font.Font("freesansbold.ttf", 24)

    # Player 1 and 2 text
    player1_text = font_h1.render("Player 1's board", True, "#FFFFFF")
    player2_text = font_h1.render("Player 2's board", True, "#FFFFFF")

    # ships for palyer 1
    # list of [[ships_img], [ships_rect], [if picked], [number of rotations], [if found]]
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

    # ships for palyer 2
    # list of [[ships_img], [ships_rect], [if picked], [number of rotations], [if found]]
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

    set_ships(screen)


def set_ships(screen):
    global background, grid_img, parchment_img, font_h1, font_h2, player1_text, player2_text, error_img, error_img_2, error_img_3
    global ships_p1, ships_p2
    global P1, P2, WHO
    global SIZE

    PICKED = False  # variable for drag and drop

    # grid (599 x 599)
    grid_p1 = grid_img.get_rect(center=(439, 359))
    grid_p2 = grid_img.get_rect(center=(1069, 359))

    # parchment (122 x 590)
    parchment_p1 = parchment_img.get_rect(center=(71, 365))
    parchment_p2 = parchment_img.get_rect(center=(1436, 365))

    # validate text
    validate_text = font_h2.render("Validate", True, "#FFFFFF")

    # validate button for player 1
    validate_p1 = pygame.Rect((0, 0), (115, 35))
    validate_p1.center = 650, 680

    # validate button for player 2
    validate_p2 = pygame.Rect((0, 0), (115, 35))
    validate_p2.center = 1240, 680

    # game loop
    run = True
    while run:
        # blits background
        screen.blit(background, (0, 0))

        # blits grids and parchment for player 1
        screen.blit(grid_img, grid_p1)
        screen.blit(parchment_img, parchment_p1)

        # blits grids and parchment for player 2
        screen.blit(grid_img, grid_p2)
        screen.blit(parchment_img, parchment_p2)

        # add player 1 and player 2 text
        screen.blit(player1_text, (313, 20))
        screen.blit(player2_text, (943, 20))

        # differentiates the case for player 1 and player 2
        if WHO:
            # adds ships for player 1
            for i in range(5):
                screen.blit(ships_p1[0][i], ships_p1[1][i])

            # button to validate
            pygame.draw.rect(screen, "#D74B4B", validate_p1, border_radius=12)
            screen.blit(validate_text, (600, 668))
        else:
            # adds ships for player 2
            for i in range(5):
                screen.blit(ships_p2[0][i], ships_p2[1][i])

            # button to validate
            pygame.draw.rect(screen, "#D74B4B", validate_p2, border_radius=12)
            screen.blit(validate_text, (1190, 668))

        # gets mouse position
        pos = pygame.mouse.get_pos()

        # event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and not PICKED:
                    # to make sure only one ship is picked
                    picked_one = False
                    # checks if mouse on ship
                    for i in range(5):
                        if ships_p1[1][i].collidepoint(pos) and not picked_one:
                            ships_p1[1][i].center = pos
                            ships_p1[2][i] = True
                            picked_one = True
                    PICKED = True

                    # checks if player 1 turn and  mouse on validate button
                    if WHO and validate_p1.collidepoint(pos):
                        valid = validate(grid_p1, ships_p1)
                        if not valid:
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

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1 and PICKED:
                    for i in range(5):
                        if ships_p1[2][i] == True:
                            ships_p1[2][i] = False
                            # snaps ship in place
                            ships_p1[1][i].center = snap(
                                ships_p1[1][i].center, i, ships_p1[3][i], True
                            )
                    PICKED = False

            elif event.type == pygame.MOUSEMOTION:
                # checks if a ship is picked
                if PICKED:
                    for i in range(5):
                        if ships_p1[2][i] == True:
                            if pos[0] > 750:
                                ships_p1[1][i].center = 750, pos[1]
                            else:
                                ships_p1[1][i].center = pos

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

        pygame.display.update()


def snap(position, ships_id, rotations, player_1):
    # check if on player 1 grid
    if player_1:
        # checks of rotation
        rotated = False
        if rotations % 2 == 1:
            rotated = True
        # checks if middle of ship should be a line
        if ships_id == 0 or ships_id == 3:
            if rotated:
                coord_x = ((position[0] - 110) // 60) * 60 + 140
                coord_y = ((position[1] - 60) // 60) * 60 + 90
            else:
                coord_x = ((position[0] - 140) // 60) * 60 + 170
                coord_y = ((position[1] - 30) // 60) * 60 + 60
        # ships whose middle is in the center of a square
        else:
            coord_x = ((position[0] - 140) // 60) * 60 + 170
            coord_y = ((position[1] - 60) // 60) * 60 + 90
    return (coord_x, coord_y)


def validate(grid, ships):
    valid = True
    # checks center of ships are on grid
    for i in range(5):
        if not grid.collidepoint(ships[1][i].center):
            valid = False

    # if still valid checks if whole ship on grid
    if valid:
        for i in range(5):
            if ships[1][i].left < grid.left:
                valid = False
                print("rigth")
            elif ships[1][i].right > grid.right + 1:
                valid = False
                print("more left")
            elif ships[1][i].top < grid.top:
                valid = False
                print("more down")
            elif ships[1][i].bottom > grid.bottom + 1:
                valid = False
                print("top")

    if valid:
        to_mat(grid, ships)
    else:
        print("Not all ships are on the grid")

    # if number of ships < 17 -> ships are on top of each other
    if num_ships() < 17:
        valid = False
        print("Some ships are overlapping")

    return valid


def to_mat(grid, ships):
    global P1, P2, WHO
    # checks for if player 1
    if WHO:
        for i in range(5):
            x = ships[1][i].center[0]
            y = ships[1][i].center[1]

            g_x = grid.left
            g_y = grid.right

            # checks if ship was rotated
            rotated = False
            if ships[3][i] % 2 == 1:
                rotated = True

            if i == 0:
                if rotated:
                    coord_x = (x - 140) // 60 - 1
                    coord_y = (y - 60) // 60
                    P1[coord_x][coord_y] = "ship"
                    P1[coord_x + 1][coord_y] = "ship"
                else:
                    coord_x = (x - 140) // 60
                    coord_y = (y - 60) // 60 - 1
                    P1[coord_x][coord_y] = "ship"
                    P1[coord_x][coord_y + 1] = "ship"
            elif i == 1 or i == 2:
                coord_x = (x - 140) // 60
                coord_y = (y - 60) // 60
                if rotated:
                    P1[coord_x - 1][coord_y] = "ship"
                    P1[coord_x][coord_y] = "ship"
                    P1[coord_x + 1][coord_y] = "ship"
                else:
                    P1[coord_x][coord_y - 1] = "ship"
                    P1[coord_x][coord_y] = "ship"
                    P1[coord_x][coord_y + 1] = "ship"
            elif i == 3:
                if rotated:
                    coord_x = (x - 140) // 60 - 1
                    coord_y = (y - 60) // 60
                    # checks if ships has 2 parts to the right
                    if (ships_p1[3][3] - 1) % 2 == 0:
                        P1[coord_x - 1][coord_y] = "ship"
                        P1[coord_x][coord_y] = "ship"
                        P1[coord_x + 1][coord_y] = "ship"
                        P1[coord_x + 2][coord_y] = "ship"
                    else:
                        P1[coord_x - 2][coord_y] = "ship"
                        P1[coord_x - 1][coord_y] = "ship"
                        P1[coord_x][coord_y] = "ship"
                        P1[coord_x + 1][coord_y] = "ship"
                else:
                    coord_x = (x - 140) // 60
                    coord_y = (y - 60) // 60 - 1
                    P1[coord_x][coord_y - 1] = "ship"
                    P1[coord_x][coord_y] = "ship"
                    P1[coord_x][coord_y + 1] = "ship"
                    P1[coord_x][coord_y + 2] = "ship"
            elif i == 4:
                coord_x = (x - 140) // 60
                coord_y = (y - 60) // 60
                if rotated:
                    P1[coord_x - 2][coord_y] = "ship"
                    P1[coord_x - 1][coord_y] = "ship"
                    P1[coord_x][coord_y] = "ship"
                    P1[coord_x + 1][coord_y] = "ship"
                    P1[coord_x + 2][coord_y] = "ship"
                else:
                    P1[coord_x][coord_y - 2] = "ship"
                    P1[coord_x][coord_y - 1] = "ship"
                    P1[coord_x][coord_y] = "ship"
                    P1[coord_x][coord_y + 1] = "ship"
                    P1[coord_x][coord_y + 2] = "ship"
    show_mat(P1)


def show_mat(m):
    for i in range(10):
        for j in range(10):
            print(f"{m[j][i]}", end=" ")
        print("\n")
    print("\n")


def num_ships():
    global P1, P2, WHO

    if WHO:
        m = P1
    else:
        m = P2
    counter = 0
    for i in range(10):
        for j in range(10):
            if m[i][j] == "ship":
                counter += 1
    return counter


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
    pygame.quit()


if __name__ == "__main__":
    main()
