import pygame
import os
import sys

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from utilities import constants
from utilities import helpers

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '.'))
from models.background import background 

pygame.init()

screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
clock = pygame.time.Clock()
isRunning = True

helpers.loadImages()

images = pygame.sprite.LayeredUpdates()
background(0, images)
background(1, images)

while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False

    screen.fill('pink')
    images.draw(screen)
    images.update()
    pygame.display.flip()
    clock.tick(constants.FPS)

pygame.quit()