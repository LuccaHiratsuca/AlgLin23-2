import pygame
import numpy as np

class Alvo():
    def __init__(self, x, y):
        self.s = np.array([x,y])
        self.hit = False

    def draw(self, screen):
        if not self.hit:
            pygame.draw.circle(screen, (0,0,255), self.s, 20)
        