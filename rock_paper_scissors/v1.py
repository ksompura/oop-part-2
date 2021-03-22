print("...Rock...") # CTRL+SHIFT+D copy and pastes the line down into the next line
print("...Scissors...")
print("...Paper...")

player1 = input("Player 1 enter your move: ")
player2 = input("Player 2 enter your move: ")


if player1 == "rock" and player2 == "scissors":
	print("player1 wins")
elif player1 == "rock" and player2 =="Paper":
	print("player2 wins")
elif player1 == "scissors" and player2 == "rock":
	print("player2 wins")
elif player1 == "scissors" and player2 =="paper":
	print("player1 wins")
elif player1 == "paper" and player2 == "rock":
	print("player1 wins")
elif player1 == "paper" and player2 == "scissors":
	print("player2 wins")

elif player1 == player2:
	print("It's a tie")
else:
	print("something went wrong")