"""settings.py: Settings menu"""


import pygame


def loop(screen):
    # background
    background = pygame.image.load("./img/background2.jpg")

    run = True
    while run:
        # sets background
        screen.blit(background, (0, 0))

        # event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

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
    pygame.quit()


if __name__ == "__main__":
    main()
