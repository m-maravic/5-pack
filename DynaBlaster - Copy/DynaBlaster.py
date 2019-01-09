import sys
import pygame
import time
from player import *
from Enemy import *
import random
from StaticWall import *
from DestroyableWall import *
import array
from definitions import *
import random
from Bomb import *
from Bomberman import *
from GreenSurface import *

def game_loop():
    fps = 40  # frame rate
    clock = pygame.time.Clock()
    pygame.init()
    pygame.display.set_caption('Dyna Blaster')

    ok = True;
    world = pygame.display.set_mode([worldx, worldy])
    backdrop = pygame.image.load(os.path.join('Slike', 'background.jpg')).convert()
    backdropbox = world.get_rect()

    # player = Player('playerup.png')  # spawn player
    # player.rect.x = iconSize
    # player.rect.y = iconSize
    # player_list = pygame.sprite.Group()
    # player_list.add(player)
    # steps = 10 # how fast to move

    bomberman = Bomberman()

    # ovaj randint krece od 50 da se ne bi preklapali sa ispisom za SCORE
    enemy1 = Enemy(680, random.randint(iconSize, worldy-2*iconSize), 'enemy1.png')  # spawn enemy
    enemy2 = Enemy(random.randint(iconSize, worldx-iconSize*2), random.randint(iconSize, worldy-2*iconSize), 'enemy2.png')  # spawn enemy
    enemy_list = pygame.sprite.Group()  # create enemy group
    enemy_list.add(enemy1)  # add enemy to group
    enemy_list.add(enemy2)  # add enemy to group

    stWalls_list = pygame.sprite.Group()  # create static walls group
    deWalls_list = pygame.sprite.Group()  # create destroyableWalls group
    grass_list = pygame.sprite.Group()

    # trava
    # for x in range(iconSize, worldx - iconSize, iconSize):
    #     for y in range(iconSize, worldy - iconSize, iconSize):
    #         if (wallsPositions[round(x / iconSize)][round(y / iconSize)] == 0):  # ako je prazno polje
    #             grass = GreenSurface(x, y)
    #             wallsPositions[round(grass.rect.x / iconSize)][round(grass.rect.y / iconSize)] = 3  # nema zida
    #             grass_list.add(grass)

    # iscrtavanje okolnih zidova kroz naredne 2 for petlje
    for x in range(0, worldx, iconSize):
        stWall1 = StaticWall(x, 0)
        stWall2 = StaticWall(x, worldy - iconSize)
        stWalls_list.add(stWall1)
        stWalls_list.add(stWall2)
        wallsPositions[round(stWall1.rect.x / iconSize)][0] = 1
        wallsPositions[round(stWall2.rect.x / iconSize)][round(stWall2.rect.y/iconSize)] = 1
    for y in range(iconSize, worldy, iconSize):
        stWall3 = StaticWall(0, y)
        stWall4 = StaticWall(worldx - iconSize, y)
        stWalls_list.add(stWall3)
        stWalls_list.add(stWall4)
        wallsPositions[0][round(stWall3.rect.y / iconSize)] = 1
        wallsPositions[round(stWall4.rect.x/iconSize)][round(stWall4.rect.y / iconSize)] = 1

    # iscrtavanje unutrasnjih zidova
    for x in range(iconSize * 2, worldx - iconSize * 2, iconSize * 2):
        for y in range(iconSize * 2, worldy - iconSize * 2, iconSize * 2):
            stWall = StaticWall(x, y)
            wallsPositions[round(stWall.rect.x / iconSize)][round(stWall.rect.y / iconSize)] = 1
            stWalls_list.add(stWall)

    # unistivi zidovi
    # for x in range(0,20):
    #     a = random.randint(1,18)
    #     b = random.randint(1,12)
    #     if (wallsPositions[a][b] == 0):
    #         deWall = DestroyableWall(a*iconSize, b*iconSize)
    #         deWalls_list.add(deWall)
    #         wallsPositions[a][b] = 2

    for x in range(iconSize, worldx - iconSize, iconSize):
        for y in range(iconSize, worldy - iconSize, iconSize):
            if (bool(random.getrandbits(1))):
                if (wallsPositions[round(x / iconSize)][round(y / iconSize)] == 0):  # ako je prazno polje
                    if ((x != 40 and x != 80) and (y != 40 and y != 80)):  # samo radi testiranja posle cemo izmeniti
                        deWall = DestroyableWall(x, y)
                        deWalls_list.add(deWall)
                        wallsPositions[round(deWall.rect.x / iconSize)][round(deWall.rect.y / iconSize)] = 2  # za unistive zidove

    # test
    print(wallsPositions)

    bomb_list = pygame.sprite.Group()  # create bomb list

    while ok:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit();
                sys.exit()
                ok = False
            # Get the passed time since last clock.tick call.
            dt = clock.tick(30)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bomb = Bomb('bonb.png')
                    bomb.rect.x = player.rect.x
                    bomb.rect.y = player.rect.y
                    bomb_list.add(bomb)  # add bomb to group
                if event.key == ord('a'):
                    bomberman.move('r', enemy_list, world)
                elif event.key == ord('d'):
                    bomberman.move('l', enemy_list, world)
                elif event.key == ord('w'):
                    bomberman.move('d', enemy_list, world)
                elif event.key == ord('s'):
                    bomberman.move('u', enemy_list, world)

                if event.key == ord('q'):
                    pygame.quit()
                    sys.exit()
                    ok = False

        #    world.fill(BLACK)
        world.blit(backdrop, backdropbox)
        # grass_list.draw(world)
        stWalls_list.draw(world)
        deWalls_list.draw(world)

        world.blit(bomberman.image, (bomberman.x, bomberman.y))

        # Game logic.
        to_remove = pygame.sprite.Group()

        # Update bombs. Pass the `dt` to the bomb instances.
        for bomb in bomb_list:
            bomb.update(dt)
            # Add old bombs to the to_remove set.
            if bomb.timeToExplode <= -3000:
                bomb_list.remove(bomb)

        for bomb in bomb_list:
            bomb.draw(world)
            # I'm just drawing the explosion lines each
            # frame when the time is below 0.
            if bomb.timeToExplode <= 0:
                bomb.explode(world)


        # player.update(enemy_list, world)
        # player_list.draw(world)  # refresh player position

        bomb_list.draw(world)
        bomberman.show_score(world)
        bomberman.show_lives(world)
        # player.show_score(world)
        # player.show_lives(world)

        enemy_list.draw(world)  # refresh enemies
        for e in enemy_list:
            e.move()

        pygame.display.flip()
        clock.tick(fps)


    # if __name__ == '__main__':
    #     app = QApplication(sys.argv)
    #     ex = ViewWindow()
    #     sys.exit(app.exec_())
