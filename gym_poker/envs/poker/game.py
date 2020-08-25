from gym_poker.envs.poker import BasePlayer
from typing import List


class Game:
    def __init__(self, players: List[BasePlayer]):
        self.players = players
        self.size = len(self.players)
        self._blind_idx = 0
        self._idx = (self.blind_idx + 2) % self.size
        self._information = None

    def proceed(self):

        player = self.players[self._idx]
        player.action(self._information)


