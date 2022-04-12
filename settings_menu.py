"""settings.py: Settings menu"""


import pygame


def show_img(surface):

    some = pygame.image.load("./img/background.jpg")

    run = True
    while run:
        surface.blit(some, (0, 0))

        # event handler
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False

        pygame.display.update()
