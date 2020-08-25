"""Players in poker game."""
from abc import ABC, abstractmethod
from gym.spaces import Discrete, Tuple, Box


class BasePlayer(ABC):
    """Abstract Class for poker player"""
    ACTION_SPACE = Tuple((Discrete(3), Box(low=0, high=1, shape=(1,))))

    def __init__(self, stack: float):
        self.stack = stack
        self.alive = True
        self.all_in = False

    @abstractmethod
    def action(self, information) -> Tuple:
        """Get action of player for given information"""

    @property
    def stack(self) -> float:
        """Property for member variable: stack"""
        return self.stack


class RandomPlayer(BasePlayer):
    """Create action randomly"""

    def __init__(self, stack):
        super(RandomPlayer, self).__init__(stack=stack)

    def action(self, information):
        _ = information
        return self.ACTION_SPACE.sample()


class ModelPlayer(BasePlayer):
    """Create action from some model"""

    class ModelNotFound(Exception):
        """Exception for trying to use unregistered model."""

    def __init__(self, stack):
        super(ModelPlayer, self).__init__(stack=stack)
        self._model = None

    def action(self, information):
        if self._model is None:
            raise ModelPlayer.ModelNotFound
        elif not hasattr(self._model, 'step'):
            raise AttributeError

        return self._model.step(information)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
