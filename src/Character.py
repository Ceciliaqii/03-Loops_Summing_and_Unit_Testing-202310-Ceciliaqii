import pygame

class Character:
    def __init__(self, x, y, screen, imaage):
        self.screen = screen
        self.image = pygame.image.load(imaage)
        self.x = x
        self.y = y
        self.saving = 1000

    def move_left(self):
        self.x = self.x - 1

    def move_right(self):
        self.x = self.x + 1

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))

    def minus10(self):
        self.saving = self.saving - 10

    def minus50(self):
        self.saving = self.saving - 50

    def plus100(self):
        self.saving+=100
