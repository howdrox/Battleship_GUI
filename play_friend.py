"""play_1v1.py: Multiplayer battleship game 1v1"""

import pygame

size = width, height = (1700, 690)

screen = pygame.display.set_mode(size)
background = pygame.image.load("./im./background.png")


run = True
while run:

    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()