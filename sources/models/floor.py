import pygame.sprite
import os
import sys

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
from utilities import helpers
from utilities import constants

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '.'))
from layer import layer

class floor(pygame.sprite.Sprite):
    def __init__(self, index, *groups):
        self._layer = layer.FLOOR

        self.image = helpers.getImages('Floor')
        self.rect = self.image.get_rect(bottomleft=(constants.SCREEN_WIDTH * index, constants.SCREEN_HEIGHT))

        self.mask = pygame.mask.from_surface(self.image)

        super().__init__(*groups)

    def update(self):
        self.rect.x -= 2
        if self.rect.right <= 0:
            self.rect.x = constants.SCREEN_WIDTH
