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

    def __init__(self,img):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join('Slike',img))
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()

        self.direction = self.set_random_direction()

        free_spots = find_free_spot() # lista slobodnih pozicija u matrici
        index = random.randint(0, len(free_spots)-1) # uzimamo random index iz liste slobodnih pozicija

        self.rect.x = free_spots[index].x*iconSize # mesta iz matrice koja su slobodna pozicioniramo na odgovarajuce piksele
        self.rect.y = free_spots[index].y*iconSize
        self.counter = 0  # counter variable

    def set_random_direction(self):
        start_direction = random.randint(1, 4)
        if start_direction == 1:
            return 'r'
        elif start_direction == 2:
            return 'l'
        elif start_direction == 3:
            return 'u'
        elif start_direction == 4:
            return 'd'


    def update(self):
        self.rect.x = self.rect.x + self.movex
        self.rect.y = self.rect.y + self.movey

    def move(self):
        #distance = 80
        speed = 1

        current_x = math.floor(self.rect.x / iconSize)
        current_y = math.floor(self.rect.y / iconSize)

        # ono deljenje ispod nije radilo kada pozicija nije deljiva sa 40 (npr. 79/40 neprijatelj tretira kao 1 u matrici)
        # ovaj if omogucava da se mapiranje sa piksela na matricu ispod desava samo za korektne slucajeve
        if self.rect.x%iconSize != 0 or self.rect.y%iconSize != 0:
            if self.direction == 'r':
                self.rect.x += speed
            if self.direction == 'l':
                self.rect.x -= speed
            if self.direction == 'd':
                self.rect.y -= speed
            if self.direction == 'u':
                self.rect.y += speed
            return

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
