import pygame
import asset

#pygame setup
pygame.init()
clock = pygame.time.Clock()
running = True

gameWidth = 320
gameHeight = 192

pygame.display.set_caption("Level Editor")
screen = pygame.display.set_mode((gameWidth,gameHeight))
surface = pygame.Surface((gameWidth,gameHeight), pygame.SRCALPHA)

#game objects
assets = asset.Sprites()
spriteID = pygame.Vector2(0,0)


#gameloop
while running:
    surface.fill("black")


    mouseX,mouseY = pygame.mouse.get_pos()
    currentTile = assets.getSprite(spriteID.x,spriteID.y)
    
    coords = pygame.Vector2((mouseX // 32) * 32, (mouseY // 32) * 32)
    surface.blit(currentTile,coords)

        #close window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if pygame.key.get_pressed()[pygame.K_RIGHT]:
                if (spriteID.x <= 14):
                    spriteID.x += 1
            elif pygame.key.get_pressed()[pygame.K_LEFT]:
                if (spriteID.x >= 1):
                    spriteID.x -= 1



     #pygame stuff
    screen.blit(surface,(0,0))
    pygame.display.flip()
    clock.tick(60)
    

pygame.quit()