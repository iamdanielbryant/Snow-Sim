import pygame

class Sprites:
    def __init__(self):
        self.spritesheet = pygame.image.load("spritesheet.png").convert()
        self.width,self.height = self.spritesheet.get_size()

        self.spriteSize = 32

        self.rows = self.width // self.spriteSize
        self.columns = self.height // self.spriteSize

        self.sprites = []
        for i in range(self.rows):
            for j in range(self.columns):
                subimage = self.spritesheet.subsurface((j * self.spriteSize, i * self.spriteSize, self.spriteSize, self.spriteSize))
                self.sprites.append(subimage)


    def getSprite(self,location):
        return self.sprites[location]


