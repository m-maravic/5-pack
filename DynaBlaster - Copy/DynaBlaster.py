import sys
import pygame
import time
from Enemy import *
import random
from StaticWall import *
from DestroyableWall import *
import array
from definitions import *
import random
from Bomb import *
from Bomberman import *
from Timer import *
import threading


def game_loop(playersNo):  #prosledjujemo broj igraca koji ucestvuju 1 ili 2
    fps = 40  # frame rate
    clock = pygame.time.Clock()
    pygame.init()
    pygame.display.set_caption('Dyna Blaster')

    ok = True;
    world = pygame.display.set_mode([worldx, worldy])
    backdrop = pygame.image.load(os.path.join('Slike', 'background.jpg')).convert()
    backdropbox = world.get_rect()


    bomberman = Bomberman(img,1,1)
    if playersNo == 2:
        bomberman2 = Bomberman(img2,17,11)

    enemy_flag = True;

    stWalls_list = pygame.sprite.Group()  # create static walls group
    deWalls_list = pygame.sprite.Group()  # create destroyableWalls group

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

    for x in range(iconSize, worldx - iconSize, iconSize):
        for y in range(iconSize, worldy - iconSize, iconSize):
            if (bool(random.getrandbits(1))):
                if (wallsPositions[round(x / iconSize)][round(y / iconSize)] == 0):  # ako je prazno polje
                    if ((x != 40 and x != 80) and (y != 40 and y != 80)):  # samo radi testiranja posle cemo izmeniti
                        if x!= worldx-iconSize*2 and y!= worldy-iconSize*2:
                            deWall = DestroyableWall(x, y)
                            deWalls_list.add(deWall)
                            wallsPositions[round(deWall.rect.x / iconSize)][round(deWall.rect.y / iconSize)] = 2  # za unistive zidove

    # ovaj randint krece od 50 da se ne bi preklapali sa ispisom za SCORE
    enemy1 = Enemy(random.randint(1, 19) * iconSize, random.randint(1, 13) * iconSize, 'enemy1.png')  # spawn enemy
    #enemy2 = Enemy(random.randint(1, 19) * iconSize, random.randint(1, 13) * iconSize, 'enemy2.png')  # spawn enemy
    enemy_list = pygame.sprite.Group()  # create enemy group
    enemy_list.add(enemy1)  # add enemy to group
    #enemy_list.add(enemy2)  # add enemy to group

    # test
    bomb_list = pygame.sprite.Group()  # create bomb list

    if playersNo == 2:
        bomb_list2 = pygame.sprite.Group()

    t=Timer()
    while ok:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit();
                sys.exit()
                ok = False
            # Get the passed time since last clock.tick call.
            dt = clock.tick(30)

            #prvi igrac
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL:
                    bomb = Bomb(bomberman.x, bomberman.y)
                    bomb_list.add(bomb)  # add bomb to group
                if event.key == ord('a'):
                    bomberman.move('l', enemy_list, world)
                elif event.key == ord('d'):
                    bomberman.move('r', enemy_list, world)
                elif event.key == ord('w'):
                    bomberman.move('u', enemy_list, world)
                elif event.key == ord('s'):
                    bomberman.move('d', enemy_list, world)

                #drugi igrac
                if playersNo == 2:
                    if event.key == pygame.K_LEFT:
                        bomberman2.move('l', enemy_list, world)
                    elif event.key == pygame.K_RIGHT:
                        bomberman2.move('r', enemy_list, world)
                    elif event.key == pygame.K_DOWN:
                        bomberman2.move('d', enemy_list, world)
                    elif event.key == pygame.K_UP:
                        bomberman2.move('u', enemy_list, world)
                    elif event.key == pygame.K_SPACE:
                        bomb2 = Bomb(bomberman2.x, bomberman2.y)
                        bomb_list2.add(bomb2)  # add bomb to group


                if event.key == ord('q'):
                    pygame.quit()
                    sys.exit()
                    ok = False

        #    world.fill(BLACK)
        world.blit(backdrop, backdropbox)
        # grass_list.draw(world)
        stWalls_list.draw(world)
        deWalls_list.draw(world)

        bomb_list.draw(world)
        if playersNo == 2:
            bomb_list2.draw(world)

        # Game logic.
        to_remove = pygame.sprite.Group()

        gameOver1 = 0
        gameOver2 = 0

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
                gameOver1 = bomb.explode(world, deWalls_list, bomberman, 1)

        #bombe drugog igraca
        if playersNo == 2:
            for bomb2 in bomb_list2:
                bomb2.update(dt)
                # Add old bombs to the to_remove set.
                if bomb2.timeToExplode <= -3000:
                    bomb_list2.remove(bomb2)
            for bomb2 in bomb_list2:
                bomb2.draw(world)
                # I'm just drawing the explosion lines each
                # frame when the time is below 0.
                if bomb2.timeToExplode <= 0:
                    gameOver2 = bomb2.explode(world, deWalls_list, bomberman2, 2)

        bomberman.show_score(world, 1)
        bomberman.show_lives(world, 1)
        if playersNo == 2:
            bomberman2.show_score(world, 2)
            bomberman2.show_lives(world, 2)

        threads = []
        enemy_list.draw(world)  # refresh enemies
        #if enemy_flag == True:
        for e in enemy_list:
            tr = threading.Thread(target=e.move())
            threads.append(tr)
            tr.start()
           # enemy_flag = False

        world.blit(bomberman.image, (bomberman.x, bomberman.y))
        if playersNo == 2:
            world.blit(bomberman2.image, (bomberman2.x, bomberman2.y))

        bomberman.rect.x = bomberman.x
        bomberman.rect.y = bomberman.y

        hit_list = pygame.sprite.spritecollide(bomberman, enemy_list, False)

        if hit_list.__len__() > 0:
            bomberman.lives_down(world, 1)

        t.tik_tack(world)
        pygame.display.flip()
        clock.tick(fps)

        if gameOver1 == 1 or gameOver2 == 1:
            game_over()



    # if __name__ == '__main__':
    #     app = QApplication(sys.argv)
    #     ex = ViewWindow()
    #     sys.exit(app.exec_())
