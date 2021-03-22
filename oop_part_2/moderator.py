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

#Moderators get the same methods as normal User but with some extra abilities
#Also inheritance helps to reduce the amount of duplication in our code
class Moderator(User):
    total_mods = 0
    def __init__(self,first,last,age,community):
        super().__init__(first,last,age)
        self.community = community
        Moderator.total_mods += 1

    @classmethod
    def dis_active_mods(cls):
        return f"There are {cls.total_mods} active moderators currently online."

    def remove_post(self):
        return f"{self.full_name()} removed a post from the {self.community} community."

print(User.dis_active_users())
print(Moderator.dis_active_mods())
u1 = User("Joe","Rogan",54)
u1 = User("Joe","Rogan",54)
u1 = User("Joe","Rogan",54)
u1 = User("Joe","Rogan",54)
u1 = User("Joe","Rogan",54)
u1 = User("Joe","Rogan",54)
print(User.dis_active_users())
print(Moderator.dis_active_mods())
kathrine = Moderator("Katherine", "Naer",45, "Pirate")
kathrine = Moderator("Katherine", "Naer",45, "Pirate")
print(User.dis_active_users())
print(Moderator.dis_active_mods())


# print(kathrine.full_name())

# print(kathrine.community)