import pygame.sprite
import os
import sys

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
from utilities import helpers
from utilities import constants

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '.'))
from layer import layer

class score(pygame.sprite.Sprite):
    def __init__(self, *groups):
        self._layer = layer.UI
        
        self.value = 0

        self.image = pygame.surface.Surface((0, 0), pygame.SRCALPHA)
        
        self.__create()

        super().__init__(*groups)
    
    def __create(self):
        self.stringValue = str(self.value)
        
        self.images = []
        self.width = 0

        for stringValueChar in self.stringValue:
            image = helpers.getImages(stringValueChar)
            self.images.append(image)
            self.width += image.get_width()

        self.height = self.images[0].get_height()

        self.image = pygame.surface.Surface((self.width, self.height), pygame.SRCALPHA)
        self.rect = self.image.get_rect(center=(constants.SCREEN_WIDTH / 2, 50))
        
        x = 0
        for image in self.images:
            self.image.blit(image, (x, 0))
            x += image.get_width()

    def update(self):
        self.__create()