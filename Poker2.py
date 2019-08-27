import random

#Create the object card so we can generate the cards, and let python know what they are!
class Card (object):
RANKS = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)

SUITS = ('C', 'D', 'H', 'S')

#Define rank and suit
def __init__ (self, rank = 12, suit = 'S'):
    if (rank in Card.RANKS):
      self.rank = rank
    else:
      self.rank = 12
  
    if (suit in Card.SUITS):
      self.suit = suit
    else:
      self.suit = 'S'

#Give Jack, Queen, King and Ace numerical values.
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

def __eq__ (self, other):
    return (self.rank == other.rank)

def __ne__ (self, other):
    return (self.rank != other.rank)

def __lt__ (self, other):
    return (self.rank < other.rank)

def __le__ (self, other):
    return (self.rank <= other.rank)

def __gt__ (self, other):
    return (self.rank > other.rank)

def __ge__ (self, other):
    return (self.rank >= other.rank)

#Create the object Deck so we can generate the actual deck!
class Deck (object):
def __init__ (self):
    self.deck = []
    for suit in Card.SUITS:
      for rank in Card.RANKS:
        card = Card (rank, suit)
        self.deck.append (card)

#Shuffle Deck
def shuffle (self):
    random.shuffle (self.deck)

#Deal Deck
def deal (self):
    if (len(self.deck) == 0):
      return None
    else:
      return self.deck.pop(0)

#Create Object Poker to simulate the game
class Poker (object):
def __init__ (self, num_players):
    self.deck = Deck()
    self.deck.shuffle()
    self.players = []
    numcards_in_hand = 5

    #Deal each player their hand
    for i in range (num_players):
      hand = []
      for j in range (numcards_in_hand):
        hand.append (self.deck.deal())
      self.players.append (hand)

#Play!
def play (self):
    # sort the hands of each player and print
    for i in range (len(self.players)):
      sortedHand = sorted (self.players[i], reverse = True)
      self.players[i] = sortedHand
      hand = ''
      for card in sortedHand:
        hand = hand + str (card) + ' '
      print ('Player ' + str (i + 1) + " : " + hand)

    #create list of points
    points_hand = [] # create list to store points for each hand

    #Find points for each hand and add them to list
    for i in range (len(self.players)):
    
      if self.is_royal(self.players[i]) != 0:
        points_hand.append(self.is_royal(self.players[i]))

      elif self.is_straight_flush(self.players[i]) != 0:
        points_hand.append(self.is_straight_flush(self.players[i]))

      elif self.is_four_kind(self.players[i]) != 0:
        points_hand.append(self.is_four_kind(self.players[i]))

      elif self.is_full_house(self.players[i]) != 0:
        points_hand.append(self.is_full_house(self.players[i]))

      elif self.is_flush(self.players[i]) != 0:
        points_hand.append(self.is_flush(self.players[i]))

      elif self.is_straight(self.players[i]) != 0:
       points_hand.append(self.is_straight(self.players[i]))

      elif self.is_three_kind(self.players[i]) != 0 :
        points_hand.append(self.is_three_kind(self.players[i]))

      elif self.is_two_pair(self.players[i]) != 0:
        points_hand.append(self.is_two_pair(self.players[i]))

      elif self.is_one_pair(self.players[i]) != 0:
        points_hand.append(self.is_one_pair(self.players[i]))

      elif self.is_high_card(self.players[i]) != 0:
        points_hand.append(self.is_high_card(self.players[i]))
  

    maxim = max(points_hand)
    timesaround = 0
    wins = 0
    winner1 = 0
    winner2 = 0

    #Print winner!!!!!! :)
    for i in range(len(points_hand)):
      timesaround = timesaround + 1

      if points_hand[i] == maxim:
        wins = wins + 1
        winner2 = i
        if winner1 < winner2:
          winner1 = winner2
      if wins > 1:
        print("Player", int(winner1) + 1, "ties.")
        print()
        print("Player", int(winner2) + 1, "ties.")
        break
      elif (wins == 1) and timesaround == len(points_hand):
        print("Player", int(winner1) + 1, "wins.")
        break


# determine if a hand is a royal flush
def is_royal (self, hand):
    same_suit = True
    for i in range (len(hand) - 1):
      same_suit = same_suit and (hand[i].suit == hand[i + 1].suit)

    if (not same_suit):
      return 0

    rank_order = True
    for i in range (len(hand)):
      rank_order = rank_order and (hand[i].rank == 14 - i)
  
    if (same_suit and rank_order):
      c1 = hand[0].rank
      c2 = hand[1].rank
      c3 = hand[2].rank
      c4 = hand[3].rank
      c5 = hand[4].rank              
      h = 10
      total_points = h * 13**5 + c1 * 13**4 + c2 * 13**3 + c3 * 13**2 + c4 * 13 + c5
      return total_points

    else:
      return 0

# determine if a hand is a straight flush
def is_straight_flush (self, hand):
    same_suit = True
    for i in range (len(hand) - 1):
      same_suit = same_suit and (hand[i].suit == hand[i + 1].suit)

    if (not same_suit):
      return 0

    rank_order = True
    for i in range (len(hand)):
      rank_order = rank_order and (hand[i].rank + 1 == hand[i+1].rank)
  
    if (same_suit and rank_order):
      c1 = hand[0].rank
      c2 = hand[1].rank
      c3 = hand[2].rank
      c4 = hand[3].rank
      c5 = hand[4].rank
      h = 9
      total_points = h * 13**5 + c1 * 13**4 + c2 * 13**3 + c3 * 13**2 + c4 * 13 + c5
      return total_points
  
    else:
      return 0

