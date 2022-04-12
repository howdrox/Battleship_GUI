import pygame


def main():
    # Initialisation
    pygame.init()

    # Afficher le logo
    logo = pygame.image.load("img\\icon.png")
    pygame.display.set_icon(logo)

    # Titre de la fenêtre
    pygame.display.set_caption("Battleship")

    # Création de l'écran
    size = 1500, 700
    screen = pygame.display.set_mode(size)

    # Images
    background = pygame.image.load("img\\background.jpg")
    cursor = pygame.image.load("img\\cursor.png")
    cursor = pygame.transform.scale(cursor, (20, 20))

    # Affichage d'images
    screen.blit(background, (0, 0))

    # Condition
    running = True

    # Ne pas afficher le curseur
    pygame.mouse.set_visible(False)

    # Boucle principale
    while running:
        # Actualisation continue de l'écran:
        pygame.display.flip()

        # On prend tout ce qui se passe sur l'écran
        for event in pygame.event.get():
            if event.type == pygame.MOUSEMOTION:
                screen.blit(background, (0, 0))
                screen.blit(cursor, event.pos)

            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False


# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__ == "__main__":
    # call the main function
    main()
