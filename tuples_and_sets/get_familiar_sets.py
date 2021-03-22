#sets are like formal mathematical sets
#sets don't have duplicate values
#elements aren't ordered and so you can't index them
# sets can be useful if you need to keep track of a collection of elements, but don't care about ordering, keys or values and duplicates

#create a set with{}
#or with set({})
set1 = {1,2,4,1,1,True,6,"a","b", True, 2.463}
print(set1) #{1, 2, 2.463, 4, 'a', 6, 'b'}

for thing in set1:
	print(thing)

#common us
cities = ['Los Angeles', "Tokyo", "Shanghai", "Mumbai", "Los Angeles", "San Diego", "Oslo", "Paris", "Mumbai","Tokyo"]
print(list(set(cities))) 
print(len(set(cities))) #unique citiees
cities = set(cities)
## set methods
#.add() adds into set if not already there
cities.add("Vancouver")
cities.add("Los Angeles")

#.remove() removes an item
#.discard() does the same as remove except it won't throw an error if its not in the set
#.copy() is same as we have seen
#.clear() empties the set

#Set Math: union, intersections, etc.
math_students = {"Matt", "Helen","Pat","Joe","Anjali"}
bio_students = {"Jane","Matt", "Charles", "Mesut", "Oliver", "Joe"}

#take all names with UNION "|", don't double count
print(math_students | bio_students)

#set INTERSECTIONS "&"
print(math_students & bio_students)

#####################
# 1 - Create a variable called numbers which is a tuple with the the values 1, 2, 3 and 4 inside.
numbers = (1,2,3,4)

# 2 - Create a variable called value which is a tuple with the the value 1 inside.
value = (1,) #need the comma, otherwise its an integer
print(type(value))
# 3 - Given the following variable:

values = [10,20,30]

# Create a variable called static_values which is the result of the values variable converted to a tuple
static_values = tuple(values)
print(static_values)
# 4 - Given the following variable

stuff = [1,3,1,5,2,5,1,2,5]

# Create a variable called unique_stuff which is a set of only the unique values in the stuff list
unique_stuff = set(stuff)

##################################

#set comprehension
x = {x**2 for x in range(10)}
print(x)

string = "hello"
str_set ={char for char in string if char in "aeiou"} 
print(str_set)
print(len({char for char in string if char in "aeiou"}) == 5)

string = "sequoia"
print(len({char for char in string if char in "aeiou"}) == 5)