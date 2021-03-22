#Conditional functions, if,elif,else
name= input("Who is a character in Game of Thrones: ")
if name == "Jon Snow": #need the ":" part otherwise it doesn't work, same for all the others
	print("You know nothing")
elif name == "Arya":
	print("Suprise bitch")
elif name == "Sansa": 		#can have as many elif as you want
	print("Forgetable")
else: 						#can only have one else as a catch all
	print("Move on")



# AND, OR
print("put a number:")
a = input()
a = int(a)
if a>1 and a -5 >0: #if BOTH are satisfied, it's True, if one is not satisified, it's false
	print("Yeehaw")
else:
	print("nah")

print("what city do you like ")
city = input()
if city == "LA" or "SD": #True if either one is true, doesn't have to be both
	print("Sup dude")
else:
	print("thats not california")