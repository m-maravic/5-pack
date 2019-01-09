import pygame
import os
import time

iconSize = 40

class Bomb(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join('Slike', 'bonb.png')).convert()
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        # vezano za eksploziju
        self.timeToExplode = 3000
        self.bombRange = 5

    def update(self, dt):
        # Subtract the passed time `dt` from the timer each frame.
        self.timeToExplode -= dt

    def explode(self, screen):
        self.image = pygame.image.load(os.path.join('Slike', 'explodeStart.png')).convert()
        self.image.set_colorkey((255, 255, 255))
        self.imageLeft = pygame.image.load(os.path.join('Slike', 'explodeLeft.png')).convert()
        self.imageLeft.set_colorkey((255, 255, 255))
        self.imageRight = pygame.image.load(os.path.join('Slike', 'explodeRight.png')).convert()
        self.imageRight.set_colorkey((255, 255, 255))
        self.imageUp = pygame.image.load(os.path.join('Slike', 'explodeUp.png')).convert()
        self.imageUp.set_colorkey((255, 255, 255))
        self.imageDown = pygame.image.load(os.path.join('Slike', 'explodeDown.png')).convert()
        self.imageDown.set_colorkey((255, 255, 255))

        screen.blit(self.image, (self.rect.x, self.rect.y))
        screen.blit(self.imageLeft, (self.rect.x - iconSize, self.rect.y))
        screen.blit(self.imageRight, (self.rect.x + iconSize, self.rect.y))
        screen.blit(self.imageUp, (self.rect.x , self.rect.y - iconSize))
        screen.blit(self.imageDown, (self.rect.x , self.rect.y + iconSize))

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
