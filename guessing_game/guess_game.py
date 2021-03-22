import random

# play = "y"

# while play == "y":
# 	rand_num = random.randint(1,10) #randint is inclusive and numbers are from 1-10

# 	intro = int(input("Guess a number between 1-10: "))

# 	while intro != rand_num:
# 		if intro > rand_num:
# 			intro = int(input("Too high, keep gussing: "))
# 		elif intro < rand_num:
# 			intro = int(input("Too low, keep gussing: "))
# 		else:
# 			print("You guessed correctly on your first try!")
# 	print("You got it right!")
# 	play = input("Do you want to play again (y/n):")

#Ask if they want to play again (y/n)

#Another way to code the same thing
random_number = random.randint(1,10)

while True:
	guess = input("Guess a number between 1-10: ")
	guess = int(guess)
	if guess < random_number:
		print("Too low, keep gussing: ")
	elif guess > random_number:
		print ("Too high, keep gussing: ")
	else:
		print("You win!!")
		play_again = input("Do you want to play again? (y/n): ")
		if play_again == "y":
			random_number = random.randint(1,10)
			guess = None
		else:
			print("Thanks for playing")
			break
