import pygame
from screeninfo import get_monitors

import snow as snowlib
import world
import asset

#pygame setup
pygame.init()
clock = pygame.time.Clock()
running = True

#screen setup
monitorWidth = get_monitors()[0].width
monitorHeight = get_monitors()[0].height
gameWidth = monitorWidth / 1.5
gameHeight = monitorHeight / 1.5

pygame.display.set_caption("Snow Simulator")
screen = pygame.display.set_mode((gameWidth,gameHeight))
surface = pygame.Surface((gameWidth,gameHeight), pygame.SRCALPHA)

#game objects
snow = snowlib.Snow(surface)
asset = asset.Sprites()
world = world.World(gameWidth,gameHeight, asset)

#gameloop
while running:
    surface.fill("black")
    snow.updateFlakes()

    #close window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    

    #render game here
    world.renderWorld(surface)
    snow.renderSnow() 


    #pygame stuff
    screen.blit(surface,(0,0))
    pygame.display.flip()
    clock.tick(60)
    

pygame.quit()

