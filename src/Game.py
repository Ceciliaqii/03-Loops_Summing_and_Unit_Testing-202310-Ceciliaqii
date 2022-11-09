import pygame
import random


# Put each class in its own module, using the same name for both.
# Then use statements like the following, but for YOUR classes in YOUR modules:
#     from Fighter import Fighter
#     from Missiles import Missiles
#     from Enemies import Enemies

# Mingjian Qin, Wenjian Zhang, Xiaoxi Qi


class Game:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        # Store whatever YOUR game needs, perhaps something like this:
        self.bill=Character(5,5,screen,"../assets/dice1.png")
        self.dice=Dice(screen, "../assets/dice2.png")
        self.map=Map(screen,"../assets/6920631.jpg")
        #     self.fighter = Fighter(self.screen, self.missiles)
        #     self.enemies = Enemies(self.screen)

    def draw_game(self):
        """ Ask all the objects in the game to draw themselves. """
        # Use something like the following, but for the objects in YOUR game:
        self.map.draw ()
        self.bill.draw()
        self.dice.draw()
        #     self.enemies.draw()

    def run_one_cycle(self):
        """ All objects that do something at each cycle: ask them to do it. """
        # Use something like the following, but for the objects in YOUR game:
        #     self.missiles.move()
        #     self.enemies.move()
        #     self.missiles.handle_explosions(self.enemies)

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
        self.screen.blit(self.image, (700,700))

class Dice:

    def __init__(self,screen, immge):
        self.screen=screen
        self.image=pygame.image.load(immge)

    def draw(self):
        self.screen.blit(self.image, (500,500))

    # def roll(self, immge, screen,

class Map:
    def __init__(self, screen, img):
        self.screen=screen
        self.img=pygame.image.load(img)
    def draw(self):
        self.screen.blit(self.img,(0,0))
