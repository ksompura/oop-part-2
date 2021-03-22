class User():
	
	active_users = 0

	
	@classmethod 
	def dis_active_users(cls):
		return f"There are {cls.active_users} active users currently online."

	@classmethod
	def from_string(cls,data_str):
		first,last,age = data_str.split(",")
		return cls(first,last,int(age))

	def __init__(self,first,last,age):
		self.first = first
		self.last = last
		self.age = age
		User.active_users += 1

	#ADD IN __repr__  Turns the class into something more readable
	def __repr__(self):
		return f"{self.first} is {self.age}"


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

tom = User.from_string("Tom,Jones,89")
print(tom)
morty = User("Morty", "Sompura", 6)
morty = str(morty)
print(morty)