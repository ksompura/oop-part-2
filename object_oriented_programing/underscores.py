#_name <- one underscore is to tell other developers that it is supposed to be a private property/method
#__name
#__name__ <- shouldn't really make dunder methods

class Person:
	def __init__(self):
		self.name = "Tony"
		self._secret = "hi"
		self.__msg = "This is a message" #makes it unique to class Person, name mangling
		self.__lol = "ahdhausfbis"

p= Person()
print(p.name)
print(p._secret)
# print(p.__msg) # won't work
# print(dir(p))
print(p._Person__msg) #this is how we can access a double underscore
print(p._Person__lol)
