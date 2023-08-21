import numpy as np
import pygame


class Objeto():
    def __init__(self, x, y):
        self.s = np.array([x,y])
        self.s0 = np.array([x,y])
        self.v = np.array([0.0,0.0])

    def draw(self, screen):
        pygame.draw.circle(screen, (0,255,0), self.s, 10)
    
    def set_v(self, v):
        self.v = v
