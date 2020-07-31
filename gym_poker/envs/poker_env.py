"""
Gym envirnoments for poker ai
versions: [0, ]
"""
import gym

from gym_poker.envs.poker import Card, Deck, Ranks

_, _, _ = Card, Deck, Ranks

class PokerEnvV0(gym.Env):
    """
    Gym envirnoment for poker ai
    version: 0
    [Summary]
    - The env will not provide other player's action.
    - An opposing player will play the game with random action.
    """
    metadata = {'render.modes': ['human', 'rgb_array']}

    def __init__(self, player_n=3):
        assert 2 <= player_n < 12
        self._deck = Deck()

        self.player_n = player_n
        self.observation_space = None
        self.action_space = None

    def step(self, action):
        state = None
        done = False
        reward = 0

        return state, reward, done, {}

    def reset(self):
        state = None

        return state

    def render(self, mode='human'):
        pass
