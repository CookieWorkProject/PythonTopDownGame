import pygame
from objects.BasicObject import BasicObject
from objects.Player import Player
from objects.Enemy import Enemy
from objects.Coin import Coin
# Initialize Pygame
pygame.init()

# Set up the game window
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Top Down Game")

#initialize Gameobjects
gameObjects = []

gameObjects.append(Player(0,0))
gameObjects.append(Enemy(50,50))
gameObjects.append(Coin(150,150))

# Game loop
running = True
while running:
    for a in gameObjects:
        a.step()
    for a in gameObjects:
        a.draw(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
# Quit Pygame
pygame.quit()