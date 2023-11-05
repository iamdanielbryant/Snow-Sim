import pygame
import asset

class Tile:
    def __init__(self,sprites):
        self.size = 32
        self.solid = False
        self.sprites = sprites
        self.pos = pygame.Vector2(0,0)

    def render(self,surface):
        surface.blit(self.sprites.getSprite(0,0),self.pos)

class World:
    def __init__(self,gameWidth,gameHeight,sprites):
        self.width = 5
        self.height = 5
        self.sprites = sprites
        self.worldSize = pygame.Vector2(self.width * self.sprites.spriteSize,self.height * self.sprites.spriteSize)
        self.offset = pygame.Vector2(gameWidth / 2,gameHeight / 2)
        self.tiles = []
        self.createWorld()

    def createWorld(self):
        for h in range(self.height):
            for w in range(self.width):
                t = Tile(self.sprites)
                t.pos.x += self.offset.x - self.worldSize.x / 2 + (w * t.size)
                t.pos.y += self.offset.y - self.worldSize.y / 2 + (h * t.size)
                self.tiles.append(t)
    
    def renderWorld(self,surface):
        for t in self.tiles:
            t.render(surface)


