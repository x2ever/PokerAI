"""Deck for poker game."""
import random
from typing import List
from gym_poker.envs.poker.card import Card

class Deck:
    """
    Deck object that shuffles and distributes cards.
    """
    def __init__(self):
        self.sample_cards = [Card(i // 13, i % 13) for i in range(52)]

        self._suffled_cards = self.sample_cards.copy()
        random.shuffle(self._suffled_cards)

    def pop(self, pop_n: int = 1) -> List[Card]:
        """
        >>> deck = Deck()
        >>> len(deck)
        52
        >>> type(deck.pop())
        <class 'list'>
        >>> len(deck.pop())
        1
        >>> type(deck.pop(pop_n=10))
        <class 'list'>
        >>> len(deck.pop(pop_n=10))
        10
        >>> len(deck)
        30
        >>> deck.pop(pop_n=35)
        Traceback (most recent call last):
        ...
        AssertionError
        """

        assert pop_n <= len(self)
        data = self._suffled_cards[:pop_n]
        self._suffled_cards = self._suffled_cards[pop_n:]
        return data

    def __len__(self):
        """
        get length of shuffled cards(left cards)
        """
        return len(self._suffled_cards)

    def reset(self):
        """
        Reset deck and re-shuffle it.
        """
        self.__init__()

if __name__ == "__main__":
    import doctest
    doctest.testmod()
