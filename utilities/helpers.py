import os
import pygame

images = {}

def loadImages():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'assets', 'images') 
    for file in os.listdir(path):
        images[file.split('.')[0]] = pygame.image.load(os.path.join(path, file))

def getImages(imageName):
    return images[imageName]
