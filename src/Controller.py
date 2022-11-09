import pygame
import sys
from Game import Game
from Character import Character

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
            if pressed_keys[pygame.K_UP]:
                self.game.mutchler.y-=2
            if pressed_keys[pygame.K_DOWN]:
                self.game.mutchler.y+=2
            if pressed_keys[pygame.K_LEFT]:
                self.game.mutchler.x-=2
            if pressed_keys[pygame.K_RIGHT]:
                self.game.mutchler.x+=2
            if pressed_keys[pygame.K_w]:
                self.game.bill.y -= 2
            if pressed_keys[pygame.K_s]:
                self.game.bill.y += 2
            if pressed_keys[pygame.K_a]:
                self.game.bill.x -= 2
            if pressed_keys[pygame.K_d]:
                self.game.bill.x += 2
            if pressed_keys[pygame.K_i]:
                self.game.baobei.y -= 2
            if pressed_keys[pygame.K_k]:
                self.game.baobei.y += 2
            if pressed_keys[pygame.K_j]:
                self.game.baobei.x -= 2
            if pressed_keys[pygame.K_l]:
                self.game.baobei.x += 2
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
