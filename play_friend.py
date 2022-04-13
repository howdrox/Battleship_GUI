"""play_friend.py: Multiplayer battleship game 1v1"""


import pygame


def loop(screen):
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

        # event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

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
