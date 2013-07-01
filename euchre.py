from random import shuffle

cards = []
rank = ["9", "10", "J", "Q", "K", "A"]
player1 = []
player2 = []
player3 = []
player4 = []


def deck():
    for c in xrange(9, 15):
        cards[len(cards):] = [{rank[c-9]: c, "c": "clubs"},
                              {rank[c-9]: c, "d": "diamonds"},
                              {rank[c-9]: c, "h": "hearts"},
                              {rank[c-9]: c, "s": "spades"}]


def deal():
    global player1
    global player2
    global player3
    global player4

    deck() # Should be moved to engine. Also need add returns to each function to push engine on.
    shuffle(cards)

    player1 = cards[:5]
    player2 = cards[5:10]
    player3 = cards[10:15]
    player4 = cards[15:20]


def declare_trump():

# Need to somehow loop through each player to decide trump. Create some kind of condition to 
# determine whether player orders up. Also need to add interactive mode for player4 to order up.
# If no one orders up, misdeal is declared and cards are redealt.





    set_trump(player1, trump_suit)
    set_trump(player2, trump_suit)
    set_trump(player3, trump_suit)
    set_trump(player4, trump_suit)
    pass


def set_trump(player, suit):
    for t in xrange(5):
        if suit in player[t]:
            for c in xrange(5):
                if player[t].get(rank[c]):
                    player[t][rank[c]] += 10

            # Sets the right bower.
            if 'J' in player[t]:
                player[t]['J'] += 5

        # Sets the left bower.
        if suit == 'c':
            opposite_suit = 's'
        elif suit == 'd':
            opposite_suit = 'h'
        elif suit == 's':
            opposite_suit = 'c'
        else:
            opposite_suit = 'd'

        if opposite_suit in player[t]:
            if 'J' in player[t]:
                player[t]['J'] += 14
