from enum import Enum
import  random
#vec ima dve klase moze samo jos jedna pazite sta stavljete
width=760
height=520

"""monsterlx=random.randint(0,3)
monsterly=random.randint(9,12)

monsterl2x=random.randint(4,6)
monsterl2y=random.randint(4,8)

monsterl3x=random.randint(7,10)
monsterl3y=random.randint(0,3)"""


def make_matrix():  # player3Lives,player4Lives,player5Lives
    Matrix = [[0 for x in range(13)] for y in range(19)]
    return  Matrix


wallsPositions= make_matrix()

