import pygame
import os

BLUE  = (25,25,200)
BLACK = (23,23,23 )
WHITE = (254,254,254)
ALPHA = (0,255,0)


class Player(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.movex = 0
        self.movey = 0
        self.frame = 0
        self.images = []
        for i in range(1,5):
            img = pygame.image.load(os.path.join('Slike','avatarright.png')).convert()
            # img.convert_alpha()
            # img.set_colorkey(BLUE)
            self.images.append(img)
            self.image = self.images[0]
            self.rect  = self.image.get_rect()

    def control(self, x, y):
        '''
        control player movement
        '''
        self.movex += x
        self.movey += y

    def update(self):
        '''
        Update sprite position
        '''

        self.rect.x = self.rect.x + self.movex
        self.rect.y = self.rect.y + self.movey

        # #moving left
        # if self.movex < 0:
        #     self.frame += 1
        #     if self.frame > 3*ani:
        #         self.frame = 0
        #     self.image = self.images[self.frame//ani]
        #
        # # moving right
        # if self.movex > 0:
        #     self.frame += 1
        #     if self.frame > 3*ani:
        #         self.frame = 0
        #     self.image = self.images[(self.frame//ani)+4]