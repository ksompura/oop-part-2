# sorted() #returns a new list of sorted items from iterable
# different from .sort() in that it doesn't alter the existing list

users = [
{"username":"sam","tweets":["Pizza is good","Yummmmm"]},
{"username":"kale","tweets":["Kale chips, yeaaaa"]},
{"username":"jeff","tweets":["Nerf or nothing"]},
{"username":"nico","tweets":[]},
{"username":"angel","tweets":["CATS"]},
{"username":"michael","tweets":[]}
]

# sort the dictionary by usernames
print(sorted(users,key= lambda user: user["username"]))

# sort the dictionary by tweet number
# least active to most active
print(sorted(users,key= lambda user: user["tweets"]))

# most active to least active
print(sorted(users,key= lambda user: user["username"], reverse=True))
