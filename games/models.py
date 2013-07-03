import random


class Suit(object):
    HEARTS = 1
    CLUBS = 2
    SPADES = 3
    DIAMONDS = 4


class Face(object):
    ACE = 11
    JACK = 12
    QUEEN = 13
    KING = 14


class Card(object):
    def __init__(self, number, suit):
        self.number = number
        self.suit = suit

    def __eq__(self, other):
        if not isinstance(other, Card):
            return False
        return other.suit == self.suit and other.number == self.number


class FullDeck(object):

    def __init__(self):
        self.cards = []
        for number in xrange(1, Face.KING):
            self.cards.append(Card(number, Suit.CLUBS))
            self.cards.append(Card(number, Suit.DIAMONDS))
            self.cards.append(Card(number, Suit.SPADES))
            self.cards.append(Card(number, Suit.HEARTS))

    def __len__(self):
        return len(self.cards)

    def shuffle(self):
        random.shuffle(self.cards)
