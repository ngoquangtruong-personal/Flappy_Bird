import pygame.sprite
import os
import sys

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
from utilities import helpers
from utilities import constants

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '.'))
from layer import layer

class gamestartmessage(pygame.sprite.Sprite):
    def __init__(self, *groups):
        self._layer = layer.UI

        self.image = helpers.getImages('Game_start_message')
        self.rect = self.image.get_rect(center=(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2))

        self.mask = pygame.mask.from_surface(self.image)

        super().__init__(*groups)