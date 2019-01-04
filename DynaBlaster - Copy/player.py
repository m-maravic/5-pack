import pygame
import os



class Player(pygame.sprite.Sprite):

    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)
        self.movex = 0
        self.movey = 0
        self.frame = 0
        self.images = []

        # dodato
        self.frame = 0
        self.health = 10
        #########

        self.imgRight = pygame.image.load(os.path.join('Slike', img)).convert()
        self.imgRight.set_colorkey((255, 255, 255))
        self.imgLeft = pygame.image.load(os.path.join('Slike', 'playerleft.png')).convert()
        self.imgLeft.set_colorkey((255, 255, 255))

        self.direction = self.imgRight
        self.img = self.imgRight
        self.images.append(self.img)
        self.image = self.images[0]
        self.rect = self.direction.get_rect()

    def control(self, x, y, dir):
        if (dir == "l"):
            self.movex += x
            self.movey += y
            self.direction = self.imgLeft
        elif (dir == "r"):
            self.movex += x
            self.movey += y
            self.direction = self.imgRight
        else:
            self.movex += x
            self.movey += y

    def update(self, enemy_list):
        self.rect.x = self.rect.x + self.movex
        self.rect.y = self.rect.y + self.movey

        # ako se sudari sa neprijateljem
        hit_list = pygame.sprite.spritecollide(self, enemy_list, False)
        for enemy in hit_list:
            self.health -= 1
            print(self.health)

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