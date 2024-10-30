import pygame.sprite
import os
import sys

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
from utilities import helpers
from utilities import constants

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '.'))
from layer import layer

class background(pygame.sprite.Sprite):
    def __init__(self, index, *groups):
        self._layer = layer.BACKGROUND

        self.image = helpers.getImages('Background')
        self.rect = self.image.get_rect(topleft=(constants.SCREEN_WIDTH * index, 0))

        super().__init__(*groups)

    def update(self):
        self.rect.x -= 1
        if self.rect.right <= 0:
            self.rect.x = constants.SCREEN_WIDTH