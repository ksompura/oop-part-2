# used to break out of loops
while True:
	command = input("Type 'exit' to exit: ")
	if (command == 'exit'):
		break

#redundant example
for x in range(1,101):
	print(x)
	if x == 3:
		break

#repeater example but end after 4 times
times = int(input("How many times did you take the dog for a walk today? "))

for t in range(times): #need to include range
	print(f"time{t+1}:They must've loved that")
	if t >=4:
		print('I think thats too many walks.')
		break
