from pyfiglet import figlet_format
from colorama import init
from termcolor import colored

init()

def text_art(msg, color):
	valid_colors = ("red", "green", "yellow", "blue", "magenta", "cyan", "white")

	if color.lower() not in valid_colors:
		color = "cyan"
	result = figlet_format(msg)
	colored_result = colored(result, color=color)
	print(colored_result)


msg = input("Hi what would you like to draw:\n")
color = str(input("What color?\n"))
text_art(msg, color)