import pygame
import os
import time

imgSize = 40

class Bomb(pygame.sprite.Sprite):

    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)
        self.movex = 0
        self.movey = 0
        self.images = []

        self.bombImage = pygame.image.load(os.path.join('Slike', img)).convert()
        self.bombImage.set_colorkey((255, 255, 255))

        self.images.append(self.bombImage)
        self.image = self.images[0]
        self.rect = self.bombImage.get_rect()

    #self.timeToExplode=3000


    #self.image=pygame.image.load(os.path.join('Slike','bonb.png')).convert()

    #explosion
        # time.sleep(3)
        #
        # self.image=pygame.image.load(os.path.join('Slike','explodstart.png')).convert()
        # self.rect=self.image.get_rect()
        #
        # self.x=x
        # self.y=y-imgSize
        #
        # self.imageUp=pygame.imageUp.load(os.path.join('Slike','exploh.png'))
        # self.rect=self.imageUp.get_rect()
        #
        # self.x = x
        # self.y = y + imgSize
        # self.imageDown=pygame.imageDown.load(os.path.join('Slike','explob.png'))
        # self.rect = self.imageDown.get_rect()
        # self.x = x-imgSize
        # self.y = y
        # self.imageLeft=pygame.imageLeft.load(os.path.join('Slike','explog.png'))
        # self.rect = self.imageLeft.get_rect()
        # self.x = x + imgSize
        # self.y = y
        #
        # self.imageRight=pygame.imageRight.load(os.path.join('Slike','explod.png'))
        # self.rect = self.imageRight.get_rect()

#after explosion, destruction of walls
    def explosion(self,matrix,x,y,imgSize,world):
        if(matrix[x][y-imgSize]==0|matrix[x][y-imgSize]==2):
           world.blit(x,y-imgSize)#nisam siguran da li moze ovo ovako da se izcrta
        if(matrix[x][y+imgSize]==0|matrix[x][y-imgSize]==2):
            world.blit(x,y+imgSize)
        if (matrix[x-imgSize][y] == 0|matrix[x][y-imgSize]==2):
            world.blit(x-imgSize, y)
        if (matrix[x+imgSize][y] == 0|matrix[x][y-imgSize]==2):
            world.blit(x+imgSize, y )
        if (matrix[x][y] == 0):
            world.blit(x, y)

