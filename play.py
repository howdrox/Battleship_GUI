"""Contains funcitons for the playing phase of the game."""


import pygame

# import bot.py file
import bot


def init(screen, against_computer, size, audio):
    """
    Loads all the necessary data then calls the different functions for the different phases of the game.

    Only loads things needed for all phases of the game

    Parameters:
        screen (Surface): Surface to blit to.
        against_computer (bool): If playing against computer.
        size (width, height): Window size.
        audio (path, volume, position): Audio settings.

    Returns:
        still_running (bool): If window was closed.
    """

    # images and fonts
    global background, grid_img, parchment_img, font_h1, font_h2, player1_text, player2_text, error_img, error_img_2, error_img_3, cursor
    # ships variables
    global ships_p1, ships_p2
    # game variables
    global p1, p2, who, gameover, computer, SIZE, AUDIO, FPS, still_running, clock

    # empty player 1 and player 2 matrix
    p1 = [["----" for x in range(10)] for x in range(10)]
    p2 = [["----" for x in range(10)] for x in range(10)]
    # who's turn it is with True being player 1
    who = True
    # global variable if pygame should be running
    still_running = True
    # if someone won
    gameover = False
    # if against computer
    computer = against_computer
    # sets a clock
    clock = pygame.time.Clock()
    # screen size
    SIZE = size
    # audio settings from main menu
    AUDIO = audio
    # frames per second
    FPS = 80

    # background image
    background = pygame.image.load("./img/background2.jpg")

    # grid image (599 x 599)
    grid_img = pygame.image.load("./img/grid_white.png")

    # parchment image (122 x 563)
    parchment_img = pygame.image.load("./img/parchment.png")

    # ships images
    destroyer_img = pygame.image.load("./img/destroyer.png")
    cruiser_img = pygame.image.load("./img/cruiser.png")
    submarine_img = pygame.image.load("./img/submarine.png")
    battleship_img = pygame.image.load("./img/battleship.png")
    carrier_img = pygame.image.load("./img/carrier.png")

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

    # cursor
    cursor = pygame.image.load("img//cursor.png")

    # continues to play same music at same position and volume
    pygame.mixer.music.load(AUDIO[0])
    pygame.mixer.music.set_volume(AUDIO[1])
    # sets music to play indefinitely
    pygame.mixer.music.play(-1)
    # sets position of song to where it was before play.init() funciton was called
    pygame.mixer.music.set_pos(AUDIO[2] / 1000)

    # ship data for palyer 1
    # list of [[ships_img], [ships_rect], [if_picked], [number_of_rotations]]
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
    ]

    # ship data for palyer 2
    # list of [[ships_img], [ships_rect], [if_picked], [number_of_rotations]]
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
    ]

    set_ships(screen)
    # checks if the window was closed, if not then continue
    if still_running:
        play_game(screen)

    return still_running


