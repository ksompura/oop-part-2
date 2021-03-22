#ranges are commonly used in for loops
#ranges are exclusive, they don't include the last number
r=range(10) #gives 0 through 9, not python starts at 0
print(r) #won't show us all the numbers, need to show in a list
print(list(r))

for x in range(10):
	print(x)
print("")

for x in range(1,6):
	print(x)
print("")
for x in range(0,10,2): #goes from 0 to 9 in steps of 2
	print(x)
print("")
for x in range(8,0,-1): #counts backwards from 8 by 1 at a time
	print(x)
