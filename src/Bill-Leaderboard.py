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

    display_width=1500
    display_height=1000

    Exit=False
    while not exit:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit= True
x = 615
y1 = 200
y2 = 300
y3 = 400
l = 200
h = 50

pygame.display.update()