def set_ships(screen):
    """
    The game loop to set up ships

    Parameters:
        screen (Surface)
    """

    # screen variables
    global background, grid_img, parchment_img, font_h1, font_h2, player1_text, player2_text, cursor
    # ship data
    global ships_p1, ships_p2
    # game data
    global p1, p2, who, computer, SIZE, FPS, still_running, clock

    # variable for drag and drop
    PICKED = False

    # grid rects (599 x 599)
    grid_p1 = grid_img.get_rect(center=(439, 359))
    grid_p2 = grid_img.get_rect(center=(1059, 359))

    # parchment rects (122 x 563)
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
        # gets mouse position
        pos = pygame.mouse.get_pos()

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
        if who:
            # blits ships for player 1
            for i in range(5):
                screen.blit(ships_p1[0][i], ships_p1[1][i])

            # blits button to validate
            pygame.draw.rect(screen, "#D74B4B", validate_p1, border_radius=12)
            screen.blit(validate_text, (600, 668))
        # if its player 2's turn and not against a computer
        elif not computer and not who:
            # blits ships for player 2
            for i in range(5):
                screen.blit(ships_p2[0][i], ships_p2[1][i])

            # blits button to validate
            pygame.draw.rect(screen, "#D74B4B", validate_p2, border_radius=12)
            screen.blit(validate_text, (1190, 668))

        # blit cursor last as it should be on top of everything
        screen.blit(cursor, pos)

        # event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # stop this while loop
                run = False
                # prevents other loop to start as pygame.quit() is called just after this while loop
                still_running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:

                # left button
                if event.button == 1:
                    if not PICKED:
                        # to make sure only one ship is picked
                        picked_one = False

                        # checks which ships is clicked and snaps its position to mouse
                        for i in range(5):
                            # for player 1
                            if (
                                who
                                and ships_p1[1][i].collidepoint(pos)
                                and not picked_one
                            ):
                                ships_p1[1][i].center = pos
                                ships_p1[2][i] = True
                                picked_one = True
                                PICKED = True
                            # for player 2
                            elif (
                                not who
                                and ships_p2[1][i].collidepoint(pos)
                                and not picked_one
                            ):
                                ships_p2[1][i].center = pos
                                ships_p2[2][i] = True
                                picked_one = True
                                PICKED = True

                    # checks if it's player 1's turn and mouse is on validate button
                    if who and validate_p1.collidepoint(pos):
                        valid = validate(ships_p1, grid_p1)
                        if not valid:
                            show_error(screen)
                        else:
                            if not computer:
                                who = False
                            else:
                                p2 = bot.set_ships()
                                # stops the phase of setting up ships
                                run = False

                    elif not who and validate_p2.collidepoint(pos) and not computer:
                        valid = validate(ships_p2, grid_p2)
                        if not valid:
                            show_error(screen)
                        else:
                            who = True
                            run = False

                # right button
                elif event.button == 3:
                    rotate_ship(ships_p1, ships_p2)

            elif event.type == pygame.MOUSEBUTTONUP:
                # if right button
                if event.button == 1:
                    if PICKED:
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
                # checks if mousewheel was scrolled
                if event.y != 0:
                    rotate_ship(ships_p1, ships_p2)

        pygame.display.update()
        # sets FPS
        clock.tick(FPS)

    # if window was closed stops pygame
    if not still_running:
        pygame.quit()


def play_game(screen):
    """
    The game loop to attack the other player.

    Parameters:
        screen (Surface)
    """

    # screen variables
    global background, grid_img, font_h1, font_h2, player1_text, player2_text, circle_img, cross_img, torpedo_img, torpedo, click_to, cursor
    # ship data
    global ships_p1, ships_p2
    # game data
    global p1, p2, who, still_running, gameover, FPS, clock
    # audio
    global explosion_audio

    # grid (599 x 599)
    grid_p1 = grid_img.get_rect(center=(309, 359))
    grid_p2 = grid_img.get_rect(center=(1189, 359))

    # torpedo (182 x 58)
    torpedo_img = pygame.image.load("./img/torpedo.png")
    torpedo = torpedo_img.get_rect(center=(750, 359))

    # cirlce and cross img (50 x 50)
    circle_img = pygame.image.load("./img/circle.png")
    cross_img = pygame.image.load("./img/cross.png")

    # click to continue text
    click_to = font_h1.render("Click to return to main menu.", True, "#FFFFFF")

    # explosion sound
    explosion_audio = pygame.mixer.Sound("./audio/explosion.mp3")

    # game loop
    run = True
    while run:
        pos = pygame.mouse.get_pos()

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
        show_torpedo(screen)

        # blits all the circles and crosses on hits or misses for both players
        show_if_hit(screen, grid_p1, grid_p2)

        # shows who won
        if gameover:
            show_winner(screen, grid_p1, grid_p2)

        # blit cursor last as it should be on top of everything
        screen.blit(cursor, pos)

        # event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                # prevents other pygame functions to be called as pygame.quit() is called just after this while loop
                still_running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if gameover:
                        run = False

                    # to store if mouse on a grid
                    on_grid = False
                    # to store if computer should play or not
                    computer_plays = False

                    if who and grid_p1.collidepoint(pos) and not gameover:
                        grid = grid_p1
                        mat = p2
                        on_grid = True
                    elif (
                        not who
                        and grid_p2.collidepoint(pos)
                        and not computer
                        and not gameover
                    ):
                        grid = grid_p2
                        mat = p1
                        on_grid = True

                    if on_grid:
                        # converts mouse position as coordinates of a matrix
                        coord = mouse_to_coord(pos, grid)
                        updated = update_matrix(coord, mat)
                        if updated:
                            # checks if against computer and tells it to play
                            if who and computer:
                                computer_plays = True

                            if if_won():
                                gameover = True
                            else:
                                # changes the player's turn
                                who = not who
                        else:
                            show_error(screen)

                        # checks if computer should play
                        # need to rewrite code as this part is only triggered if mouse button is pressed and we want the computer to play directly after player 1
                        if computer_plays:
                            coord = bot.guess(p1)
                            update_matrix(coord, p1)
                            if if_won():
                                gameover = True
                            else:
                                who = not who

        pygame.display.update()
        # sets FPS
        clock.tick(FPS)

    # if window was closed
    if not still_running:
        pygame.quit()


