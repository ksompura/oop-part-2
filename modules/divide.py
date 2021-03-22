# def divide(a,b):
# 	try:
# 		result =  a/b
# 	except ZeroDivisionError as err:
# 		print("You can't divide by zero")
# 		print(err)
# 	except TypeError as err:
# 		print("Only accepts numbers")
# 		print(err)
# 	else:
# 		print(f"{a} divided by {b} = {result}")

def divide(a,b):
	try:
		result =  a/b
	except (ZeroDivisionError, TypeError) as err: #can have different errors in the same tuple
		print("Something went wrong")
		print(err)
	else:
		print(f"{a} divided by {b} = {result}")

def add(a,b):
	return a + b
if __name__ == "__main__": # for if you don't want to execute when it is imported into another file
	divide("a",2)
	divide(1,0)
	divide(1,346958025)