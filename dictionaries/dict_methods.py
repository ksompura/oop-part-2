d = dict(a=1, b=2,c=3)
print(d)

# d.clear()
# d = {}

#.copy makes a copy
c = d.copy()
print(c==d) #True
print(c is d) #False

#{}.fromkeys is used to create new dictionaies with the same values
new_user = {}.fromkeys(["name","email","bio","score"], "unknown")
print(new_user) #{'name': 'unknown', 'email': 'unknown', 'bio': 'unknown', 'score': 'unknown'}
unknown_vars = {}.fromkeys(range(1,11), "unknown")
print(unknown_vars)

#.get() to see a value from a key or if there's no key it returns None
result = d.get('a')
result2 = d.get('z')
print(result) #1 
print(result2) #None

###########
# This code picks a random food item:
from random import choice #DON'T CHANGE!
food = choice(["cheese pizza", "quiche","morning bun","gummy bear","tea cake"]) #DON'T CHANGE!

#DON'T CHANGE THIS DICTIONARY EITHER!
bakery_stock = {
    "almond croissant" : 12,
    "toffee cookie": 3,
    "morning bun": 1,
    "chocolate chunk cookie": 9,
    "tea cake": 25
}

# YOUR CODE GOES BELOW:
quantity = bakery_stock.get(food)

if quantity:
	print(f"{quantity} left")
else:
	print("We don't make that")


#DO NOT TOUCH game_properties!
game_properties = ["current_score", "high_score", "number_of_lives", "items_in_inventory", "power_ups", "ammo", "enemies_on_screen", "enemy_kills", "enemy_kill_streaks", "minutes_played", "notifications", "achievements"] 

# Use the game_properties list and dict.fromkeys() to generate a dictionary with all values set to 0. Save the result to a variable called initial_game_state
initial_game_state = dict.fromkeys(game_properties,0)

print(initial_game_state)

############
#.pop(key) pops out the key from the dictionary, returns the corresponding value that was in the key
#.popitem() randomly pops out a key and its corresponding value
#.update() updates a dictionary
first = dict(a=1,b=2,c=3,d=4,e=5)
second={}

second.update(first)
print(second) #{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

#overwrite an existing key
second['a'] = "AMAZING"
print(second) #{'a': 'AMAZING', 'b': 2, 'c': 3, 'd': 4, 'e': 5}

third = {"city": "Los Angeles"}
third.update(first)
print(third) # {'city': 'Los Angeles', 'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}



#############
inventory = {'croissant': 19, 'bagel': 4, 'muffin': 8, 'cake': 1} #DON'T CHANGE THIS LINE!

# Make a copy of inventory and save it to a variable called stock_list USE A DICTIONARY METHOD
stock_list =inventory.copy()


# add the value 18 to stock_list under the key "cookie"
stock_list.update(cookie=18)
print(stock_list)

# remove 'cake' from stock_list USE A DICTIONARY METHOD
stock_list.pop("cake")
print(stock_list)
