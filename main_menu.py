import pygame

def main():
     
    # Initialisation
    pygame.init()
    
    # Afficher le logo
    logo = pygame.image.load("H:\\test_pygame\\data\\logo.png")
    pygame.display.set_icon(logo)

    # Titre de la fenêtre
    pygame.display.set_caption("La bataille navale super cool de KUSNO & WOJTUSCISZYN & SAMAIN.")
     
    # Création de l'écran
    screen = pygame.display.set_mode((1700,720))

    #image
    background = pygame.image.load("H:\\test_pygame\\data\\background.jpg")
    win = pygame.image.load("H:\\test_pygame\\data\\win.png")

    screen.blit(background, (0, 0))

    # define a variable to control the main loop
    running = True
     
    # main loop
    while running:
        pygame.display.flip()
        # event handling, gets all event from the event queue
        for event in pygame.event.get():

            print(event)
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
     
     
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__ == "__main__":
    # call the main function
    main()