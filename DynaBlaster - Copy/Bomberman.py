import pygame
import os
from definitions import *

iconSize =40
sirina = 19
visina = 13

class Bomberman(pygame.sprite.Sprite):
    def __init__(self):
        self.image = pygame.image.load(os.path.join('Slike', 'playerup.png')).convert()
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()

        self.total_score = 0
        self.kill_points = 10
        self.total_lives = 10
        # score
        self.score_cfg = pygame.font.SysFont('Helvetica', 20, True)
        self.health_cfg = pygame.font.SysFont('Helvetica', 20, True)

        self.case_x = 1
        self.case_y = 1
        self.x = iconSize * self.case_x
        self.y = iconSize * self.case_y


    def move(self, direction, enemy_list, world):
        if direction == "r":
            if self.case_x < (sirina - 1):
                if wallsPositions[self.case_x+1][self.case_y] == 0:
                    self.case_x += 1
                    self.x = self.case_x * iconSize

        if direction == "l":
            if self.case_x > 0:
                if wallsPositions[self.case_x-1][self.case_y] == 0:
                    self.case_x -= 1
                    self.x = self.case_x * iconSize

        if direction == "d":
            if self.case_y > 0:
                if wallsPositions[self.case_x][self.case_y-1] == 0:
                    self.case_y -= 1
                    self.y = self.case_y * iconSize

        if direction == "u":
            if self.case_y < (visina - 1):
                if wallsPositions[self.case_x][self.case_y+1] == 0:
                    self.case_y += 1
                    self.y = self.case_y * iconSize


    def update(self, enemy_list, world):
        # ako se sudari sa neprijateljem
        hit_list = pygame.sprite.spritecollide(self, enemy_list, False)

        if hit_list.__len__() > 0:
            self.rect.x = 50
            self.rect.y = 50
            self.lives_down(world)


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

