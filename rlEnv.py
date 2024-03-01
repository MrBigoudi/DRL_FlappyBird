from game import Game
import numpy as np

from constants import *

"""
A class representing an environment
attributes:
    - _Game: The game currently running
    - _ActionSpace: The possible actions for the agent
"""
class RlEnv:
    """
    Initiate the environment
    """
    def __init__(self):
        self._Game = Game()
        self._Game.init("flappyBird")
        self._ActionSpace = np.array([ActionType.DO_NOTHING, ActionType.JUMP])

    """
    Reset the environment
    return:
        - The initial observations
            The observations are as follows:
                - bird's position: min = 0, max = WINDOW_HEIGHT
                - bird's velocity: min = -inf, max = inf
                - distance to next pipe: min = 0, max = WINDOW_WIDTH // 2
                - position of next gap: min = 0, max = WINDOW_HEIGHT
                - boolean to tell if the bird is currently jumping
    """
    def reset(self):
        self._Game.reset()
        agent = self._Game._Agent

        birdPos = agent.rect.top
        birdVel = agent._Velocity
        distToNextPipe = WINDOW_WIDTH - agent.rect.left
        nextGapPos = FIRST_GAP_TOP
        isBirdJumping = False

        observations = [birdPos, birdVel, distToNextPipe, nextGapPos, isBirdJumping]
        return np.array(observations)

    """
    A step in the environment
    params:
        - action: The action taken by the agent
    return:
        - observations: The observations after execution of the action
        - reward: The reward after taking the action
        - terminated: True if the agent died
        - shouldQuit: True if the user closed the window
    """
    def step(self, action):
        return self._Game.step(action)

    """
    Free the environment
    """
    def close(self):
        self._Game.quit()
