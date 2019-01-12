import os
import pygame
from definitions import *
import math

BLUE  = (25,25,200)
BLACK = (23,23,23 )
WHITE = (254,254,254)
ALPHA = (0,255,0)

worldx = 760
worldy = 520
iconSize = 40

class Enemy(pygame.sprite.Sprite):
    '''
    Spawn an enemy
    '''
    def __init__(self,x,y,img):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join('Slike',img))
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        self.direction = 'r'

        free_spots = find_free_spot() # lista slobodnih pozicija u matrici
        index = random.randint(0, len(free_spots)-1) # uzimamo random index iz liste slobodnih pozicija

        self.rect.x = free_spots[index].x*iconSize # mesta iz matrice koja su slobodna pozicioniramo na odgovarajuce piksele
        self.rect.y = free_spots[index].y*iconSize
        self.counter = 0  # counter variable

    # def move(self):
    #     distance = 80
    #     speed = 1
    #
    #     if self.rect.x < iconSize:
    #         self.rect.x += speed
    #         self.counter = 80
    #     elif self.rect.x > worldx-iconSize*2:
    #         self.rect.x -= speed
    #         self.counter = 80
    #     else:
    #         if self.counter >= 0 and self.counter <= distance:
    #             self.rect.x += speed
    #         elif self.counter >= distance and self.counter <= distance * 2:
    #             self.rect.x -= speed
    #         else:
    #             self.counter = 0
    #
    #     self.counter += 1


    def update(self):

        self.rect.x = self.rect.x + self.movex
        self.rect.y = self.rect.y + self.movey

    def move(self):
        #distance = 80
        speed = 1

        current_x = math.floor(self.rect.x / iconSize)
        current_y = math.floor(self.rect.y / iconSize)

        if wallsPositions[current_x + 1][current_y] == 0 and self.direction == 'r': # dal moze DESNO
            self.rect.x += speed
        elif wallsPositions[current_x + 1][current_y] != 0 and self.direction == 'r':
            self.direction = 'l'

        if wallsPositions[current_x - 1][current_y] == 0 and self.direction == 'l': # LEVO
            self.rect.x -= speed
        elif wallsPositions[current_x - 1][current_y] != 0 and self.direction == 'l':
            self.direction = 'u'

        if wallsPositions[current_x][current_y + 1] == 0 and self.direction == 'u': # GORE
            self.rect.y += speed
        elif wallsPositions[current_x][current_y + 1] != 0 and self.direction == 'u':
            self.direction = 'd'

        if wallsPositions[current_x][current_y - 1] == 0 and self.direction == 'd': # DOLE
            self.rect.y -= speed
        elif wallsPositions[current_x][current_y - 1] != 0 and self.direction == 'd': # DOLE
            self.direction = 'r'