def snap(grid, ships, id):
    """
    Snaps ship in place.

    Parameters:
        grid (Rect): Rect of grid.
        ships (list): Ship data.
        id (int): Ship id.

    Returns:
        coord_x, coord_y (int, int) : Postion of ship's center.
    """

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
    """
    Validates if all ships are on grid.

    Parameters:
        ships (list): Ship data.
        grid (Rect): Rect of grid.

    Returns:
        valid (bool)
    """

    global p1, p2, who
    valid = True

    # runs through all the ships and checks if it is contained in grid
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

    # if still valid, adds ships position to matrix
    if valid:
        to_mat(ships, grid)

        if who:
            mat = p1
        else:
            mat = p2

        # if number of ships < 17 -> ships are on top of each other
        if num_of("ship", mat) < 17:
            # resets players matrix as blank
            if who:
                p1 = [["----" for x in range(10)] for x in range(10)]
            else:
                p2 = [["----" for x in range(10)] for x in range(10)]
            valid = False
            print("Some ships are overlapping")
    else:
        print("Not all ships are on the grid")

    return valid


def to_mat(ships, grid):
    """
    Takes all ships position and converts them to matrix coordinates.

    Parameters:
        ships (list): Ship data.
        grid (Rect): Rect of grid.
    """

    global p1, p2, who

    # determines which matrix is being changed
    if who:
        mat = p1
    else:
        mat = p2

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

        # for destroyer (2 long)
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
        # for cruiser and submarine (3 long)
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
        # for battleship (4 long)
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
        # for carrier (5 long)
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


def num_of(a, mat):
    """
    Counts the number of `a` in `mat`.

    Parameters:
        a (str): Object.
        mat (list[list[str]]): Matrix.

    Returns:
        counter (int)
    """

    counter = 0
    for i in range(10):
        for j in range(10):
            if mat[i][j] == a:
                counter += 1
    return counter


def show_error(screen):
    """
    Shows an error has occured.

    Blits `error_img` centered on the screen 3 times with delay in between.

    Parameters:
        screen (Surface): Screen to blit to.
    """

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


# rotates the image of the ship which is being picked
def rotate_ship(ships_p1, ships_p2):
    """
    Rotates the image and Rect of the ship which is being picked up

    Parameters:
        ships_p1 (list): Player 1's ship data.
        ships_p2 (list): Player 2's ship data.
    """

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
            # adds one to the ships number of rotation
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
            # adds one to the ships number of rotation
            ships_p2[3][i] += 1


def mouse_to_coord(pos, grid):
    """
    Converts mouse position to matrix coordinates depending on which `grid`.

    Parameters:
        pos (tuple[int, int]): Mouse position.
        grid (Rect): Rect of grid.

    Returns:
        (coord_x, coord_y) (tuple[int, int]): Matrix coordinates.
    """

    g_x = grid.left
    g_y = grid.top

    coord_x = (pos[0] - g_x) // 60
    coord_y = (pos[1] - g_y) // 60

    return (coord_x, coord_y)


def coord_to_pos(coord, grid_left_top):
    """
    Converts matrix coordinates to a position on the screen.

    Parameters:
        coord (tuple[int, int]): Matrix coord.
        grid_left_top (tuple[int, int]): Grid's left and top position.

    Returns:
        (pos_x, pos_y) (tuple[int, int]): The position of the topleft of the square (plus some margin to center the img) on the respective grid.
    """

    global circle_img, cross_img
    g_x = grid_left_top[0]
    g_y = grid_left_top[1]

    pos_x = coord[0] * 60 + g_x + ((60 - circle_img.get_width()) / 2)
    pos_y = coord[1] * 60 + g_y + ((60 - circle_img.get_height()) / 2)

    return (pos_x, pos_y)


