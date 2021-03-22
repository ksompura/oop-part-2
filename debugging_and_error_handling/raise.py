#we can raise (cause) our own errors when something occurs and give a description
#if other people use our code, it would make sense to see what they did wrong
def colorize(text, color):
	colors = ["blue","teal","maroon","purple"]
	if type(color) is not str:
		raise TypeError("color must be instance of str")
	if type(text) is not str:
		raise TypeError("text must be instance of str")
	if color not in colors:
		raise ValueError("color must be blue, teal, maroon, or purple")
	print(f"Printed {text} in {color}")

colorize("hello", "red")
colorize(48, "red")

