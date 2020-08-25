"""Card for poker game."""


class Card(int):
    """
    Card object to play in poker game.

    [Doctest]
    >>> card = Card(3, 4)
    >>> card
    CLOVER 6
    >>> int(card)
    43
    """
    PATTERNS = ["SPADE", "DAIMOND", "HEART", "CLOVER"]
    NUMBERS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

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

    @property
    def number(self):
        """Property for self._number"""
        return self._number

    @property
    def pattern(self):
        """Property for self._pattern"""
        return self._pattern


if __name__ == "__main__":
    import doctest
    doctest.testmod()
