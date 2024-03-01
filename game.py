import pygame
import constants

from agent import Agent
from pipe import PipePair
from background import Background

from pygame.locals import (
    QUIT,
)

"""
A class representing the game

attributes:
    _Window: the pygame window
    _WindowWidth: The window's width
    _WindowHeight: The window's height

    _Clock: The pygame timer
    _FPS: The target fps

    _ShouldQuit: A boolean to quit the game
    _BackgroundColor: The window's background color

    _Agent: The agent
    _Pipes: The pipes as a pygame group to handle collisions
    _AllSprites: All the sprites as a pygame group for rendering

    _ADD_PIPES_EVENT: A custom event
"""
class Game:
    """
    Empty constructor
    """
    def __init__(self):
        return

    """
    Init the game
    params:
        - title: The window's title
        - width: The window's width
        - height: The window's height
        - fps: The target fps
        - bgColor: The background color
    """
    def init(self, title, width = constants.WINDOW_WIDTH, height = constants.WINDOW_HEIGHT, fps = constants.TARGET_FPS):
        pygame.init()
        pygame.display.set_caption(title)
        self._Window = pygame.display.set_mode((width, height))
        self._WindowWidth = width
        self._WindowHeigth = height
        self._FPS = fps
        self._Clock = pygame.time.Clock()
        self._ShouldQuit = False

        self._Agent = Agent()
        self._Pipes = pygame.sprite.Group()
        self._Background = Background()

        self._AllSprites = pygame.sprite.Group()
        self._AllSprites.add(self._Background)
        self._AllSprites.add(self._Agent)

        self.initPipeApparitionEvent()

        return

    def initPipeApparitionEvent(self):
        # create custom event to make pipes appear
        self._ADD_PIPES_EVENT = pygame.USEREVENT + 1
        pygame.time.set_timer(self._ADD_PIPES_EVENT, constants.PIPE_APPARITION_SPEED)

    """
    The infinite game loop
    """
    def gameLoop(self):
        while not self._ShouldQuit:
            dt = self._Clock.tick(self._FPS) / 1000.0
            self.processEvents()
            self.processInputs()
            self.update(dt)
            self.draw()
        return

    """
    The events handler
    """
    def processEvents(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self._ShouldQuit = True
            if event.type == self._ADD_PIPES_EVENT:
                newPipes = PipePair()
                self._Pipes.add(newPipes._TopPipe)
                self._Pipes.add(newPipes._BottomPipe)
                self._AllSprites.add(newPipes._TopPipe)
                self._AllSprites.add(newPipes._BottomPipe)
        return

    """
    The input handler
    """
    def processInputs(self):
        pressedKeys = pygame.key.get_pressed()
        self._Agent.inputHandler(pressedKeys)

    """
    Handle collisions
    """
    def collisionsHandling(self):
        if pygame.sprite.spritecollideany(self._Agent, self._Pipes):
            self._Agent._IsAlive = False
        return
    

    """
    The update function
    params:
        - dt: The time elapsed since the last frame
    """
    def update(self, dt):
        # update the agent
        self._Agent.update(dt)
        self._Pipes.update(dt)
        self.collisionsHandling()

        if not self._Agent._IsAlive:
            self._ShouldQuit = True
        return

    """
    Draw on the screen
    """
    def draw(self):
        # draw background
        self._Window.fill(constants.BLACK)
        # draw the sprites
        for entity in self._AllSprites:
            self._Window.blit(entity.surf, entity.rect)
        # update the window
        pygame.display.flip()
        return

    """
    Quit and free the game
    """
    def quit(self):
        pygame.quit()
        return

    """
    Run the game
    """
    def run(self):
        self.gameLoop()
        self.quit()
        return

