import pygame
import random
pygame.init()

def main():
    screen = pygame.display.set_mode([550,200])
    screen.fill((0, 0, 0))
    pygame.display.set_caption('dice')
    pygame.display.flip()

    myfont = pygame.font.SysFont("monospace", 15)


    label = myfont.render("click the button to roll the dice!", 2, (255, 0, 255))
    screen.blit(label, (200, 100))





    running= True

    while running:
         for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            dice = [1, 2, 3, 4, 5, 6]


            button = pygame.Rect(100, 100, 50, 50)
            playerroll = random.choice(dice)


            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()


                if button.collidepoint(mouse_pos):
                    print("you rolled a:" , playerroll)

            pygame.draw.rect(screen, [255, 255, 255], button)
            pygame.display.update()

if __name__ == '__main__':
    main()


