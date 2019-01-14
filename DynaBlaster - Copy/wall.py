from definitions import *
from StaticWall import *
from DestroyableWall import *

stWalls_list = pygame.sprite.Group()  # create static walls group
deWalls_list = pygame.sprite.Group()  # create destroyableWalls group


def createWalls():
    # iscrtavanje okolnih zidova kroz naredne 2 for petlje
    for x in range(0, worldx, iconSize):
        stWall1 = StaticWall(x, 0)
        stWall2 = StaticWall(x, worldy - iconSize)
        stWalls_list.add(stWall1)
        stWalls_list.add(stWall2)
        wallsPositions[round(stWall1.rect.x / iconSize)][0] = 1
        wallsPositions[round(stWall2.rect.x / iconSize)][round(stWall2.rect.y / iconSize)] = 1
    for y in range(iconSize, worldy, iconSize):
        stWall3 = StaticWall(0, y)
        stWall4 = StaticWall(worldx - iconSize, y)
        stWalls_list.add(stWall3)
        stWalls_list.add(stWall4)
        wallsPositions[0][round(stWall3.rect.y / iconSize)] = 1
        wallsPositions[round(stWall4.rect.x / iconSize)][round(stWall4.rect.y / iconSize)] = 1

    # iscrtavanje unutrasnjih zidova
    for x in range(iconSize * 2, worldx - iconSize * 2, iconSize * 2):
        for y in range(iconSize * 2, worldy - iconSize * 2, iconSize * 2):
            stWall = StaticWall(x, y)
            wallsPositions[round(stWall.rect.x / iconSize)][round(stWall.rect.y / iconSize)] = 1
            stWalls_list.add(stWall)

    for x in range(iconSize, worldx - iconSize, iconSize):
        for y in range(iconSize, worldy - iconSize, iconSize):
            if bool(random.getrandbits(1)):
                if wallsPositions[round(x / iconSize)][round(y / iconSize)] == 0:  # ako je prazno polje
                        if x != worldx - iconSize * 2 and y != worldy - iconSize * 2:
                            deWall = DestroyableWall(x, y)
                            deWalls_list.add(deWall)
                            wallsPositions[round(deWall.rect.x / iconSize)][
                                round(deWall.rect.y / iconSize)] = 2  # za unistive zidove