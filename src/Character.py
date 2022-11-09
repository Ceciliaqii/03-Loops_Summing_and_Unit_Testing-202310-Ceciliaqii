import pygame

class Character:
    def __init__(self, x, y, screen, imaage):
        self.screen=screen
        self.image=pygame.image.load(imaage)
        self.x=x
        self.y=y

    def move(self, x1, y1):
        self.x=self.x + x1
        self.y=self.y+y1

    def draw(self):
        self.screen.blit(self.image, (900,900))

