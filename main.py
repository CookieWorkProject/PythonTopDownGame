import pygame
from objects.BasicObject import BasicObject
from objects.Player import Player
from objects.Enemy import Enemy
from objects.Coin import Coin
from util.Controller import Controller
from util.Controller import Controller
def startGame(gameObjects,replay,player):
    # Initialize Pygame
    pygame.init()

    # Set up the game window
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Top Down Game")

    # Game loop
    running = True
    FramesSinceStart = 0
    FPS = 60
    clock = pygame.time.Clock()
    while running:
        
        
        screen.fill((0,0,0))
        if FramesSinceStart < len(replay):
            player.controller = replay[FramesSinceStart]
        else:
            running = False
            break
        for a in gameObjects:
            if a.active:
                a.step()
                a.draw(screen)
                a.collision(gameObjects)
        
                
        pygame.display.update()
        FramesSinceStart +=1
        pygame.display.set_caption(str(FramesSinceStart))
        clock.tick(60)
    # Quit Pygame
    pygame.quit()
    return gameObjects
    
    
