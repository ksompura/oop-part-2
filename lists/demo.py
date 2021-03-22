stuff = ["blue","orange","green"] #index starts at 0

print(stuff[0]) #blue
print(stuff[2]) #green

print(stuff[-1]) #green
print(stuff[-2]) #orange

"blue" in stuff #True
"black" in stuff #False

if "orange" in stuff:
	print("orange is cool")

#Swapping values
names = ["Joe","Jill"]
names[0], names[1] = names[1], names[0]
print(names) #['Jill', 'Joe']