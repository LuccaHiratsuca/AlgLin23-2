import numpy as np
import pygame

class Planeta():
    def __init__(self, x, y, raio, atrator):
        self.planeta = 0
        self.s = np.array([x,y])
        self.raio = raio
        self.atrator = atrator

    def draw(self, screen):
        pygame.draw.circle(screen, (255,0,0), self.s, 20)
        pygame.draw.circle(screen, (255,255,255), self.s, self.raio, 1)
    
    