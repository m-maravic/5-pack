#ova skripta trenutno nista ne radi zidove smo pravile u definitions

import sys
from PyQt5 import*
from definitions import *
from pyrandom import *



def countFreeSpace(w,h):
    Matrix1 = make_matrix()
    count = 0
    for i in range(w):
        for j in range(h):
            if(Kind(Matrix[i][j]) == Kind.Empty):
               count=count+1


    return count

def makeDestructableWall():
   br= countFreeSpace(13, 13)
   Matrix=make_matrix()
   for r in range((round(br / 1.3))):
       m = random.randint(0, 13)
       n = random.randint(0, 13)
       if (Kind(Matrix[m][n]) == Kind.Empty):
           Matrix[m][n] = Kind.Wall


   return Matrix