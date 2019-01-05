import  pygame
import os

class DestroyableWall(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(os.path.join('Slike', 'Wall.jpg')).convert()
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y