# for j in range(1,21):
# 	if j == 4 or j == 13:
# 		print(f"{j} is unlucky")
# 	elif j % 2 == 0:
# 		print(f"{j} is even")
# 	else:
# 		print(f"{j} is odd")
	

for j in range(1,21):
	if j == 4 or j == 13:
		state = "unlucky"
	elif j % 2 == 0:
		state = "even"
	else:
		state = "odd"
	print(f"{j} is {state}")
	