def show_if_hit(screen, grid_p1, grid_p2):
    """
    Blits all circles (miss) and crosses (hit) on both grids.

    Parameters:
        screen (Surface): Surface to blit to.
        grid_p1 (Rect): Player 1's grid Rect.
        grid_p2 (Rect): Player 2's grid Rect.
    """

    global circle_img, cross_img
    global p1, p2
    for i in range(10):
        for j in range(10):
            if p1[i][j] == "hit-":
                screen.blit(
                    cross_img, coord_to_pos((i, j), (grid_p2.left, grid_p2.top))
                )
            elif p1[i][j] == "miss":
                screen.blit(
                    circle_img, coord_to_pos((i, j), (grid_p2.left, grid_p2.top))
                )
            if p2[i][j] == "hit-":
                screen.blit(
                    cross_img, coord_to_pos((i, j), (grid_p1.left, grid_p1.top))
                )
            elif p2[i][j] == "miss":
                screen.blit(
                    circle_img, coord_to_pos((i, j), (grid_p1.left, grid_p1.top))
                )


def show_torpedo(screen):
    """
    Blits a torpedo on `screen` to show who's turn it is

    Parameters:
        screen (Surface): Surface to blit to.
    """

    global torpedo_img, torpedo
    global who

    if who:
        image = torpedo_img
    else:
        image = pygame.transform.rotate(torpedo_img, 180)

    screen.blit(image, torpedo)


def update_matrix(coord, mat):
    """
    Updates `mat` at `coord`.

    The other player attacked you at `coord`

    Parameters:
        coord (tuple[int, int])
        mat (list[list[str]])

    Returns:
        result (bool): if `coord` was valid (player has not tried to attack there before).
    """

    global explosion_audio
    result = True
    coord_x = coord[0]
    coord_y = coord[1]

    value = mat[coord_x][coord_y]
    if value == "ship":
        mat[coord_x][coord_y] = "hit-"
        # play sound
        explosion_audio.play()
    elif value == "----":
        mat[coord_x][coord_y] = "miss"
    else:
        result = False

    return result


def if_won():
    """
    Checks if someone won.

    Returns:
        won (bool): If won.
    """

    global p1, p2, who
    won = False

    if who:
        hits = num_of("hit-", p2)
    else:
        hits = num_of("hit-", p1)

    # if number of hits is 17 then game finished
    if hits == 17:
        won = True

    return won


def show_winner(screen, grid_p1, grid_p2):
    """
    Blits end screen winner displayed.

    Parameters:
        screen (Surface): Surface to blit to.
        grid_p1 (Rect): Player 1's grid Rect.
        grid_p2 (Rect): Player 2's grid Rect.
    """

    global who, gameover, click_to

    # translucent banner
    banner = pygame.Surface((1500, 200))
    banner.set_alpha(128)
    banner.fill("#000000")

    # won image (180 x 180)
    win = pygame.image.load("./img/win.png")

    # KO image (398 x 180)
    ko = pygame.image.load("./img/KO.png")

    if who:
        grid_winner = grid_p1
        grid_loser = grid_p2
    else:
        grid_winner = grid_p2
        grid_loser = grid_p1

    screen.blit(banner, (0, 360 - (200 / 2)))
    screen.blit(
        ko,
        (
            grid_loser.center[0] - ko.get_width() / 2,
            grid_loser.center[1] - ko.get_height() / 2,
        ),
    )
    screen.blit(
        win,
        (
            grid_winner.center[0] - win.get_width() / 2,
            grid_winner.center[1] - win.get_height() / 2,
        ),
    )
    screen.blit(click_to, (750 - click_to.get_width() / 2, 460 - click_to.get_height()))


def show_mat(m):
    """
    Prints a matrix

    Debug function, not used in the code.

    Parameters:
        m (list[list[str]])
    """

    for i in range(10):
        for j in range(10):
            print(f"{m[j][i]}", end=" ")
        print("\n")
    print("\n")


def main():
    """
    Initialises pygame for solo testing.

    Debug function, not used in the code.
    Used when the main menu was not yet set up.
    """
    pygame.init()

    # screen
    size = 1500, 700
    screen = pygame.display.set_mode(size)

    # title and caption
    pygame.display.set_caption("Battleship")
    icon = pygame.image.load("./img/icon.png")
    pygame.display.set_icon(icon)

    # sets cursor to false
    pygame.mouse.set_visible(False)

    init(screen, True, size, ("./audio/0.mp3", 0.05, 0))


if __name__ == "__main__":
    main()
