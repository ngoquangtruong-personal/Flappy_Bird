import pygame.sprite
import os
import sys
import random

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
from utilities import helpers
from utilities import constants

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '.'))
from layer import layer

class pipe(pygame.sprite.Sprite):
    def __init__(self, *groups):
        self._layer = layer.OBSTACLE

        self.gap = 100

        self.sprite = helpers.getImages('Green_pipe')
        self.spriteRect = self.sprite.get_rect()

        self.pipeBottom = self.sprite
        self.pipeBottomRect = self.pipeBottom.get_rect(topleft=(0, self.spriteRect.height + self.gap))
        self.pipeTop = pygame.transform.flip(self.sprite, False, True)
        self.pipeTopRect = self.pipeTop.get_rect(topleft=(0, 0))

        self.image = pygame.surface.Surface((self.spriteRect.width, self.spriteRect.height * 2 + self.gap), pygame.SRCALPHA)
        self.image.blit(self.pipeBottom, self.pipeBottomRect)
        self.image.blit(self.pipeTop, self.pipeTopRect)

        spriteFloorHeight = helpers.getImages('Floor').get_rect().height
        minY = 100
        maxY = constants.SCREEN_HEIGHT - spriteFloorHeight - 100

        self.rect = self.image.get_rect(midleft=(constants.SCREEN_WIDTH, random.uniform(minY, maxY)))

        self.mask = pygame.mask.from_surface(self.image)

        self.isPassed = False

        super().__init__(*groups)

    def update(self):
        self.rect.x -= 2
        if self.rect.right <= 0:
            self.kill()

    def passed(self):
        if self.rect.x < 50 and not self.isPassed:
            self.isPassed = True
            return True
        return False