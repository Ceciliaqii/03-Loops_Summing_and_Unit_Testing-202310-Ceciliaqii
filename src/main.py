import sys

import pygame
from Game import Game
from Controller import Controller
from View import View
from Character import Character
from Dice import Dice
import random

# Mingjian Qin, Wenjian Zhang, Xiaoxi Qi


def main():
    pygame.init()
    screen = pygame.display.set_mode((950, 950))  # Done: Choose your own size
    pygame.display.set_caption("The Monopoly")  # Done: Choose your own title
    clock = pygame.time.Clock()
    game = Game(screen)  # the Model
    viewer = View(screen, game)  # the View
    controller = Controller(game)  # the Controller
    frame_rate = 31  # Done: Choose your own frame rate

    dices = ["../assets/dice1.png", "../assets/dice2.png", "../assets/dice3.png",
             "../assets/dice4.png", "../assets/dice5.png", "../assets/dice6.png"]
    di = "../assets/dice6.png"

    while True:
        clock.tick(frame_rate)
        controller.get_and_handle_events()
        game.run_one_cycle()
        viewer.draw_everything()  # Includes the pygame.display.update()
        pressed_key = pygame.key.get_pressed()

        if pressed_key[pygame.K_SPACE]:
            di = random.choice(dices)
        dice = Dice(screen, di, 425, 425)
        dice.draw()
        pygame.display.update()



main()
