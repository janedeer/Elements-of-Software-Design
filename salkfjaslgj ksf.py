
import random

class Card (object):
  RANKS = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)

  SUITS = ('C', 'D', 'H', 'S')

  # constructor
  def __init__ (self, rank = 12, suit = 'S'):
    if (rank in Card.RANKS):
      self.rank = rank
    else:
      self.rank = 12

    if (suit in Card.SUITS):
      self.suit = suit
    else:
      self.suit = 'S'

  # string representation of a Card object
  def __str__ (self):
    if (self.rank == 14):
      rank = 'A'
    elif (self.rank == 13):
      rank = 'K'
    elif (self.rank == 12):
      rank = 'Q'
    elif (self.rank == 11):
      rank = 'J'
    else:
      rank = str (self.rank)
    return rank + self.suit

  # equality tests
  def __eq__ (self, other):
    return self.rank == other.rank

  def __ne__ (self, other):
    return self.rank != other.rank

  def __lt__ (self, other):
    return self.rank < other.rank

  def __le__ (self, other):
    return self.rank <= other.rank

  def __gt__ (self, other):
    return self.rank > other.rank

  def __ge__ (self, other):
    return self.rank >= other.rank

class Deck (object):
  # constructor
  def __init__ (self, num_decks = 1):
    self.deck = []
    for i in range (num_decks):
      for suit in Card.SUITS:
        for rank in Card.RANKS:
          card = Card (rank, suit)
          self.deck.append (card)

  # shuffle the deck
  def shuffle (self):
    random.shuffle (self.deck)

  # deal a card
  def deal (self):
    if (len(self.deck) == 0):
      return None
    else:
      return self.deck.pop(0)

