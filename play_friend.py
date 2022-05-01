"""play_friend.py: Multiplayer battleship game 1v1"""


import pygame

# loads all the necessary things then calls set_ships() to allow the users to position their ships
# then calls
def loop(screen):
    global background, grid_img, parchment_img, font_h1, font_h2, player1_text, player2_text, validate_text
    global ships_p1
    global P1, P2

    P1 = [[[""] for x in range(10)] for x in range(10)]
    P2 = []

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

    # fonts
    font_h1 = pygame.font.Font("freesansbold.ttf", 32)
    font_h2 = pygame.font.Font("freesansbold.ttf", 24)

    # Player 1 and 2 text
    player1_text = font_h1.render("Player 1's board", True, "#FFFFFF")
    player2_text = font_h1.render("Player 2's board", True, "#FFFFFF")

    # validate text
    validate_text = font_h2.render("Validate", True, "#FFFFFF")

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

    # ships_p2[0].center = 1406, 150
    # ships_p2[1].center = 1406, 310
    # ships_p2[2].center = 1406, 500
    # ships_p2[3].center = 1458, 210
    # ships_p2[4].center = 1458, 490

    set_ships(screen)


def set_ships(screen):
    global background, grid_img, parchment_img, font_h1, font_h2, player1_text, player2_text, validate_text
    global ships_p1
    global P1, P2

    PICKED = False  # variable for drag and drop

    # grid (599 x 599)
    grid_p1 = grid_img.get_rect(center=(440, 360))
    grid_p2 = grid_img.get_rect(center=(1070, 370))

    # parchment (122 x 590)
    parchment_p1 = parchment_img.get_rect(center=(71, 365))
    parchment_p2 = parchment_img.get_rect(center=(1436, 365))

    # validate button for player 1
    validate_p1 = pygame.Rect((0, 0), (115, 35))
    validate_p1.center = 650, 680

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

        # button to validate
        pygame.draw.rect(screen, "#D74B4B", validate_p1, border_radius=12)
        screen.blit(validate_text, (600, 668))

        # adds ships for player 1
        for i in range(5):
            screen.blit(ships_p1[0][i], ships_p1[1][i])

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

                    # checks if mouse on button
                    if validate_p1.collidepoint(pos):
                        validate(grid_p1, ships_p1)
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
                coord_x = ((position[0] - 140) // 60) * 60 + 140
                coord_y = ((position[1] - 60) // 60) * 60 + 90
            else:
                coord_x = ((position[0] - 140) // 60) * 60 + 170
                coord_y = ((position[1] - 60) // 60) * 60 + 60
        # ships whose middle is in the center of a square
        else:
            coord_x = ((position[0] - 140) // 60) * 60 + 170
            coord_y = ((position[1] - 60) // 60) * 60 + 90
    return (coord_x, coord_y)


def validate(grid, ships):
    valid = True
    # checks ships are on grid
    for i in range(5):
        if not grid.collidepoint(ships[1][i].center):
            valid = False

    if valid:
        for i in range(5):
            to_grid(grid, ships)
    else:
        print("Not all ships are on the grid")

    # if number of ships less than 17 -> error


def to_grid(grid, ships):
    global P1, P2
    # checks for if player 1
    if grid.center == (440, 360):
        for i in range(5):
            x = ships[1][i].center[0]
            y = ships[1][i].center[1]

            # checks if ship was rotated
            rotated = False
            if ships[3][i] % 2 == 1:
                rotated = True

            # checks for destroyer
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
            elif i == 1:
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


# sets up the display for solo testing
# main menu is supposed to call the loop() function when the Play Against a Friend button is pressed
def main():
    pygame.init()

    # screen
    size = 1500, 700
    screen = pygame.display.set_mode(size)

    # title and caption
    pygame.display.set_caption("Battleship")
    icon = pygame.image.load("./img/icon.png")
    pygame.display.set_icon(icon)

    loop(screen)
    pygame.quit()


if __name__ == "__main__":
    main()
