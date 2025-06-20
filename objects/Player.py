import pygame
from objects.BasicObject import BasicObject
from objects.Coin import Coin
from objects.Enemy import Enemy
from util.Controller import Controller
class Player(BasicObject):
    def __init__(self,*args):
        super().__init__(*args) 
        self.controller = Controller(False,False,False,False)
        self.coins = 0
        
    def step(self):
        if self.controller.right:
            self.rect.left+=1
        if self.controller.left:
            self.rect.left-=1
        if self.controller.up:
            self.rect.top-=1
        if self.controller.down:
            self.rect.top+=1
    def draw(self,surface):
        pygame.draw.ellipse(surface, (0, 255, 0), self.rect)
    def collision(self,gameObjects):
        for a in gameObjects:
            if type(a) == Coin and self.rect.colliderect(a):
                a.active = False
                self.coins +=1
            elif type(a) == Enemy and self.rect.colliderect(a):
                self.active = False