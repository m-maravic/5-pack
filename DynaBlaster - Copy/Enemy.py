import os
import pygame

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
        self.rect.x = x
        self.rect.y = y
        self.counter = 0  # counter variable

    def move(self):
        '''
        enemy movement
        '''
        distance = 80
        speed = 1

        if self.rect.x < iconSize:
            self.rect.x += speed
            self.counter = 80
        elif self.rect.x > worldx-iconSize*2:
            self.rect.x -= speed
            self.counter = 80
        else:
            if self.counter >= 0 and self.counter <= distance:
                self.rect.x += speed
            elif self.counter >= distance and self.counter <= distance * 2:
                self.rect.x -= speed
            else:
                self.counter = 0

        self.counter += 1


    def update(self):
        '''
        Update sprite position
        '''

        self.rect.x = self.rect.x + self.movex
        self.rect.y = self.rect.y + self.movey