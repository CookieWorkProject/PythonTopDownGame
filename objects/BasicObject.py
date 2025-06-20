import pygame
class BasicObject:
    def __init__(self, rect):
        self.rect = rect
        self.active = True

    def step(self):
        pass
    def draw(self):
        pass
    def collision(self,gameObjects):
        pass
        