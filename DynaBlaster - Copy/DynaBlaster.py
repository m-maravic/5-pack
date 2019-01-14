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
from Gifts import *
import threading
from wall import *

play = True

level_cfg = pygame.font.SysFont('Helvetica', 20, True)


def game_loop(playersNo):  #prosledjujemo broj igraca koji ucestvuju 1 ili 2
    fps = 40  # frame rate
    clock = pygame.time.Clock()
    pygame.init()
    pygame.display.set_caption('Dyna Blaster')


    world = pygame.display.set_mode([worldx, worldy])
    backdrop = pygame.image.load(os.path.join('Slike', 'background.jpg')).convert()
    backdropbox = world.get_rect()

    level = 1
    while play:

        ok = True

        #threads for create walls
        staticWallThread = Thread(target=createStaticWalls())
        destroyableWallThread = Thread(target = createDestroyableWalls())

        staticWallThread.start()
        destroyableWallThread.start()

        staticWallThread.join()
        destroyableWallThread.join()
        #createWalls()

        bomberman = Bomberman(img,1,1)
        if playersNo == 2:
            bomberman2 = Bomberman(img2,17,11)

        enemy_list = pygame.sprite.Group()  # create enemy group
        for x in range(level):
            enemy = Enemy('enemy.png')
            enemy_list.add(enemy)  # add enemy to group

        bomb_list = pygame.sprite.Group()  # create bomb list

        if playersNo == 2:
            bomb_list2 = pygame.sprite.Group()

        fObjekat = Gifts()
        fObjekat.provera = True  # da bi samo jednom odradilo force
        force_list = pygame.sprite.Group()  # pravim grupu
        force_list.add(fObjekat)  # dodajem objekat u grupi

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
                    if event.key == ord('q'):
                        pygame.quit()
                        sys.exit()
                        ok = False
                    if not bomberman.hidden:
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
                        if not bomberman2.hidden:
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
                    bomb.explode(world, deWalls_list, bomberman, 1, enemy_list)

            bomberman.update(1)

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
                        bomb2.explode(world, deWalls_list, bomberman2, 2, enemy_list)

                bomberman2.update(2)

            if enemy_list.__len__() == 0:
                level += 1
                ok = False

            bomberman.show_score(world, 1)
            bomberman.show_lives(world, 1)
            lev = level_cfg.render('Level: ' + str(level), True, (255, 230, 0))
            world.blit(lev, (10,495))


            if playersNo == 2:
                bomberman2.show_score(world, 2)
                bomberman2.show_lives(world, 2)


            enemy_list.draw(world)  # refresh enemies
            #if enemy_flag == True:
            threads = []
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

            if fObjekat.provera == True:
                fObjekat.update(dt)
                if fObjekat.TimeToAppear <= 0:
                    fObjekat.poziv(world, bomberman, dt, 1)  # za prvog icraca
                    if playersNo == 2:
                        fObjekat.poziv(world, bomberman2, dt, 2)  # za drugog igraca

                    force_list.draw(world)  # onda iscrtaj listu sa tim objektima-samo jedna

                # odradjuje
                # if fObjekat.provera==False:
            if fObjekat.TimeToAppear <= 0:
                if fObjekat.provera == False:
                    force_list.remove(fObjekat)  # uklanja sa liste da bi se obrisala slika
                    force_list.draw(world)  # iscrtava ponovo da bi se sila uklonila

            hit_list = pygame.sprite.spritecollide(bomberman, enemy_list, False)

            if hit_list.__len__() > 0:
                bomberman.lives_down(world, 1)

            t.tik_tack(world)
            pygame.display.flip()
            clock.tick(fps)

            if bomberman.total_lives == 0:
                game_over()

            if playersNo == 2:
                if bomberman2.total_lives == 0:
                    game_over()