# determine if a hand is a four of a kind
def is_four_kind (self, hand):
    four = 0
    for i in range(len(hand) - 1):
      if hand[i].rank == hand[i+1].rank:
        four = four + 1
        c = hand[i].rank
      else:
        cx = hand[i].rank
    if four == 4:
      c1 = c
      c2 = c
      c3 = c
      c4 = c
      c5 = cx
      h = 8
      total_points = h * 13**5 + c1 * 13**4 + c2 * 13**3 + c3 * 13**2 + c4 * 13 + c5
      return total_points

    else:
      return 0

# determine if a hand is a full house
def is_full_house (self, hand):
    three = 0
    distance = 0
    for i in range(len(hand) - 1):
      if hand[i].rank == hand[i+1].rank:
        three = three + 1
        c = hand[i].rank
      else:
        cx = hand[i].rank
        distance = distance + 1
    if three == 3 and distance == 1:
      c1 = c
      c2 = c
      c3 = c
      c4 = cx
      c5 = cx
      h = 7
      total_points = h * 13**5 + c1 * 13**4 + c2 * 13**3 + c3 * 13**2 + c4 * 13 + c5
      return total_points

    else:
      return 0

# determine if a hand is a flush
def is_flush (self, hand):
    same_suit = True
    for i in range (len(hand) - 1):
      same_suit = same_suit and (hand[i].suit == hand[i + 1].suit)

    if same_suit == True:
      c1 = hand[0].rank
      c2 = hand[1].rank
      c3 = hand[2].rank
      c4 = hand[3].rank
      c5 = hand[4].rank
      h = 6
      total_points = h * 13**5 + c1 * 13**4 + c2 * 13**3 + c3 * 13**2 + c4 * 13 + c5
      return total_points

    else:
      return 0

# determine if a hand is a straight
def is_straight (self, hand):
    rank_order = True
    for i in range (len(hand) - 1):
      rank_order = rank_order and (hand[i].rank + 1 == hand[i+1].rank)
  
    if rank_order == True:
      c1 = hand[0].rank
      c2 = hand[1].rank
      c3 = hand[2].rank
      c4 = hand[3].rank
      c5 = hand[4].rank
      h = 5
      total_points = h * 13**5 + c1 * 13**4 + c2 * 13**3 + c3 * 13**2 + c4 * 13 + c5
      return total_points

    else:
      return 0

# determine if a hand is a three of kind
def is_three_kind (self, hand):
    c4 = 0
    distance = 0
    three = 0
    for i in range(len(hand) - 1):
      if hand[i].rank == hand[i+1].rank:
        three = three + 1
        if three == 3:
          c = hand[i].rank
      else:
        three = 0
        distance = distance + 1
        cx = hand[i].rank
        if c4 <= cx:
          c4 = cx
    if three == 3 and distance == 2:
      c1 = c
      c2 = c
      c3 = c
      c4 = c4
      c5 = cx
      h = 4
      total_points = h * 13**5 + c1 * 13**4 + c2 * 13**3 + c3 * 13**2 + c4 * 13 + c5
      return total_points

    return 0

# determine if a hand is a two pair
def is_two_pair (self, hand):
    c = 0
    cx = 0
    cx2 = 0
    two = 0
    for i in range(len(hand) - 1):
      if hand[i].rank == hand[i+1].rank:
        two = two + 1
        cx = hand[i].rank
        if cx2 <= cx:
          cx2 = cx
    for i in range(len(hand)):
      if hand[i].rank != cx and hand[i].rank != cx2:
        c = hand[i].rank
        break
      
    if two == 2 and cx2 != cx:
      c1 = cx2
      c2 = cx2
      c3 = cx
      c4 = cx
      c5 = c
      h = 3
      total_points = h * 13**5 + c1 * 13**4 + c2 * 13**3 + c3 * 13**2 + c4 * 13 + c5
      return total_points

    else:
      return 0

# determine if a hand is one pair
def is_one_pair (self, hand):
    c = 0
    cx = 0
    cx2 = 0
    cx3 = 0
    for i in range (len(hand) - 1):
      if (hand[i].rank == hand[i + 1].rank):
        c = hand[i].rank
      else:
        cx = hand[i].rank
        if cx2 <= cx:
          cx2 = cx
          if cx3 <= cx2:
            cx3 = cx2
    if c != 0:
      c1 = c
      c2 = c
      c3 = cx3
      c4 = cx2
      c5 = cx
      h = 2
      total_points = h * 13**5 + c1 * 13**4 + c2 * 13**3 + c3 * 13**2 + c4 * 13 + c5
      return total_points

    else:
      return 0

# determine if a hand is a high card
def is_high_card (self, hand):
    high = 0
    for i in range(len(hand)):
      if high <= hand[i].rank:
        high = hand[i].rank

    c1 = hand[0].rank
    c2 = hand[1].rank
    c3 = hand[2].rank
    c4 = hand[3].rank
    c5 = hand[4].rank
    h = 1
    total_points = h * 13**5 + c1 * 13**4 + c2 * 13**3 + c3 * 13**2 + c4 * 13 + c5
    return total_points

def main():
# prompt user to enter the number of players
num_players = int (input ('Enter number of players: '))
while ((num_players < 2) or (num_players > 6)):
    num_players = int (input ('Enter number of players: '))

# create the Poker object
game = Poker (num_players)

# play the game (poker)
game.play()

main()
