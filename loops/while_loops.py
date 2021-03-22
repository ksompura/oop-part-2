### BE CAREFUL WHEN USING WHILE LOOPS, THEY CAN CONTINUE FOREVER
# msg = input("What's the best car? ")
# while msg != "jeep":
# 	print("Nah")
# 	msg = input("What's the best car? ")
# print("Yup")
# will go on forever until the user inputs jeep

#BAD, USE CTRL+C to break the loop in powershell
# num = 1 
# while num <11:
# 	print(num)

#Good
num = 1 
while num <11:
	print(num)
	num +=1

from random import randint  # use randint(a, b) to generate a random number between a and b

number = 0 # store random number in here, each time through
i = 0  # i should be incremented by one each iteration
while number !=5:
    number = randint(1,11)
    i += 1
print(i)