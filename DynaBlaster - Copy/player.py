import pygame
import os
from definitions import *

iconSize =40
sirina = 19
visina = 13

class Player(pygame.sprite.Sprite):

    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)
        self.movex = 0
        self.movey = 0
        self.frame = 0
        self.images = []
        self.total_score = 0
        self.kill_points = 10
        self.total_lives = 10
        # score
        self.score_cfg = pygame.font.SysFont('Helvetica', 20, True)
        self.health_cfg = pygame.font.SysFont('Helvetica', 20, True)

        self.imgRight = pygame.image.load(os.path.join('Slike', img)).convert()
        self.imgRight.set_colorkey((255, 255, 255))
        self.imgLeft = pygame.image.load(os.path.join('Slike', 'playerleft.png')).convert()
        self.imgLeft.set_colorkey((255, 255, 255))

        self.direction = self.imgRight
        self.img = self.imgRight
        self.images.append(self.img)
        self.image = self.images[0]
        self.rect = self.direction.get_rect()

        #proba za kretanje
        self.case_x = 1
        self.case_y = 1
        self.x = iconSize * self.case_x  # taille_sprite = 40
        self.y = iconSize * self.case_y

    # score se uvecava kad ubije nekog
    def score_up(self):
        self.total_score += self.kill_points

    # prikaz score
    def show_score(self, world):
        self.score = self.score_cfg.render('Score: ' + str(self.total_score), True, (255, 230, 0))
        world.blit(self.score, (10, 10))

    # smanjenje zivota
    def lives_down(self, world):
        self.total_lives -= 1
        if self.total_lives == 0:
            pygame.quit()

    # prikaz zivota
    def show_lives(self, world):
        self.health = self.health_cfg.render('Lives: ' + str(self.total_lives), True, (255, 230, 0))
        world.blit(self.health, (150, 10))

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

    def update(self, enemy_list, world):
        self.rect.x = self.rect.x + self.movex
        self.rect.y = self.rect.y + self.movey

        # ako se sudari sa neprijateljem
        hit_list = pygame.sprite.spritecollide(self, enemy_list, False)

        if hit_list.__len__() > 0:
            self.rect.x = 50
            self.rect.y = 50
            self.lives_down(world)

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