"""settings.py: Settings menu"""


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

        # event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        pygame.display.update()


# sets up the display for solo testing
# main menu is supposed to call the loop() function when the Settings button is pressed
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
