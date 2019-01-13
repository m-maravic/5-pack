import pygame
import time
from DynaBlaster import *
from definitions import *
#from StartWindow import *

pygame.init()

def button(text, x, y, width, height, inactive_color, active_color, action=None):
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    # print(click)
    if x + width > cur[0] > x and y + height > cur[1] > y:
        pygame.draw.rect(gameDisplay, active_color, (x, y, width, height))
        if click[0] == 1 and action != None:
            if action == "quit":
                pygame.quit()
                quit()

            if action == "multiplay":#ovde bih stavila multiplay
                game_loop(2)

            if action == "playAgain":
                game_loop(1)

            if action == "menu":
                pass
                #game_intro()

    else:
        pygame.draw.rect(gameDisplay, inactive_color, (x, y, width, height))

    text_to_button(text, black, x, y, width, height)
def game_over():

    game_over = True

    while game_over:
        for event in pygame.event.get():
                #print(event)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

        gameDisplay.fill(white)
        message_to_screen("Game Over",green,-100,size="large")
        message_to_screen("You died.",black,-30)



        button("play Again", 150,400,150,50, green, light_green, action="playAgain")
        button("multiplay", 375,400,100,50, yellow, light_yellow, action="multiplay")
        button("quit", 550,400,100,50, red, light_red, action ="quit")


        pygame.display.update()

        clock.tick(15)

def you_win():

    win = True

    while win:
        for event in pygame.event.get():
                #print(event)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

        gameDisplay.fill(white)
        message_to_screen("You won!",green,-100,size="large")
        message_to_screen("Congratulations!",black,-30)



        button("play Again", 150,500,150,50, green, light_green, action="play")
        button("controls", 350,500,100,50, yellow, light_yellow, action="controls")
        button("quit", 550,500,100,50, red, light_red, action ="quit")


        pygame.display.update()

        clock.tick(15)