class Poker (object):
    # constructor
    def __init__ (self, num_players = 2, num_cards = 5):
        self.deck = Deck(5)
        self.deck.shuffle()
        self.all_hands = [[Card(2, "S"), Card(2, "C"), Card(2, "D"), \
                           Card(11, "S"), Card(11, "C")], [Card(4, "H"),\
                                                         Card(5, "H"), \
                                                         Card(6, "H"),
                           Card(7, "H"), Card(8, "H")] ]
                                            
        self.numCards_in_Hand = num_cards

  # simulate the play of poker
    def play (self):
    # sort the hands of each player and print
        for i in range(len(self.all_hands)):
            sorted_hand = sorted (self.all_hands[i], reverse = True)
            self.all_hands[i] = sorted_hand
            hand_str = ''
            for card in sorted_hand:
                hand_str = hand_str + str (card) + ' '
            print ('Player ' + str(i + 1) + ' : ' + hand_str)
        print()
        points_hand = []
        for i in range(len(self.all_hands)):
            if self.is_royal(self.all_hands[i])[0] != 0:
                print("Player ", i + 1, ": ", self.is_royal(self.all_hands[i])[1])
                points_hand.append(self.is_royal(self.all_hands[i])[0])
                
            elif self.is_straight_flush(self.all_hands[i])[0] != 0:
                print("Player ", i + 1, ": ", self.is_straight_flush(self.all_hands[i])[1])
                points_hand.append(self.is_straight_flush(self.all_hands[i])[0])
                
            elif self.is_four_kind(self.all_hands[i])[0] != 0:
                print("Player ", i + 1, ": ", self.is_four_kind(self.all_hands[i])[1])
                points_hand.append(self.is_four_kind(self.all_hands[i])[0])
                
            elif self.is_full_house(self.all_hands[i])[0] != 0:
                print("Player ", i + 1, ": ", self.is_full_house(self.all_hands[i])[1])
                points_hand.append(self.is_full_house(self.all_hands[i])[0])
                
            elif self.is_flush(self.all_hands[i])[0] != 0:
                print("Player ", i + 1, ": ", self.is_flush(self.all_hands[i])[1])
                points_hand.append(self.is_flush(self.all_hands[i])[0])
                
            elif self.is_straight(self.all_hands[i])[0] != 0:
                print("Player ", i + 1, ": ", self.is_straight(self.all_hands[i])[1])
                points_hand.append(self.is_straight(self.all_hands[i])[0])
                
            elif self.is_three_kind(self.all_hands[i])[0] != 0:
                print("Player ", i + 1, ": ", self.is_three_kind(self.all_hands[i])[1])
                points_hand.append(self.is_three_kind(self.all_hands[i])[0])
                
            elif self.is_two_pair(self.all_hands[i])[0] != 0:
                print("Player ", i + 1, ": ", self.is_two_pair(self.all_hands[i])[1])
                points_hand.append(self.is_two_pair(self.all_hands[i])[0])
                
            elif self.is_one_pair(self.all_hands[i])[0] != 0:
                print("Player ", i + 1, ": ", self.is_one_pair(self.all_hands[i])[1])
                points_hand.append(self.is_one_pair(self.all_hands[i])[0])
                
            else:
                print("Player ", i + 1, ": ", self.is_high_card(self.all_hands[i])[1])
                points_hand.append(self.is_high_card(self.all_hands[i])[0])
        
        winner_points = max(points_hand)
        print()
        winner = points_hand.index(winner_points)
        print("Player ", winner + 1, " wins.")
    
    

 
  # determine if a hand is a royal flush
  # takes as argument a list of 5 Card objects
  # returns a number (points) for that hand
    def is_royal (self, hand):
        same_suit = True
        for i in range (len(hand) - 1):
            same_suit = same_suit and (hand[i].suit == hand[i + 1].suit)

        if (not same_suit):
            return 0, ''

        rank_order = True
        for i in range (len(hand)):
            rank_order = rank_order and (hand[i].rank == 14 - i)

        if (not rank_order):
            return 0, ''

        c1, c2, c3, c4, c5 = hand[0].rank, hand[1].rank, \
                             hand[2].rank, hand[3].rank, hand[4].rank
        h = 10
        points = h*15**5 + c1*15**4 + c2*15**3 + c3*15**2 + c4*15 + c5

        return points, "Royal Flush"

    def is_straight_flush (self, hand):
        same_suit = True
        for i in range(len(hand) - 1):
            same_suit = same_suit and (hand[i].suit == hand[i + 1].suit)

        if (not same_suit):
            return 0, ''

        rank_order = True
        for i, card in enumerate(hand):
            rank_order = rank_order and (card.rank == hand[i + 1].rank - 1)

        if (not rank_order):
            return 0, ''

        c1, c2, c3, c4, c5 = hand[0].rank, hand[1].rank, \
                             hand[2].rank, hand[3].rank, hand[4].rank
        h = 9
        points = h*15**5 + c1*15**4 + c2*15**3 + c3*15**2 + c4*15 + c5

        return points, "Straight Flush"
    

    def is_four_kind (self, hand):
        freq = {}
        four_kind = 0
        for i, card in enumerate(hand):
            if card.rank in freq:
                freq[card.rank] += 1
            else:
                freq[card.rank] = 1
        c1 = 0
        c5 = 0
        for key, count in freq.items():
            if count == 4:
                four_kind += 1
                c1 = key
            else:
                c5 = key
                
        if four_kind == 1:
            h = 8
            points = h*15**5 + c1*15**4 + c1*15**3 + c1*15**2 + c1*15 + c5
            return points, "Four of a Kind"

        else:
            return 0, ""
                
            

    def is_full_house (self, hand):
        freq = {}
        three_kind = 0
        pairs = 0
        for i, card in enumerate(hand):
            if card.rank in freq:
                freq[card.rank] += 1
            else:
                freq[card.rank] = 1

        three_pair = []
        two_pair = []
        for key, count in freq.items():
            if count == 3:
                three_kind += 1
                three_pair.append(key)
            elif count == 2:
                pairs += 1
                two_pair.append(key)

        if three_kind == 1 and pairs == 1:
            c1 = three_pair[0]
            c2 = three_pair[0]
            c3 = three_pair[0]
            c4 = two_pair[0]
            c5 = two_pair[0]
            h = 7
            points = h*15**5 + c1*15**4 + c2*15**3 + c3*15**2 + c4*15 + c5
            return points, "Full House"
        else:
            return 0, ""
            
    def is_flush (self, hand):
        same_suit = True
        for i in range(len(hand) - 1):
            same_suit = same_suit and (hand[i].suit == hand[i + 1].suit)

        if not (same_suit):
            return 0, ''

        c1, c2, c3, c4, c5 = hand[0].rank, hand[1].rank, \
                             hand[2].rank, hand[3].rank, hand[4].rank
        h = 6
        points = h*15**5 + c1*15**4 + c2*15**3 + c3*15**2 + c4*15 + c5
        return points, "Flush"


    def is_straight (self, hand):
        rank_order = True
        for i in range(len(hand) - 1):
            rank_order = rank_order and (hand[i].rank == hand[i + 1].rank - 1)

        if (not rank_order):
            return 0, ''

        c1, c2, c3, c4, c5 = hand[0].rank, hand[1].rank, \
                             hand[2].rank, hand[3].rank, hand[4].rank
        h = 5
        points = h*15**5 + c1*15**4 + c2*15**3 + c3*15**2 + c4*15 + c5
        return points, "Straight"
    
    def is_three_kind (self, hand):
        freq = {}
        for i, card in enumerate(hand):
            if card.rank in freq:
                freq[card.rank] += 1
            else:
                freq[card.rank] = 1
        three_kind = 0

        not_three_kind = []
        c1 = 0
        for key, count in freq.items():
            if count == 3:
                three_kind += 1
                c1 = key
            else:
                not_three_kind.append(key)

        if three_kind == 1:
            c4 = not_three_kind[0]
            c5 = not_three_kind[1]
            h = 4
            points = h*15**5 + c1*15**4 + c1*15**3 + c1*15**2 + c4*15 + c5
            return points, "Three of a Kind"

        else:
            return 0, ""
    

    def is_two_pair (self, hand):
        freq = {}
        for i, card in enumerate(hand):
            if card.rank in freq:
                freq[card.rank] += 1
            else:
                freq[card.rank] = 1
        pairs = 0

        c5 = 0
        has_two_pair = []
        for key, count in freq.items():
            if count == 2:
                pairs += 1
                has_two_pair.append(key)
            else:
                c5 = key
                
        sorted(has_two_pair, reverse = True)
        
        if pairs == 2:
            c1 = has_two_pair[0]
            c2 = has_two_pair[0]
            c3 = has_two_pair[1]
            c4 = has_two_pair[1]
            h = 3
            points = h*15**5 + c1*15**4 + c2*15**3 + c3*15**2 + c4*15 + c5
            return points, "Two Pair"

        else:
            return 0, ""

  # determine if a hand is one pair
  # takes as argument a list of 5 Card objects
  # returns the number of points for that hand
    def is_one_pair (self, hand):
        freq = {}
        for i, card in enumerate(hand):
            if card.rank in freq:
                freq[card.rank] += 1
            else:
                freq[card.rank] = 1
        pairs = 0

        has_pair = []
        has_no_pair = []
        for key, count in freq.items():
            if count == 2:
                pairs += 1
                has_pair.append(key)
            else:
                has_no_pair.append(key)

        if pairs == 1:
            c1 = has_pair[0]
            c2 = has_pair[0]
            c3 = has_no_pair[0]
            c4 = has_no_pair[1]
            c5 = has_no_pair[2]
            h = 2
            points = h*15**5 + c1*15**4 + c2*15**3 + c3*15**2 + c4*15 + c5
            return points, "One Pair"

        else:
            return 0, ""

    def is_high_card (self, hand):
        high = hand[0].rank
        c1, c2, c3, c4, c5 = hand[0].rank, hand[1].rank, \
                             hand[2].rank, hand[3].rank, hand[4].rank
        h = 1
        points = h*15**5 + c1*15**4 + c2*15**3 + c3*15**2 + c4*15 + c5
        return points, "High Card"
            
def main():
  # prompt the user to enter the number of plaers
  num_players = int (input ('Enter number of players: '))
  while ((num_players < 2) or (num_players > 6)):
    num_players = int (input ('Enter number of players: '))

  # create the Poker object
  game = Poker (num_players)

  # play the game
  game.play()

main()

