import pygame
from objects.BasicObject import BasicObject
class Enemy(BasicObject):
    def draw(self,surface):
        pygame.draw.ellipse(surface, (255, 0, 0), (self.x, self.y, 20, 20))
