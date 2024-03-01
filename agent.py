import pygame
import constants

from pygame.locals import (
    K_SPACE,
)

"""
A class representing the agent

attributes:
    surf: The surface of the agent
    rect: The rectangle of the agent

    _IsAlive: Boolean to check if the agent is alive
"""
class Agent(pygame.sprite.Sprite):
    """
    Instantiate the agent
    """
    def __init__(self):
        super(Agent, self).__init__()
        self.surf = pygame.image.load("media/sprites/bird.png").convert_alpha()
        self.surf = pygame.transform.scale(self.surf, constants.AGENT_SIZE)
        self.rect = self.surf.get_rect()
        self.center(constants.WINDOW_WIDTH, constants.WINDOW_HEIGHT)
        self._IsAlive = True

        self._Velocity = 0
        self._IsJumping = False
        self._Mass = constants.BIRD_MASS

    """
    The input handler

    params:
        - pressedKeys: A dictionary containing the keys pressed at the beginning of every frame
    """
    def inputHandler(self, pressedKeys):
        if pressedKeys[K_SPACE] and not self._IsJumping:
            self.jump()

    def jump(self):
        self._Velocity = -constants.BIRD_FLY_VEL
        self._IsJumping = True

    """
    Center the agent

    params:
        - windowWidth: The window's width
        - windowHeight: The window's height
    """
    def center(self, windowWidth, windowHeight):
        surfCenter = (
            (windowWidth - self.surf.get_width()) / 2,
            (windowHeight - self.surf.get_height()) / 2
        )
        self.rect.move_ip(surfCenter)
        return

    """
    Check if the agent is dead
    """
    def checkDeath(self):
        if self.rect.top <= 0:
            self._IsAlive = False
        if self.rect.bottom >= constants.WINDOW_HEIGHT:
            self._IsAlive = False
        return

    """
    Update the agent

    params:
        - dt: The delta time since the last frame
    """
    def update(self, dt):
        # TODO:
        self._Velocity += constants.GRAVITY * self._Mass
        self.rect.move_ip(0, self._Velocity)

        if(self._Velocity > 0):
            self._IsJumping = False

        self.checkDeath()
        return

