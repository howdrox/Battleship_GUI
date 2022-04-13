"""play_friend.py: Multiplayer battleship game 1v1"""


import pygame


def loop(screen):
    # background
    background = pygame.image.load("./img/background2.jpg")

    # grid
    grid = pygame.image.load("./img/grid_white.png")

    # parchment
    parchment = pygame.image.load("./img/parchment.png")

    # font
    font = pygame.font.Font("freesansbold.ttf", 32)
    player1_text = font.render("Player 1's board", True, (255, 255, 255))
    player2_text = font.render("Player 2's board", True, (255, 255, 255))

    run = True
    while run:
        # sets background
        screen.blit(background, (0, 0))

        # puts grids and parchment for player 1
        screen.blit(grid, (140, 70))
        screen.blit(parchment, (10, 70))

        # puts grids and parchment for player 2
        screen.blit(grid, (770, 70))
        screen.blit(parchment, (1375, 70))

        # add player 1 and player 2 text
        screen.blit(player1_text, (313, 20))
        screen.blit(player2_text, (943, 20))

        # event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

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


if __name__ == "__main__":
    main()
