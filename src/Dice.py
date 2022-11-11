import random

import pygame

class Dice:

    def __init__(self, screen, pic, x, y):
        self.screen = screen
        self.image = pygame.image.load(pic)
        self.image = pygame.transform.scale(self.image, (80, 80))
        self.x = x
        self.y = y

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))


