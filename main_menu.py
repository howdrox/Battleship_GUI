import pygame
import time
from pygame import mixer




def main():
    # Initialisation
    pygame.init()

    volume = 0.01
    mixer.init()
    mixer.music.load("music//0.mp3")
    indice_music = 0
    mixer.music.set_volume(volume)
    mixer.music.play()
    


    # Afficher le logo
    logo = pygame.image.load(".//img//icon.png")
    pygame.display.set_icon(logo)

    # Titre de la fenêtre
    pygame.display.set_caption("Battleship")

    # Création de l'écran
    size = (1500, 800)
    screen = pygame.display.set_mode(size)

    # Images
    background = pygame.image.load("img//background.jpg")
    background = pygame.transform.scale(background, size)
    background_rect = background.get_rect()
    
    #Boutons & curseur
    cursor = pygame.image.load("img//cursor.png")
    cursor = pygame.transform.scale(cursor, (30,30))

    play_button = pygame.image.load("img//start.png")
    play_button = pygame.transform.scale(play_button, (200,100))
    play_rect = play_button.get_rect()
    
    option_button = pygame.image.load("img//option.png")
    option_button = pygame.transform.scale(option_button, (200,50))
    option_rect = option_button.get_rect()
    
    exit_button = pygame.image.load("img//exit_button.png")
    exit_button = pygame.transform.scale(exit_button, (200,75))
    exit_rect = exit_button.get_rect()

    computer_button = pygame.image.load("img//computer.png")
    computer_button = pygame.transform.scale(computer_button, (100,100))
    computer_rect = computer_button.get_rect()

    versus_button = pygame.image.load("img//versus.png")
    versus_button = pygame.transform.scale(versus_button, (200,125))
    versus_rect = versus_button.get_rect()

    return_button = pygame.image.load("img//return.png")
    return_button = pygame.transform.scale(return_button, (70,75))
    return_rect = return_button.get_rect()

    plus_button = pygame.image.load("img//plus_button.png")
    plus_button = pygame.transform.scale(plus_button, (70,70))
    plus_rect = plus_button.get_rect()

    minus_button = pygame.image.load("img//minus_button.png")
    minus_button = pygame.transform.scale(minus_button, (70,20))
    minus_rect = minus_button.get_rect()

    mute = pygame.image.load("img//mute.png")
    mute = pygame.transform.scale(mute, (50,50))
    mute_rect = mute.get_rect()

    unmute = pygame.image.load("img//unmute.png")
    unmute = pygame.transform.scale(unmute, (50,50))
    unmute_rect = unmute.get_rect()

    switch = pygame.image.load("img//switch.png")
    switch = pygame.transform.scale(switch, (70,70))
    switch_rect = switch.get_rect()


    mix = ["music//0.mp3", "music//1.mp3", "music//2.mp3", "music//3.mp3", "music//4.mp3", "music//5.mp3"]


    empty = pygame.image.load("img//empty_.png")
    empty = pygame.transform.scale(empty, size)
    empty_rect = empty.get_rect()

    #useful variables
    play_button_pressed = False
    option_button_pressed = False
    mute_action = False
    clicked = False
    running = True
    option_fait = False

    # Ne pas afficher le curseur
    pygame.mouse.set_visible(False)

    # Boucle principale
    while running:
        screen.blit(background, (0, 0))
        empty_rect.topleft = (0, 0)

        if not(pygame.mixer.music.get_busy()) and not(mute_action):
            mixer.music.load(mix[indice_music])
            mixer.music.play()
        
        mixer.music.set_volume(volume)
        mouse_positions = pygame.mouse.get_pos()
        time.sleep(1/120)

        # Events & actions
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False



            """if event.type == pygame.KEYDOWN:
                print("lo")
                effect = pygame.mixer.Sound("music//oo.mp3")
                effect.play()
            """
        #BUTTONS
            #PLAY BUTTON--------------------------------------------------------------------------------------------------
            if play_rect.collidepoint(mouse_positions) and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                print("Play button pressed")
                play_button_pressed = True
                option_button_pressed = False

            if not play_button_pressed:
                #rect
                play_rect.topleft = ((size[0]//2)-70, (size[1]//2)-150)
            else:
                #rect
                play_rect.topleft = ((2000, 2000))
                versus_rect.topleft = ((size[0]//2)+130, (size[1]//2)-70)
                computer_rect.topleft = ((size[0]//2)-220, (size[1]//2)-50)
                return_rect.topleft = ((0, (size[1])-100))

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if versus_rect.collidepoint(mouse_positions): #échappatoire
                        print("versus battle")

                    if computer_rect.collidepoint(mouse_positions): #échappatoire
                        print("computer battle")





#---------------OPTION BUTTON----------------------------------------------------------------------------------------------------------
            if option_rect.collidepoint(mouse_positions) and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                print("Option button pressed")
                option_button_pressed = True
                play_button_pressed = False
            if not option_button_pressed:
                #rect
                option_rect.topleft = ((size[0]//2)-70, (size[1]//2)-50)
            else:
                #rect
                plus_rect.topleft = ((size[0]//2)+130, (size[1]//2)-10)
                minus_rect.topleft = ((size[0]//2)-150, (size[1]//2)-10)
                switch_rect.topleft = ((size[0]//2), (size[1]//2))
                return_rect.topleft = ((0, (size[1])-100))
                mute_rect.topleft = (size[0]-100, 0)
                #Adaptation du volume
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if plus_rect.collidepoint(mouse_positions):
                        print("increase volume")
                        volume += 0.005

                    if minus_rect.collidepoint(mouse_positions):
                        print("decrease volume")
                        volume -= 0.005

                #Mute button
                if mute_rect.collidepoint(mouse_positions):
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not(mute_action):
                        mute_action = True
                        print("muting")
                    elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and mute_action:
                        mute_action = False
                        print("unmuting")

                if mute_action or volume == 0 :
                    mixer.music.pause()
                else:
                    mixer.music.unpause()


                #Switch music:
                if switch_rect.collidepoint(mouse_positions) and  event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    print("music: ", indice_music)
                    indice_music += 1
                    if indice_music >= len(mix):
                        indice_music = 0
                        mixer.music.load(mix[indice_music])
                        mixer.music.play()
                    else:
                        mixer.music.load(mix[indice_music])
                        mixer.music.play()
                    
            







            if return_rect.collidepoint(mouse_positions) and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                print("return pressed")
                play_button_pressed = False
                option_button_pressed = False

            if exit_rect.collidepoint(mouse_positions) and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                print("je baise la daronne a paul")
                running = False
        




         # Blits -----------------------------------------------------------------------------
        exit_rect.topleft = ((size[0]//2)-70, (size[1]//2)+100)
        screen.blit(exit_button, ((size[0]//2)-70, (size[1]//2)+100))

        if not(play_button_pressed):
            screen.blit(play_button, ((size[0]//2)-70, (size[1]//2)-150))
        else:
                screen.blit(return_button, ((0, (size[1])-100)))
                screen.blit(versus_button, ((size[0]//2)+130, (size[1]//2)-70))
                screen.blit(computer_button, ((size[0]//2)-220, (size[1]//2)-50))
        
        if not(option_button_pressed):
            screen.blit(option_button, ((size[0]//2)-70, (size[1]//2)-50))
        else:
            screen.blit(return_button, ((0, (size[1])-100)))
            screen.blit(plus_button, ((size[0]//2)+130, (size[1]//2)-10))
            screen.blit(minus_button, ((size[0]//2)-150, (size[1]//2)+10))
            screen.blit(switch, ((size[0]//2), (size[1]//2)))
            if mute_action:
                screen.blit(mute,(size[0]-100, 0))
            else:
                screen.blit(unmute,(size[0]-100, 0))

    
        screen.blit(cursor, pygame.mouse.get_pos())
        # Actualisation les changements à l'écran:
        pygame.display.update()


# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__ == "__main__":
    # call the main function
    main()
