#tuples are like lists except they are immutable (cam't be changed)
# tuples use () instead of []
alphabet = ("a","b",'c','d')
'a' in alphabet #True
# alphabet[0] = "change me!" ##Throws an error

#tuples can be used as keys in a dictionary, lists cannot
locations = {(35,39):'Tokyo Office', (41,74): "New York Office", (37,122):"San Francisco Office"}
print(locations[(35,39)])

#some dictionary methods will return tuples
dog = {"name": "murphy", "age":2, "isActive":True}
print(dog.items()) #dict_items([('name', 'murphy'), ('age', 2), ('isActive', True)])

#loops are the same

for a in alphabet:
	print(a)

i = len(alphabet) - 1
while i >=0:
	print(alphabet[i])
	i -= 1

#.count() works the same way as we've seen before
#.index() returns the index at which the value is found
print(alphabet.index("c")) #2

#you can nest tuples inside tuples just like lists