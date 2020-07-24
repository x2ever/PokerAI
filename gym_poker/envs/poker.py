"""
Objects for poker game.
"""
import random
from typing import List


class Card(int):
    """
    Card object to play in poker game.

    [Doctest]
    >>> card = Card(3, 4)
    >>> card
    CLOVER 5
    >>> int(card)
    43
    """
    PATTERNS = ["SPADE", "DAIMOND", "HEART", "CLOVER"]
    NUMBERS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    def __init__(self, pattern: int, number: int):
        self._pattern = pattern
        self._number = number
        super(Card, self).__init__()

    def __new__(cls, pattern: int, number: int):
        assert 0 <= pattern < 4
        assert 0 <= number < 13
        return super(Card, cls).__new__(cls, pattern * 13 + number)

    def __str__(self):
        return f"{Card.PATTERNS[self._pattern]} {Card.NUMBERS[self._number]}"

    def __repr__(self):
        return f"{Card.PATTERNS[self._pattern]} {Card.NUMBERS[self._number]}"


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
