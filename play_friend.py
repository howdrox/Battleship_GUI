"""play_friend.py: Multiplayer battleship game 1v1"""


from re import sub
import pygame


def loop(screen):
    # variables for drag and drop
    picked = False

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
    ships_img = {
        "destroyer": destroyer_img,
        "cruiser": cruiser_img,
        "submarine": submarine_img,
        "battleship": battleship_img,
        "carrier": carrier_img,
    }

    # ships for palyer 1
    # initial 10 px between each ship
    ships_p1 = {
        "destroyer": [destroyer_img.get_rect(), False],
        "cruiser": [cruiser_img.get_rect(), False],
        "submarine": [submarine_img.get_rect(), False],
        "battleship": [battleship_img.get_rect(), False],
        "carrier": [carrier_img.get_rect(), False],
    }
    ships_p1["destroyer"][0].center = 41, 150
    ships_p1["cruiser"][0].center = 41, 310
    ships_p1["submarine"][0].center = 41, 500
    ships_p1["battleship"][0].center = 93, 210
    ships_p1["carrier"][0].center = 93, 490

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
        screen.blit(ships_img["destroyer"], ships_p1["destroyer"][0])
        screen.blit(ships_img["cruiser"], ships_p1["cruiser"][0])
        screen.blit(ships_img["submarine"], ships_p1["submarine"][0])
        screen.blit(ships_img["battleship"], ships_p1["battleship"][0])
        screen.blit(ships_img["carrier"], ships_p1["carrier"][0])

        # adds ships for player 2
        screen.blit(destroyer_img, ships_p2[0])
        screen.blit(cruiser_img, ships_p2[1])
        screen.blit(submarine_img, ships_p2[2])
        screen.blit(battleship_img, ships_p2[3])
        screen.blit(carrier_img, ships_p2[4])

        # gets mouse position
        pos = pygame.mouse.get_pos()

        # checks if the ships is being moved
        if picked:
            for ship in ships_p1:
                if ships_p1[ship][1] == True:
                    ships_p1[ship][0].center = pos

        # event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if not picked:
                    # to make sure only one ship is picked
                    pick_one = True
                    # checks if mouse on ship
                    for ship in ships_p1:
                        if ships_p1[ship][0].collidepoint(pos) and pick_one:
                            ships_p1[ship][0].center = pos
                            ships_p1[ship][1] = True
                            pick_one = False
                    picked = True

            if event.type == pygame.MOUSEBUTTONUP:
                if picked:
                    for ship in ships_p1:
                        if ships_p1[ship][1] == True:
                            ships_p1[ship][1] = False
                    picked = False

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
