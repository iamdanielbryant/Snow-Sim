import pygame
import snow as snowlib

width = 640
height = 480

pygame.init()
screen = pygame.display.set_mode((width,height))
surface = pygame.Surface((width,height), pygame.SRCALPHA)

clock = pygame.time.Clock()
running = True

snow = snowlib.Snow(surface)

while running:
    surface.fill("black")

    snow.updateFlakes()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #render game here
    snow.renderSnow() 

    screen.blit(surface,(0,0))
    pygame.display.flip()

    clock.tick(60)

pygame.quit()

