import pygame
from objects.BasicObject import BasicObject
class Player(BasicObject):
    def draw(self,surface):
        pygame.draw.ellipse(surface, (0, 255, 0), (self.x, self.y, 20, 20))
