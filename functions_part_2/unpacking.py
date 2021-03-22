def sum_all_values(*args):
	total = 0
	for num in args:
		total += num
	print(total)

nums = [1,2,54,2,56,853,264,7]
# sum_all_values(nums) #This will throw an error because it passes in a list

sum_all_values(*nums) #won't throw an error because of the "*" which unpacks the list or tuple

def display_names(first, second):
	print(f"{first} says hello to {second}")

names = {"first":"Colt","second":"Rusty"}

display_names(first="Charles",second ="Morty")
# display_names(names) #Does not work
display_names(**names) # ** unpacks the dictionary

def add_and_multiply_numbers(a,b,c,**kwargs):
	print(a + b * c)
	print("OTHER STUFF...")
	print(kwargs)

data = dict(a=1,b=2,c=3,d=55,name="Ashvin")

add_and_multiply_numbers(**data,dog="Murph")