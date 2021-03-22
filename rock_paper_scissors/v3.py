from random import randint
print("...Rock...") # CTRL+SHIFT+D copy and pastes the line down into the next line
print("...Scissors...")
print("...Paper...")

player = input("Player 1 enter your move: ").lower()

rand_num = randint(0,2)
if rand_num == 0:
	computer = "rock"
elif rand_num == 1:
	computer = "paper"
else:
	computer = "scissors"
print(f"Computer: {computer}")

if player == computer: ## most common outcome so put it first
	print("It's a tie")
elif player == "rock":
	if computer == "scissors":
		print("player wins")
	elif computer =="paper":
		print("computer wins")
elif player == "scissors":
	if computer == "rock":
		print("computer wins")
	elif computer =="paper":
		print("player wins") 	
elif player == "paper":
	if computer == "rock":
		print("player wins")
	elif computer == "scissors":
		print("computer wins")
else:
	print("something went wrong")