from unittest import TestCase
from games.models import Card
from games.models import Suit
from games.models import FullDeck

class CardTestCase(TestCase):

    def test_suit(self):
        card = Card(10, Suit.CLUBS)
        self.assertEqual(10, card.number)
        self.assertEqual(Suit.CLUBS, card.suit)

class DeckTestCase(TestCase):

    def setUp(self):
        self.deck = FullDeck()

    def test_deck_size(self):
        self.assertEquals(52, len(self.deck))

    def test_shuffle(self):
        self.deck.shuffle()
        self.assertNotEqual(FullDeck().cards, self.deck.cards)
