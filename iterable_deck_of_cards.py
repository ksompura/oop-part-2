from random import shuffle

class Card:
	allowed_suit = ("Hearts", "Diamonds", "Clubs", "Spades")
	allowed_value = ("A","2","3","4","5","6","7","8","9","10","J","Q","K")
	def __init__(self,value,suit):
		if suit not in Card.allowed_suit:
			raise ValueError (f"{suit} is not an acceptable suit.")
		self.suit = suit
		if value not in Card.allowed_value:
			raise ValueError (f"{value} is not an acceptable value.")
		self.value = value

	def __repr__(self):
		# return f"{self.value} of {self.suit}" 
		return "{} of {}".format(self.value, self.suit) # need to write this way for UDEMY

# card = Card("8","Hearts")
# print(card)

class Deck:
	
    def __init__(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        values = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
        self.cards = [Card(value,suit) for suit in suits for value in values]
        # print(self.cards)

    def __repr__(self):
        return "Deck of {} cards".format(self.count())

    def __iter__(self):
        return iter(self.cards)

    def count(self):
        return len(self.cards)

    def _deal(self,num):
        count = self.count()
        if count == 0:
            raise ValueError ("All cards have been dealt")
        actual = min(count,num)
        cards = self.cards[-actual:]
        self.cards = self.cards[:-actual]
        return cards

        print("Going to remove {} cards".format(actual))

    def deal_card(self):
        return self._deal(1)[0] # the 0 returns a single element rather than a list with one card

    def deal_hand(self, hand_size):
        return self._deal(hand_size)

    def shuffle(self):
        if self.count() < 52:
            raise ValueError ("Only full decks can be shuffled")
        shuffle(self.cards)
        return self #good practice but we don't need it here

my_deck = Deck()
my_deck.shuffle()

for card in my_deck:
    print(card)
