import pygame
import random

class Snow:

    def __init__(self,surface):
        self.maxFlakes = 100
        self.surface = surface
        self.screenWidth = surface.get_width()
        self.screenHeight = surface.get_height()
        self.flakes = []
        self.gravity = 1

        for i in range(self.maxFlakes):
            randW = random.uniform(0,self.screenWidth)
            randH = random.uniform(-self.screenHeight,self.screenHeight)

            pos = pygame.Vector2(randW,randH)
            snowEntity = {
                "position": pos, 
                "size": random.uniform(1,2),
                "opacity": random.uniform(0,255),
                "speed": 1,
                "xFactor":random.uniform(-1,1), 
                "yFactor":random.uniform(-1,1)
            }
            self.flakes.append(snowEntity)

    def updateFlakes(self):
        for s in self.flakes:
            s["position"].x += s["speed"] * s["xFactor"]
            s["position"].y += s["speed"] * s["yFactor"] + self.gravity

            if (s["position"].x > self.screenWidth or s['position'].y > self.screenHeight):
                s["position"].x = random.uniform(0,self.screenWidth)
                s["position"].y = random.uniform(0,-self.screenHeight)

    def renderSnow(self):
        for s in self.flakes:
            pygame.draw.circle(self.surface, (255,255,255,s['opacity']),s["position"],s["size"])
        
    

