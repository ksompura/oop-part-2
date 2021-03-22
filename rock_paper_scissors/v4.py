from random import randint
player_wins = 0
computer_wins = 0
winning_score = 2

print("...Rock...") # CTRL+SHIFT+D copy and pastes the line down into the next line
print("...Scissors...")
print("...Paper...")
while player_wins < winning_score and computer_wins < winning_score:
	print(f"Score: player = {player_wins}, computer = {computer_wins}")
	

	player = input("Player 1 enter your move: ").lower()
	if player == "quit" or player == "q":
		break
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
			player_wins += 1
		elif computer =="paper":
			print("computer wins")
			computer_wins += 1
	elif player == "scissors":
		if computer == "rock":
			print("computer wins")
			computer_wins += 1
		elif computer =="paper":
			print("player wins")
			player_wins += 1 	
	elif player == "paper":
		if computer == "rock":
			print("player wins")
			player_wins += 1
		elif computer == "scissors":
			print("computer wins")
			computer_wins += 1
	else:
		print("something went wrong")
if player_wins > computer_wins:
	print("CONGRATS, YOU WIN")
elif player_wins == computer_wins:
	print("TIE GAME")
else:
	print("YOU LOSE")
print(f"Final score: player = {player_wins}, computer = {computer_wins}")