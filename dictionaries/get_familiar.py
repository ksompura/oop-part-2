# #Dictionaries are made up of key/ value pairs.
dog = {"name": "murphy", "age":2, "isActive":True}
# print(dog)

# artist = {
#     "first": "Neil",
#     "last": "Young",
# }
# # full_name = artist["first"] +" "+ artist["last"]
# # print(full_name)

# #Another way
# full_name = f"{artist['first']} {artist['last']}"
# print(full_name)

# #.values() to see values in a dictionary
# for v in dog.values():
# 	print(v)
# #.keys() to see keys in a dictionary
# for k in dog.keys():
# 	print(k)

# #to see both use .items()
# for k,v in dog.items():
# 	print(f"key is {k} and value is {v}")


# #############
# # DON'T TOUCH PLEASE!
# donations = dict(sam=25.0, lena=88.99, chuck=13.0, linus=99.5, stan=150.0, lisa=50.25, harrison=10.0)
# # DON'T TOUCH PLEASE!


# # Use a loop to add together all the donations and store the resulting number in a variable called total_donations
# total_donations = 0
# for v in donations.values():
#     total_donations += v
# print(total_donations)

###############
#test to see if a dictionary has a certain key
print("name" in dog) #True because name is a key in dict dog

#test to see if a dictionary has a certain value
print("murphy" in dog.values()) #True
print("name" in dog.values()) #False