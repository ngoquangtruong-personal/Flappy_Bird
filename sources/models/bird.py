import pygame.sprite
import os
import sys

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
from utilities import helpers
from utilities import constants

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '.'))
from layer import layer

from models.floor import floor
from models.pipe import pipe

class bird(pygame.sprite.Sprite):
    def __init__(self, *groups):
        self._layer = layer.PLAYER

        self.images = [helpers.getImages('Red_bird-Up_flap'), helpers.getImages('Red_bird-Middle_flap'), helpers.getImages('Red_bird-Down_flap')]

        self.image = self.images[0]
        self.rect = self.image.get_rect(topleft=(-50, 50))

        self.mask = pygame.mask.from_surface(self.image)

        self.flap = 0

        super().__init__(*groups)

    def update(self):
        self.images.insert(0, self.images.pop())

        self.image = self.images[0]

        self.flap += constants.GRAVITY
        self.rect.y += self.flap

        if self.rect.x < 50:
            self.rect.x += 3

    def handleEvent(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            self.flap = 0
            self.flap -= 6
            helpers.playSound('Wing')

    def checkCollision(self, sprites):
        for sprite in sprites:
            if ((type(sprite) is pipe or type(sprite) is floor) and sprite.mask.overlap(self.mask, (self.rect.x - sprite.rect.x, self.rect.y - sprite.rect.y)) or self.rect.bottom < 0):
                return True
        return False