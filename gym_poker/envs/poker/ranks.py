"""Ranks for poker game."""
# pylint: disable=C0301
from typing import List
from gym_poker.envs.poker.card import Card


class Ranks:
    """
    Define Ranks in poker and find a winners.
    """

    @staticmethod
    def get_winners(cards_dummy: List[List[Card]]):
        """
        >>> ranks = Ranks()
        >>> data1 = [Card(1, 1), Card(1, 2), Card(1, 3), Card(1, 4), Card(1, 5), Card(2, 3), Card(2, 4)]
        >>> data1
        [DAIMOND 3, DAIMOND 4, DAIMOND 5, DAIMOND 6, DAIMOND 7, HEART 5, HEART 6]
        >>> data2 = [Card(0, 1), Card(1, 1), Card(2, 1), Card(3, 1), Card(2, 2), Card(2, 3), Card(2, 4)]
        >>> data2
        [SPADE 3, DAIMOND 3, HEART 3, CLOVER 3, HEART 4, HEART 5, HEART 6]
        >>> ranks.get_winners([data1, data2]) # straight_flush vs fourcard
        [0]
        >>> data3 = [Card(1, 2), Card(1, 4), Card(1, 5), Card(1, 9), Card(1, 12), Card(2, 3), Card(2, 4)]
        >>> data3
        [DAIMOND 4, DAIMOND 6, DAIMOND 7, DAIMOND J, DAIMOND A, HEART 5, HEART 6]
        >>> data4 = [Card(1, 2), Card(1, 4), Card(1, 5), Card(1, 9), Card(1, 12), Card(2, 11), Card(2, 12)]
        >>> data4
        [DAIMOND 4, DAIMOND 6, DAIMOND 7, DAIMOND J, DAIMOND A, HEART K, HEART A]
        >>> ranks.get_winners([data3, data4]) # A flush vs A flush
        [0, 1]
        """
        def check_ranks(rank_function, cards_dummy):
            results = [[i, rank_function(cards)] for i, cards in enumerate(cards_dummy)]
            max_sub_rank = max(results, key=lambda x: x[1])[1]
            max_sub_rank = None if max_sub_rank == -1 else max_sub_rank
            temp = []
            for idx, sub_rank in results:
                if sub_rank == max_sub_rank:
                    temp.append(idx)

            return temp

        check_functions = [
            Ranks.check_straight_flush, Ranks.check_four_card,
            Ranks.check_full_house, Ranks.check_flush, Ranks.check_straight,
            Ranks.check_three_card, Ranks.check_two_pair, Ranks.check_one_pair,
            Ranks.check_high_card
            ]

        for check_function in check_functions:
            result = check_ranks(check_function, cards_dummy)
            if result:
                return result
        return result

    @staticmethod
    def check_four_card(cards: List[Card]):
        """
        >>> ranks = Ranks()
        >>> data = [Card(1, 1), Card(2, 1), Card(3, 1), Card(2, 9), Card(0, 12), Card(1, 8), Card(0, 1)]
        >>> data
        [DAIMOND 3, HEART 3, CLOVER 3, HEART J, SPADE A, DAIMOND 10, SPADE 3]
        >>> ranks.check_four_card(data)
        1
        """
        assert len(cards) == 7

        memos = [0 for _ in range(13)]
        for card in cards:
            memos[card.number] += 1

        for i in range(12, -1, -1):
            if memos[i] == 4:
                return i
        return -1

    @staticmethod
    def check_full_house(cards: List[Card]):
        """
        >>> ranks = Ranks()
        >>> data = [Card(1, 2), Card(2, 3), Card(3, 2), Card(3, 3), Card(0, 12), Card(1, 8), Card(0, 2)]
        >>> data
        [DAIMOND 4, HEART 5, CLOVER 4, CLOVER 5, SPADE A, DAIMOND 10, SPADE 4]
        >>> ranks.check_full_house(data)
        2
        """
        assert len(cards) == 7

        memos = [0 for _ in range(13)]
        for card in cards:
            memos[card.number] += 1

        if 2 not in memos or 3 not in memos:
            return -1

        for i in range(12, -1, -1):
            if memos[i] == 3:
                return i
        return -1

    @staticmethod
    def check_three_card(cards: List[Card]):
        """
        >>> ranks = Ranks()
        >>> data = [Card(1, 2), Card(2, 3), Card(3, 2), Card(3, 3), Card(0, 12), Card(1, 8), Card(0, 2)]
        >>> data
        [DAIMOND 4, HEART 5, CLOVER 4, CLOVER 5, SPADE A, DAIMOND 10, SPADE 4]
        >>> ranks.check_three_card(data)
        2
        """
        assert len(cards) == 7

        memos = [0 for _ in range(13)]
        for card in cards:
            memos[card.number] += 1

        for i in range(12, -1, -1):
            if memos[i] == 3:
                return i
        return -1

    @staticmethod
    def check_two_pair(cards: List[Card]):
        """
        >>> ranks = Ranks()
        >>> data = [Card(1, 2), Card(2, 3), Card(3, 2), Card(3, 3), Card(0, 12), Card(1, 8), Card(0, 10)]
        >>> data
        [DAIMOND 4, HEART 5, CLOVER 4, CLOVER 5, SPADE A, DAIMOND 10, SPADE Q]
        >>> ranks.check_two_pair(data)
        [3, 2]
        >>> data = [Card(1, 2), Card(2, 3), Card(3, 2), Card(3, 3), Card(0, 12), Card(1, 8), Card(0, 12)]
        >>> data
        [DAIMOND 4, HEART 5, CLOVER 4, CLOVER 5, SPADE A, DAIMOND 10, SPADE A]
        >>> ranks.check_two_pair(data)
        [12, 3]
        """
        assert len(cards) == 7

        memos = [0 for _ in range(13)]
        for card in cards:
            memos[card.number] += 1

        temp = []
        for i in range(12, -1, -1):
            if memos[i] == 2:
                temp.append(i)

        if len(temp) >= 2:
            return temp[:2]

        return -1

    @staticmethod
    def check_one_pair(cards: List[Card]):
        """
        >>> ranks = Ranks()
        >>> data = [Card(1, 2), Card(2, 3), Card(3, 2), Card(3, 3), Card(0, 12), Card(1, 8), Card(0, 10)]
        >>> data
        [DAIMOND 4, HEART 5, CLOVER 4, CLOVER 5, SPADE A, DAIMOND 10, SPADE Q]
        >>> ranks.check_one_pair(data)
        3
        >>> data = [Card(1, 2), Card(2, 3), Card(3, 2), Card(3, 3), Card(0, 12), Card(1, 8), Card(0, 12)]
        >>> data
        [DAIMOND 4, HEART 5, CLOVER 4, CLOVER 5, SPADE A, DAIMOND 10, SPADE A]
        >>> ranks.check_one_pair(data)
        12
        """
        assert len(cards) == 7

        memos = [0 for _ in range(13)]
        for card in cards:
            memos[card.number] += 1

        for i in range(12, -1, -1):
            if memos[i] == 2:
                return i

        return -1

    @staticmethod
    def check_high_card(cards: List[Card]):
        """
        >>> ranks = Ranks()
        >>> data = [Card(1, 2), Card(2, 3), Card(3, 2), Card(3, 3), Card(0, 12), Card(1, 8), Card(0, 10)]
        >>> data
        [DAIMOND 4, HEART 5, CLOVER 4, CLOVER 5, SPADE A, DAIMOND 10, SPADE Q]
        >>> ranks.check_high_card(data)
        12
        """
        assert len(cards) == 7

        memos = [0 for _ in range(13)]
        for card in cards:
            memos[card.number] += 1

        for i in range(12, -1, -1):
            if memos[i] == 1:
                return i

        return -1

    @staticmethod
    def check_straight(cards: List[Card]):
        """
        >>> ranks = Ranks()
        >>> data = [Card(1, 2), Card(2, 3), Card(3, 4), Card(3, 5), Card(0, 6), Card(1, 8), Card(0, 10)]
        >>> data
        [DAIMOND 4, HEART 5, CLOVER 6, CLOVER 7, SPADE 8, DAIMOND 10, SPADE Q]
        >>> ranks.check_straight(data)
        6
        >>> data = [Card(1, 12), Card(2, 0), Card(3, 1), Card(3, 2), Card(0, 3), Card(1, 8), Card(0, 10)]
        >>> data
        [DAIMOND A, HEART 2, CLOVER 3, CLOVER 4, SPADE 5, DAIMOND 10, SPADE Q]
        >>> ranks.check_straight(data)
        3
        """
        assert len(cards) == 7

        memos = [0 for _ in range(13)]
        for card in cards:
            memos[card.number] += 1

        memos.insert(0, memos[-1])

        count = 0
        for i in range(13, -1, -1):
            if memos[i] != 0:
                count += 1
                if count == 5:
                    return i + 3
            else:
                count = 0

        return -1

    @staticmethod
    def check_straight_flush(cards: List[Card]):
        """
        >>> ranks = Ranks()
        >>> data = [Card(1, 2), Card(2, 3), Card(3, 4), Card(3, 5), Card(0, 6), Card(1, 8), Card(0, 10)]
        >>> data
        [DAIMOND 4, HEART 5, CLOVER 6, CLOVER 7, SPADE 8, DAIMOND 10, SPADE Q]
        >>> ranks.check_straight_flush(data)
        -1
        >>> data = [Card(1, 12), Card(1, 0), Card(1, 1), Card(1, 2), Card(1, 3), Card(1, 8), Card(0, 10)]
        >>> data
        [DAIMOND A, DAIMOND 2, DAIMOND 3, DAIMOND 4, DAIMOND 5, DAIMOND 10, SPADE Q]
        >>> ranks.check_straight_flush(data)
        3
        """
        assert len(cards) == 7

        memos = [[0 for _ in range(13)] for _ in range(4)]
        for card in cards:
            memos[card.pattern][card.number] = 1

        for number_memos in memos:
            number_memos.insert(0, number_memos[-1])

        for i in range(4):
            count = 0
            for j in range(13, -1, -1):
                if memos[i][j] == 1:
                    count += 1
                    if count == 5:
                        return j + 3
                else:
                    count = 0

        return -1

    @staticmethod
    def check_flush(cards: List[Card]):
        """
        >>> ranks = Ranks()
        >>> data = [Card(1, 2), Card(2, 3), Card(3, 4), Card(3, 5), Card(0, 6), Card(1, 8), Card(0, 10)]
        >>> data
        [DAIMOND 4, HEART 5, CLOVER 6, CLOVER 7, SPADE 8, DAIMOND 10, SPADE Q]
        >>> ranks.check_flush(data)
        -1
        >>> data = [Card(3, 12), Card(3, 0), Card(3, 1), Card(3, 2), Card(3, 3), Card(1, 8), Card(3, 10)]
        >>> data
        [CLOVER A, CLOVER 2, CLOVER 3, CLOVER 4, CLOVER 5, DAIMOND 10, CLOVER Q]
        >>> ranks.check_flush(data)
        [12, 10, 3, 2, 1]
        """
        assert len(cards) == 7

        memos = [[0 for _ in range(13)] for _ in range(4)]
        for card in cards:
            memos[card.pattern][card.number] = 1

        for i in range(4):
            if sum(memos[i]) >= 5:
                temp = []
                for j in range(12, -1, -1):
                    if memos[i][j] == 1:
                        temp.append(j)
                        if len(temp) == 5:
                            return temp

        return -1


if __name__ == "__main__":
    import doctest
    doctest.testmod()
