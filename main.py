import pygame
import numpy
import config

#Pygame initialisation
pygame.init()
screen = pygame.display.set_mode((config.WIDTH, config.HEIGTH))
clock = pygame.time.Clock()
running = True


while(running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.display.flip()
    clock.tick(config.FPS)

pygame.quit()