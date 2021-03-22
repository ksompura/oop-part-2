#Basic syntax
#try:
#except:

try:
	morty
except: # not very helpful, want to be more specific because this will catch ALL errors
	print("Problem!!")
print("after try")

def get(d, key):
	try:
		return d[key]
	except KeyError:
		return None
d = {"name": "Rick"}
print(get(d, "name"))
print(get(d, "city"))