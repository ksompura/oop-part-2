import requests
from random import choice
from pyfiglet import figlet_format
from colorama import init
from termcolor import colored

init()

header = figlet_format("DAD JOKES!!!")
header = colored(header, color="green")
print(header)

search_term = input("What do you want to hear a joke about?\n")
url = "https://icanhazdadjoke.com/search"
# res = requests.get(url)
res = requests.get(
	url,
	headers= {"Accept":"application/json"},
	params={"term":search_term}
).json()

# num_jokes = len(res["results"])
num_jokes = res["total_jokes"] # from the request we see this 
results = res["results"]
if num_jokes > 1:
	print(f"There are {num_jokes} jokes about {search_term}. Here's one:")
	print(choice(results)["joke"])
elif num_jokes == 1:
	print(f"There is one jokes about {search_term}")
	print(choice(results)["joke"])
else:
	print(f"Sorry, couldn't find a joke about: {search_term}")

