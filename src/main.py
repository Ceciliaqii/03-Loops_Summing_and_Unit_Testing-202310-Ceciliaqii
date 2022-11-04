import pygame
from Game import Game
from Controller import Controller
from View import View

# Mingjian Qin, Wenjian Zhang, Xiaoxi Qi
# DONE: Put your names here (entire team)


def main():
    pygame.init()
    screen = pygame.display.set_mode((5000, 5000))  # Done: Choose your own size
    pygame.display.set_caption("The Big Ass Monopolyyyyyyy")  # Done: Choose your own title
    clock = pygame.time.Clock()
    game = Game(screen)  # the Model
    viewer = View(screen, game)  # the View
    controller = Controller(game)  # the Controller

    frame_rate = 120  # Done: Choose your own frame rate

    while True:
        clock.tick(frame_rate)
        controller.get_and_handle_events()
        game.run_one_cycle()
        viewer.draw_everything()  # Includes the pygame.display.update()


main()
