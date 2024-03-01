import pygame
import constants
from pygame.locals import (
    RLEACCEL,
)

"""
A class representing the background

attributes:
    surf: The surface of the background
    rect: The rectangle of the background
"""
class Background(pygame.sprite.Sprite):
    """
    Inititate the background
    """
    def __init__(self):
        super(Background, self).__init__()
        self.surf = pygame.image.load("media/sprites/bg.png").convert()
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        self.surf = pygame.transform.scale(self.surf, (constants.WINDOW_WIDTH, constants.WINDOW_HEIGHT))
        self.rect = self.surf.get_rect()
        return