from enum import Enum
import  random
#vec ima dve klase moze samo jos jedna pazite sta stavljete
width=760
height=760

"""monsterlx=random.randint(0,3)
monsterly=random.randint(9,12)

monsterl2x=random.randint(4,6)
monsterl2y=random.randint(4,8)

monsterl3x=random.randint(7,10)
monsterl3y=random.randint(0,3)"""


def make_matrix():  # player3Lives,player4Lives,player5Lives
    Matrix = [[0 for x in range(width)] for y in range(height)]
  #okvirni zidovi
    # for u in range(0,width,1):  # gornja paralelna sa podlogom-x se menja
    #     Matrix[u][0]=2
    # for u1 in range(0,height):  # leva y se menja
    #     Matrix[0][u1]=2
    # for u2 in range(width):  # donja-x se menja
    #     Matrix[u2][height-1] = 2
    # for u3 in range(height): # desna -y se menja
    #     Matrix[width-1][u3] = 2
    #
    # step=2
    # for t in range(2,width-2,step):
    #     for t1 in range(2,height,step):
    #         Matrix[t][t1]=2
    # for r in range((round(133 / 1.3))):
    #     m = random.randint(0, 13)
    #     n = random.randint(0, 13)
    #     if (Kind(Matrix[m][n]) == Kind.Empty):
    #         Matrix[m][n] = Kind.Wall


    return  Matrix


class Kind(Enum):
        Empty=0
        Wall=1
        IndestructibleWall=2
        Bomb=3
        Monster=4
        Player1=5
        Player2 = 6
        Player3 = 7
        Player4 = 8
        Player5 = 9
        PlayerBomb1 = 10  # slika sa bombom dok je avatar drzi
        PlayerBomb2 = 11
        PlayerBomb3 = 12
        PlayerBomb4 = 13
        PlayerBomb5 = 14
        Fire=15

class Direction(Enum):
    Left=1
    Right=2
    Up=3
    Down=4
    BombPlanted=5



