# want to make an def __init__(self,args): at the beginning of every class, because it will always be called

class User():
	def __init__(self,first,last,age): #generally the first is called self as a rule of thumb, then add in other stuff
		self.first = first
		self.last = last
		self.age = age

# 2 instances of User
#instantiating a class:
user1 = User("Joe","Smith",34) #needs to have all parameters filled, otherwise error
user2 = User("Jill","Gold",23)
print(user1.first, user1.last) #Joe Smith
print(user2.first, user2.last) 

class Comment:
    def __init__(self,username,text,likes=0): # can made default arguments (shown here)
        self.username = username
        self.text = text
        self.likes = likes