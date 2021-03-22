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

c = Card("3","Diamonds")
print(c)
