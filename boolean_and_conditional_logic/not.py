age = 3
# 2-8 $2 ticket
# 65 or older $5 ticket
# $10 for everyone else
if not((age>=2 and age<=8) or age>=65):
	print("You pay $10")
else:
	print("You are a child or seinior")