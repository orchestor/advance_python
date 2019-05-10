import collections
#    tuple with names. access value without index.
Card = collections.namedtuple('Card', ['rank', 'suit'])


class Deck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = ['spades diamonds clubs hearts'.split(' ', 1)

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]
    def __len__(self):
        return len(self._cards)
    def __getitem__(self, position):
        return self._cards[position]


if __name__ == '__main__':
             deck = Deck()
             print(len(deck))
