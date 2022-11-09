import pygame
import sys
from Game import Game

# Mingjian Qin, Wenjian Zhang, Xiaoxi Qi

class Controller:
    def __init__(self, game: Game):
        self.game = game

    def get_and_handle_events(self):
        """
        [Describe what keys and/or mouse actions cause the game to ...]
        """
        events = pygame.event.get()
        self.exit_if_time_to_quit(events)

        pressed_keys = pygame.key.get_pressed()
        # while True:
        #     for event in pygame.event.get():
        #         pressed_keys = pygame.key.get_pressed()
        #         if pressed_keys[pygame.K_UP]:
        #             print("up")
        #         if pressed_keys[pygame.K_DOWN]:
        #             print('down')
        #         if pressed_keys[pygame.K_LEFT]:
        #             print('left')
        #         if pressed_keys[pygame.K_RIGHT]:
        #             print("right")

    @staticmethod
    def exit_if_time_to_quit(events):
        for event in events:
            if event.type == pygame.QUIT:
                sys.exit()

    @staticmethod
    def key_was_pressed_on_this_cycle(key, events):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == key:
                return True
        return False
