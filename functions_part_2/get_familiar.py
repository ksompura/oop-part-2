def check_who(*args): # *args allows us to pass through more than one parameter	
	if "Keshav" in args:
		return "Welcom back Keshav"
	return "Who are you"

print(check_who())
print(check_who("Keshav",3,4.6, True, "pizza"))
