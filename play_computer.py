"""play_computer.py: Battleship game against a bot"""


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
    computer_text = font.render("Computer's board", True, (255, 255, 255))

    # ships
    destroyer_img = pygame.image.load("./img/destroyer.png")
    destroyer = destroyer_img.get_rect()
    destroyer.center = 530, 490

    run = True
    while run:
        # sets background
        screen.blit(background, (0, 0))

        # puts grids and parchment for computer
        screen.blit(grid, (140, 70))
        screen.blit(parchment, (10, 70))

        # puts grids and parchment for computer
        screen.blit(grid, (770, 70))
        screen.blit(parchment, (1375, 70))

        # add player 1 and computer text
        screen.blit(player1_text, (313, 20))
        screen.blit(computer_text, (928, 20))

        # show ship
        screen.blit(destroyer_img, destroyer)
        pygame.draw.circle(screen, (0, 255, 0), (530, 490), 7, 0)

        # if mouse on top of rect
        if destroyer.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.circle(screen, (0, 255, 0), (450, 490), 7, 0)

        # event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                destroyer_img = pygame.transform.rotate(destroyer_img, 90)
                position = destroyer.center
                destroyer = destroyer_img.get_rect()
                destroyer.center = position

        pygame.display.update()


# sets up the display for solo testing
# main menu is supposed to call the loop() function when the Play Against Computer button is pressed
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
