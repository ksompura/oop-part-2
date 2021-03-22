# builds 3 pyramids (nested for loop)
for x in range(3):
	for n in range(1,11):
		print("/\\" * n)


for n in range(1,11):
	print("/\\" * n)

# with a while loop
times = 1
while times <11:
	print("/\\" * times)
	times += 1

#without string multiplication - ugly solution
for num in range(1,11):
	count = 1
	steps = ""
	while count <= num:
		steps += "/\\"
		count += 1
	print(steps)