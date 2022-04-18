"""play_friend.py: Multiplayer battleship game 1v1"""


import pygame


def loop(screen):
    PICKED = False  # variable for drag and drop

    # background
    background = pygame.image.load("./img/background2.jpg")

    # grids (599 x 599)
    grid_img = pygame.image.load("./img/grid_white.png")

    grid_p1 = grid_img.get_rect()
    grid_p1.center = 440, 370

    grid_p2 = grid_img.get_rect()
    grid_p2.center = 1070, 370

    # parchments (122 x 590)
    parchment_img = pygame.image.load("./img/parchment.png")

    parchment_p1 = parchment_img.get_rect()
    parchment_p1.center = 71, 365

    parchment_p2 = parchment_img.get_rect()
    parchment_p2.center = 1436, 365

    # font
    font = pygame.font.Font("freesansbold.ttf", 32)
    player1_text = font.render("Player 1's board", True, (255, 255, 255))
    player2_text = font.render("Player 2's board", True, (255, 255, 255))

    # ships images
    destroyer_img = pygame.image.load("./img/destroyer.png")
    cruiser_img = pygame.image.load("./img/cruiser.png")
    submarine_img = pygame.image.load("./img/submarine.png")
    battleship_img = pygame.image.load("./img/battleship.png")
    carrier_img = pygame.image.load("./img/carrier.png")

    # ships for palyer 1
    # list of [[ships_img], [ships_rect], [if picked], [number of rotations]]
    ships_p1 = [
        [
            destroyer_img,
            cruiser_img,
            submarine_img,
            battleship_img,
            carrier_img,
        ],
        [
            destroyer_img.get_rect(),
            cruiser_img.get_rect(),
            submarine_img.get_rect(),
            battleship_img.get_rect(),
            carrier_img.get_rect(),
        ],
        [False, False, False, False, False],
        [0, 0, 0, 0, 0],
    ]
    # initial 10 px between each ship
    ships_p1[1][0].center = 41, 150
    ships_p1[1][1].center = 41, 310
    ships_p1[1][2].center = 41, 500
    ships_p1[1][3].center = 93, 210
    ships_p1[1][4].center = 93, 490

    # ships for palyer 2
    # initial 10 px between each ship
    ships_p2 = [
        destroyer_img.get_rect(),
        cruiser_img.get_rect(),
        submarine_img.get_rect(),
        battleship_img.get_rect(),
        carrier_img.get_rect(),
    ]
    ships_p2[0].center = 1406, 150
    ships_p2[1].center = 1406, 310
    ships_p2[2].center = 1406, 500
    ships_p2[3].center = 1458, 210
    ships_p2[4].center = 1458, 490

    # game loop
    run = True
    while run:
        # sets background
        screen.blit(background, (0, 0))

        # puts grids and parchment for player 1
        screen.blit(grid_img, grid_p1)
        screen.blit(parchment_img, parchment_p1)

        # puts grids and parchment for player 2
        screen.blit(grid_img, grid_p2)
        screen.blit(parchment_img, parchment_p2)

        # add player 1 and player 2 text
        screen.blit(player1_text, (313, 20))
        screen.blit(player2_text, (943, 20))

        # adds ships for player 1
        for i in range(5):
            screen.blit(ships_p1[0][i], ships_p1[1][i])

        # adds ships for player 2
        screen.blit(destroyer_img, ships_p2[0])
        screen.blit(cruiser_img, ships_p2[1])
        screen.blit(submarine_img, ships_p2[2])
        screen.blit(battleship_img, ships_p2[3])
        screen.blit(carrier_img, ships_p2[4])

        pygame.draw.circle(screen, (0, 255, 0), (380, 310), 7, 0)

        # gets mouse position
        pos = pygame.mouse.get_pos()

        # checks if the ships is being moved
        if PICKED:
            for i in range(5):
                if ships_p1[2][i] == True:
                    ships_p1[1][i].center = pos

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
                            pygame.transform.rotate(ships_p1[0][i], 90)
                    PICKED = True

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1 and PICKED:
                    for i in range(5):
                        if ships_p1[2][i] == True:
                            ships_p1[2][i] = False
                    PICKED = False

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
