class User():
	
	active_users = 0

	#very simple example of a class method
	@classmethod #need to define like this, makes the next method a classmethod
	def dis_active_users(cls):
		return f"There are {cls.active_users} active users currently online."

	#more useful / practical class method
	@classmethod
	def from_string(cls,data_str):
		first,last,age = data_str.split(",") #splits at the commas
		return cls(first,last,int(age)) #creates a new instance of User from the string

	def __init__(self,first,last,age):
		self.first = first
		self.last = last
		self.age = age
		User.active_users += 1

	def logout(self):
		User.active_users -= 1
		return f"{self.first} has logged out."

	def full_name(self):
		return f"{self.first} {self.last}"

	def initials(self):
		return f"{self.first[0]}.{self.last[0]}."

	def likes(self,thing):
		return f"{self.first} likes {thing}"

	def is_senior(self):
		return self.age >= 65 

	def birthday(self):
		self.age += 1
		return f"You are {self.age} now {self.first}, congrats!"

# user1 = User("Joe","Smith",78) 
# user2 = User("Jill","Gold",23)
# print(User.dis_active_users())
# user1 = User("Joe","Smith",78) 
# user2 = User("Jill","Gold",23)
# print(User.dis_active_users())

# For example, if we have a csv:
tom = User.from_string("Tom,Jones,89")
print(tom.first)
print(tom.full_name())
print(tom.birthday())