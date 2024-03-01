import pygame
import random

from constants import *

from enum import Enum

from pygame.locals import (
    RLEACCEL,
)

"""
An enum to represent the type of the pipe either top or bottom
"""
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
    """
    Initiate a pipe
    params:
        - gapTopPos: The top position of the gap between the two pipes
        - pipeType: The type of the pipe (either the top pipe or the bottom pipe)
    """
    def __init__(self, gapTopPos, pipeType):
        super(Pipe, self).__init__()
        if pipeType == PipeType.TOP:
            self.initTop(gapTopPos)
        if pipeType == PipeType.BOTTOM:
            self.initBottom(gapTopPos)
        return

    """
    Initiate a top pipe
    params
        - gapTopPos: The top position of the gap between the two pipes
    """
    def initTop(self, gapTopPos):
        self.surf = pygame.image.load("media/sprites/pipe.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        size = (PIPE_WIDTH, PIPE_HEIGHT)
        self.surf = pygame.transform.scale(self.surf, size)
        self.rect = self.surf.get_rect(
            bottomleft=(WINDOW_WIDTH, gapTopPos)
        )
        return

    """
    Initiate a bottom pipe
    params
        - gapTopPos: The top position of the gap between the two pipes
    """
    def initBottom(self, gapTopPos):
        self.surf = pygame.image.load("media/sprites/pipe.png").convert()
        self.surf = pygame.transform.flip(self.surf, False, True) # flip bottom pipe
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        size = (PIPE_WIDTH, PIPE_HEIGHT)
        self.surf = pygame.transform.scale(self.surf, size)
        self.rect = self.surf.get_rect(
            topleft = (WINDOW_WIDTH, gapTopPos + PIPE_GAP_HEIGHT)
        )
        return

    """
    Update the pipe
    params:
        - dt: The delta time between the last frame
    """
    def update(self, dt):
        self.rect.move_ip(-SCROLLING_SPEED, 0)
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
    """
    Initiate the pair of pipes
    params:
        - gapTopPos: The top position of the gap between the two pipes
    """
    def __init__(self, gapTopPos = None):
        if gapTopPos is None:
            gapTopPos = self.getRandomGapTopPosition()
        self._TopPipe = Pipe(gapTopPos, PipeType.TOP)
        self._BottomPipe = Pipe(gapTopPos, PipeType.BOTTOM)
        return

    """
    Update the pipes
    params:
        - dt: The delta time between the last frame
    """
    def update(self, dt):
        self._TopPipe.update(dt)
        self._BottomPipe.update(dt)
        return

    """
    Get a random position for the top of the gap between the pipes
    return:
        - The random top position of the gap
    """
    def getRandomGapTopPosition(self):
        return random.randint(MIN_GAP_TOP, MAX_GAP_TOP)