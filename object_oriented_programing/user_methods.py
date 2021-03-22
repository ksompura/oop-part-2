class User():
	
	def __init__(self,first,last,age):
		self.first = first
		self.last = last
		self.age = age

	def full_name(self): #always have to include "self", can be named other things but its convention to call it self
		return f"{self.first} {self.last}"

	def initials(self):
		return f"{self.first[0]}.{self.last[0]}."

	def likes(self,thing):
		return f"{self.first} likes {thing}"

	def is_senior(self):
		return self.age >= 65 #returns boolean True or False

	#previous methods have been getters, now make a setter, increases age by 1
	def birthday(self):
		self.age += 1
		return f"Happy {self.age}, {self.first}"

user1 = User("Joe","Smith",78) 
user2 = User("Jill","Gold",23)

print(user2.full_name())
print(user2.initials())

print(user1.likes("ice cream"))
print(user2.likes("fries"))

print(user2.is_senior())
print(user1.age)
print(user1.birthday())
print(user1.age)

class BankAccount:
    def __init__(self, owner, balance=0.0):
    	self.owner = owner
    	self.balance = balance
    
    def deposit(self, deposit):
        self.balance += deposit
        return self.balance
        
    def withdraw(self, withdraw):
        self.balance -= withdraw
        return self.balance

acct = BankAccount("Daryl")
print(acct.owner)
print(acct.balance)
print(acct.deposit(10))
print(acct.withdraw(3))
print(acct.balance)