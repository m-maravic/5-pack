from enum import Enum
import  random
#vec ima dve klase moze samo jos jedna pazite sta stavljete
worldx = 760
worldy = 520
iconSize = 40
img = 'playerup.png'

"""monsterlx=random.randint(0,3)
monsterly=random.randint(9,12)

monsterl2x=random.randint(4,6)
monsterl2y=random.randint(4,8)

monsterl3x=random.randint(7,10)
monsterl3y=random.randint(0,3)"""


def make_matrix():
    Matrix = [[0 for x in range(20)] for y in range(20)]
    return  Matrix


wallsPositions= make_matrix()

