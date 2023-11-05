import pygame

class Sprites:
    def __init__(self):
        self.spritesheet = pygame.image.load("asset/spritesheet.png").convert()
        self.width,self.height = self.spritesheet.get_size()
        self.spriteSize = 32

    def getSprite(self,locX,locY):
        sprite = self.spritesheet.subsurface((locX * self.spriteSize,locY * self.spriteSize,self.spriteSize,self.spriteSize))

        return sprite


