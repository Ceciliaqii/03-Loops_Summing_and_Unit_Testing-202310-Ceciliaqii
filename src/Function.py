import pygame, random


pygame.init()

display_width = 950
display_height = 950

white = (255, 255, 255)
black = (0, 0, 0)
yellow = (255, 255, 0)
red = (255, 50, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
back = (100, 10, 100)

clock = pygame.time.Clock()

a = 0
b = 0

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Monopoly")
pygame.display.update()

def rolldice():
    global a, b
    a = random.randrange(1, 7)
    b = random.randrange(1, 7)

    return a + b