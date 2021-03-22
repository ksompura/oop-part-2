# ask for age
# age = input("How old are you: ")
# if age:
# 	age = int(age)
# 	if age>=18 and age<21:
# 		# 18-21 wristband
# 		print("you can enter with wristband")
# 	elif age >=21:
# 		# 21+ drink, normal entry
# 		print("Your good bud")
# 	else:
# 		# otherwise too young
# 		print("Get lost")
# else:
# 	print("Please enter an age")

age = input("How old are you: ")
if age:
	age = int(age)
	if age>=21:
		# 21+ drink, normal entry
		print("Your good bud")
	elif age >=18:
		# 18-21 wristband
		print("you can enter with wristband")
	else:
		# otherwise too young
		print("Get lost")
else:
	print("Please enter an age")