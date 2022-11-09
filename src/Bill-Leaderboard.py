import pygame
class gameboard():
     money_to_win=1000
     def __init__(self):
         self.name="Bill"

p=[gameboard(),gameboard()]
def screen1(a,b,c):
     gameboard.money_to_win=(int)(c.get())
     p[1].name=b.get()
     p[0].name=a.get()

    pygame.init()

    display_width=950
    display_height=950

    exit=False
    while not exit:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit= True
    pygame.display.update()



