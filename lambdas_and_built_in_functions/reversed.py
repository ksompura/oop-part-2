#like sorted(), but creates a new reversed list/tuple
for char in reversed("hello world"):
	print(char)
# reverses iterables like slices but not all iterables supports slices
for x in reversed(range(0,11)):
	print(x*2)