# filter is like map, but it is used to filter out a thing based on some conditions
# filter uses True and False to determine what is filtered out
users = [
{"username":"sam","tweets":["Pizza is good","Yummmmm"]},
{"username":"kale","tweets":["Kale chips, yeaaaa"]},
{"username":"jeff","tweets":[]},
{"username":"nico","tweets":[]},
{"username":"angel","tweets":["CATS"]},
{"username":"michael","tweets":[]}
]

# inactive_users = list(filter(lambda n: not n["tweets"] == 0,users))

## MOST OFTEN IN PYTHON PEOPLE USE LIST COMPREHENSIONS INSTEAD OF THIS, this is more of what is used in some other languages

# print(inactive_users)
usernames = list(map(lambda u: u["username"].upper(),
	filter(lambda n: not n["tweets"],users)))

print(usernames)