import pygame
import os
import time
from definitions import*


class Gifts(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(os.path.join('Slike','heart.PNG')).convert()
        self.image.set_colorkey((255,255,255))
        self.rect = self.image.get_rect()
        #kada da se pojavi
        self.TimeToAppear=random.randint(5,90)*100
        self.provera=True#da bi samo jednom radilo force
        #self.TimeToStop=10000
        free_spots = find_free_spot()  # lista slobodnih pozicija u matrici
        index = random.randint(0, len(free_spots) - 1)  # uzimamo random index iz liste slobodnih pozicija

        self.rect.x = free_spots[index].x * iconSize  # mesta iz matrice koja su slobodna pozicioniramo na odgovarajuce piksele
        self.rect.y = free_spots[index].y * iconSize


    def update(self, dt):
        self.TimeToAppear-= dt
        print(self.TimeToAppear)
    def draw(self, world):

        world.blit(self.image, (self.rect.x, self.rect.y))

    def force(self,world,bomberman,no):
            m=int(random.randint(1,2))#random bi rad izmedju da li da uvecava ili smanjuje zivote

            if bomberman.x == self.rect.x and bomberman.y == self.rect.y:

                if m==1:
                    bomberman.lives_up(world, no)
                    self.provera = False  #da bi se uklonila clicica tek kad igrac pokupi

                if m==2:
                    bomberman.lives_down(world, no)
                    self.provera = False

            bomberman.show_lives(world,1)



    def poziv(self, world, bomberman, dt, no):
        if self.TimeToAppear <= 0:#kada vreme istekne iscrtaj(kad vreme jednom istekne non stop ce ovo ovde prolaziti)
            self.force(world, bomberman, no)




