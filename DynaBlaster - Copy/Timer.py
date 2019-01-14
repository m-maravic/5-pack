import pygame
from threading import Thread, Timer
from multiprocessing import Pipe
import time
import os
from CloseWindow import *

# Define some colorsc
class Timer():
        def __init__(self):
                self.cur_time = time.time()
        def tik_tack(self,world):
                font = pygame.font.Font(None, 25)
                run_time=time.time()-self.cur_time
                t=round(run_time,0)

                t1=180-t

                minuts=round(t1//60,0)
                minuts=int(minuts)

                sesonds=t1%60
                sesonds=int(sesonds)

                text = font.render("{0}:{1:0}".format(minuts,sesonds), True, (255, 230, 0))
                world.blit(text,(300, 10))

                if t1 > 1 :
                        pass
                else:
                        game_over()
