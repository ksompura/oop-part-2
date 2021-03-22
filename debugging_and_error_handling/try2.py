# try:
# except:
# else:
# finally:
while True:
	try:
		num = int(input("Please enter a number:\n"))
	except ValueError:
		print("Thats not a number!")
	else: #executes if except don't go through
		print(f"Good job, that was a number: {num}")
		break
	finally: #will always run
		print("Runs no matter what")