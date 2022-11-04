import pygame
global p
import fun
class gameboard():
     money_to_win=1000
     def __init__(self):
         self.name="Bill"
p=[gameboard(),gameboard()]
def screen1(a,b,c):
     gameboard.money_to_win=(int)(c.get())

