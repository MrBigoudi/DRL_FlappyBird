import pygame
import numpy as np

from constants import *

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

    _FirstPipeTriggered: A boolean to have a deterministic first pipe
    _ShouldQuit: A boolean to quit the game
    _Background: The window's background

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
    """
    def init(self, title, width = WINDOW_WIDTH, height = WINDOW_HEIGHT, fps = TARGET_FPS):
        pygame.init()
        pygame.display.set_caption(title)
        self._Window = pygame.display.set_mode((width, height))
        self._WindowWidth = width
        self._WindowHeigth = height
        self._FPS = fps
        self.initPipeApparitionEvent()
        self.reset()
        return

    """
    Reset the game attributes
    """
    def reset(self):
        self._Clock = pygame.time.Clock()
        self._ShouldQuit = False
        self._FirstPipeTriggered = False
        self._Agent = Agent()
        self._Pipes = pygame.sprite.Group()
        self._Background = Background()
        self._AllSprites = pygame.sprite.Group()
        self._AllSprites.add(self._Background)
        self._AllSprites.add(self._Agent)
        return

    """
    Initiate the pipe generation event
    """
    def initPipeApparitionEvent(self):
        # create custom event to make pipes appear
        self._ADD_PIPES_EVENT = pygame.USEREVENT + 1
        pygame.time.set_timer(self._ADD_PIPES_EVENT, PIPE_APPARITION_SPEED)

    """
    The events handler
    """
    def processEvents(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self._ShouldQuit = True
            if event.type == self._ADD_PIPES_EVENT:
                newPipes = 0
                if not self._FirstPipeTriggered:
                    newPipes = PipePair(FIRST_GAP_TOP)
                    self._FirstPipeTriggered = True
                else:
                    newPipes = PipePair()
                self._Pipes.add(newPipes._TopPipe)
                self._Pipes.add(newPipes._BottomPipe)
                self._AllSprites.add(newPipes._TopPipe)
                self._AllSprites.add(newPipes._BottomPipe)
        return

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
        return

    """
    Draw on the screen
    """
    def draw(self):
        self._Window.fill(BLACK)
        for entity in self._AllSprites:
            self._Window.blit(entity.surf, entity.rect)
        pygame.display.flip()
        return

    """
    Quit and free the game
    """
    def quit(self):
        pygame.quit()
        return


    """
    Get the observations from the current game state
    return:
        - bird's position: min = 0, max = WINDOW_HEIGHT
        - bird's velocity: min = -inf, max = inf
        - distance to next pipe: min = 0, max = WINDOW_WIDTH // 2
        - position of next gap: min = 0, max = WINDOW_HEIGHT
        - boolean to tell if the bird is currently jumping
    """
    def getObservations(self):
        agent = self._Agent
        birdPos = agent.rect.top
        birdVel = agent._Velocity
        distToNextPipe = WINDOW_WIDTH - agent.rect.left
        nextGapPos = FIRST_GAP_TOP

        pipes = self._Pipes.sprites()    
        if len(pipes) > 0:
            lastPipe = pipes[-1]
            # if last pipe is not behind bird, then get the distance
            if lastPipe.rect.left >= agent.rect.left:
                distToNextPipe = lastPipe.rect.left - agent.rect.left
            # update next gap pos if there is at least one pipe on screen
            nextGapPos = lastPipe.rect.top - PIPE_GAP_HEIGHT # last pipe is a bottom pipe
        
        isBirdJumping = agent._IsJumping
        observations = [birdPos, birdVel, distToNextPipe, nextGapPos, isBirdJumping]
        return np.array(observations)

    """
    Get the reward
    For now it is a basic reward because, we just want to keep the bird alive as much as possible
    so we add +1 every step
    """
    def getReward(self):
        return 1

    """
    A step in the game
    params:
        - action: The action taken by the agent
    return:
        - observations: The observations after execution of the action
        - reward: The reward after taking the action
        - terminated: True if the agent died
        - shouldQuit: True if the user closed the window
    """
    def step(self, action):
        if self._ShouldQuit:
            return (np.array([]), 0, False, True)

        dt = self._Clock.tick(self._FPS) / 1000.0
        self.processEvents()
        if action == ActionType.JUMP:
            self._Agent.jump()      
        self.update(dt)
        self.draw()
        return (self.getObservations(), self.getReward(), not self._Agent._IsAlive, self._ShouldQuit)


