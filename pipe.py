import pygame
import constants
import random

from enum import Enum

from pygame.locals import (
    RLEACCEL,
)

def getRandomGapTopPosition():
    return random.randint(constants.MIN_GAP_TOP, constants.MAX_GAP_TOP)

class PipeType(Enum):
    TOP = 0,
    BOTTOM = 1,

"""
A class representing a pipe

attributes:
    surf: The surface of the pipe
    rect: The rectangle of the pipe
"""
class Pipe(pygame.sprite.Sprite):
    def __init__(self, gapTopPos, pipeType):
        super(Pipe, self).__init__()
        if pipeType == PipeType.TOP:
            self.initTop(gapTopPos)
        if pipeType == PipeType.BOTTOM:
            self.initBottom(gapTopPos)
        # self.surf.fill(constants.GREEN)
        return

    def initTop(self, gapTopPos):
        self.surf = pygame.image.load("media/sprites/pipe.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        size = (constants.PIPE_WIDTH, constants.PIPE_HEIGHT)
        self.surf = pygame.transform.scale(self.surf, size)
        self.rect = self.surf.get_rect(
            bottomleft=(constants.WINDOW_WIDTH, gapTopPos)
        )
        return

    def initBottom(self, gapTopPos):
        self.surf = pygame.image.load("media/sprites/pipe.png").convert()
        self.surf = pygame.transform.flip(self.surf, False, True) # flip bottom pipe
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        size = (constants.PIPE_WIDTH, constants.PIPE_HEIGHT)
        self.surf = pygame.transform.scale(self.surf, size)
        self.rect = self.surf.get_rect(
            topleft = (constants.WINDOW_WIDTH, gapTopPos + constants.PIPE_GAP_HEIGHT)
        )
        return

    def update(self, dt):
        self.rect.move_ip(-constants.SCROLLING_SPEED, 0)
        if self.rect.right < 0:
            self.kill()
        return

"""
A class representing a pair or pipes

attributes:
    _TopPipe: The pipe going from the top to the bottom
    _BottomPipe: The pipe going from the bottom to the top
"""
class PipePair():
    def __init__(self):
        gapTopPos = getRandomGapTopPosition()
        self._TopPipe = Pipe(gapTopPos, PipeType.TOP)
        self._BottomPipe = Pipe(gapTopPos, PipeType.BOTTOM)
        return

    def update(self, dt):
        self._TopPipe.update(dt)
        self._BottomPipe.update(dt)
        return