#define function to flip a coin
from random import random
def flip_coin():
	#generate float from 0-1
	r = random()
	if r > 0.5:
		return "Heads"
	else:
		return "Tails"

print(flip_coin())

#another way to write it
def flip_coin():
	if random() > 0.5:
		return "Heads"
	else:
		return "Tails"
#second function overwrites the first
print(flip_coin())