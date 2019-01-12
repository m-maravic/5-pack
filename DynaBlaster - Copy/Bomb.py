import pygame
import os
import time
from definitions import*

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

    def explode(self, screen, deWalls_list, bomberman, no, enemy_list):
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

        #ako je zid u opsegu eksplozije
        for wall in deWalls_list:
            if wall.rect.x == self.rect.x-iconSize and wall.rect.y == self.rect.y:
                deWalls_list.remove(wall)
                wallsPositions[round((self.rect.x-iconSize)/iconSize)][round(self.rect.y/iconSize)] = 0
            if wall.rect.x == self.rect.x+iconSize and wall.rect.y == self.rect.y:
                deWalls_list.remove(wall)
                wallsPositions[round((self.rect.x+iconSize)/iconSize)][round(self.rect.y/iconSize)] = 0
            if wall.rect.x == self.rect.x and wall.rect.y == self.rect.y+iconSize:
                deWalls_list.remove(wall)
                wallsPositions[round(self.rect.x/iconSize)][round((self.rect.y+iconSize)/iconSize)] = 0
            if wall.rect.x == self.rect.x and wall.rect.y == self.rect.y - iconSize:
                deWalls_list.remove(wall)
                wallsPositions[round(self.rect.x/iconSize)][round((self.rect.y-iconSize)/iconSize)] = 0

        deWalls_list.draw(screen)


        # ako je igrac u opsegu eksplozije
        if bomberman.x == self.rect.x - iconSize and bomberman.y == self.rect.y:
            bomberman.lives_down(screen, no)
        elif bomberman.x == self.rect.x + iconSize and bomberman.y == self.rect.y:
            bomberman.lives_down(screen, no)
        elif bomberman.x == self.rect.x and bomberman.y == self.rect.y + iconSize:
            bomberman.lives_down(screen, no)
        elif bomberman.x == self.rect.x and bomberman.y == self.rect.y - iconSize:
            bomberman.lives_down(screen, no)
        elif bomberman.x == self.rect.x and bomberman.y == self.rect.y:
            bomberman.lives_down(screen, no)

        # ako je neprijatelj u opsegu eksplozije
        for e in enemy_list:
            if e.rect.x == self.rect.x - iconSize and e.rect.y == self.rect.y:
                enemy_list.remove(e)
                bomberman.score_up()
            elif e.rect.x == self.rect.x + iconSize and e.rect.y == self.rect.y:
                enemy_list.remove(e)
                bomberman.score_up()
            elif e.rect.x == self.rect.x and e.rect.y == self.rect.y + iconSize:
                enemy_list.remove(e)
                bomberman.score_up()
            elif e.rect.x == self.rect.x and e.rect.y == self.rect.y - iconSize:
                enemy_list.remove(e)
                bomberman.score_up()
            elif e.rect.x == self.rect.x and e.rect.y == self.rect.y:
                enemy_list.remove(e)
                bomberman.score_up()

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
