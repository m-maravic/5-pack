import pygame
from threading import Thread, Timer
from multiprocessing import Pipe
import time
from CloseWindow import *

# Define some colorsc
class Timer():
        def __init__(self):
                self.cur_time = time.time()
        def tik_tack(self,world):
                font = pygame.font.Font(None, 25)
                run_time=time.time()-self.cur_time
                t=round(run_time,0)


                t1=90-t

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

        #def timer_tik(screen):
        # clock = pygame.time.Clock()
        # font = pygame.font.Font(None, 25)
        # frame_count = 0
        # frame_rate = 60
        # start_time = 90
        # counter = start_time
        # total_seconds = frame_count // frame_rate
        # minutes = total_seconds // 60
        # seconds = total_seconds % 60
        #
        # #while counter !=0:
        # total_seconds = start_time - (frame_count // frame_rate)
        # if total_seconds < 0:
        #         total_seconds = 0
        # minutes = total_seconds // 60
        # seconds = total_seconds % 60
        #
        # # Use python string formatting to format in leading zeros
        # output_string = "Time left: {0:02}:{1:02}".format(minutes, seconds)
        #
        # text = font.render(output_string, True, (255, 230, 0))
        # counter = counter-1
        # screen.blit(text,(300, 10))
        # frame_count += 1
        # clock.tick(frame_rate)
