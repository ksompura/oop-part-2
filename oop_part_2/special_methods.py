from copy import copy
class Human:
    def __init__(self,first,last,age):
        self.first = first
        self.last = last
        self.age = age
    
    def __repr__(self):
        return f"Human named {self.first} {self.last}"

    def __len__(self):
        return self.age

    #add two humans together to create a baby, taking on the last name of first person
    def __add__(self,other):
        #create a check if other is a Human instance
        if isinstance(other, Human):
            return Human(first="Newborn", last = self.last, age=0)
        raise TypeError ("You can't add nonhumans!")

    #what happens when we multiply a human by a number
    def __mul__(self,other):
        if isinstance(other,int):
            return [copy(self) for i in range(other)]
        raise TypeError ("Can only multiply humans by integers")


j = Human("Jenny", "Larsen", 32)
k = Human("Kevin","Jones",28)
print(j)
print(k)

print(j + k)

triplets = j * 3
#rename the second clone, note we need the copy method we imported, otherwise they will all be the exact same
triplets[1].first = "Jessica"
print(triplets)

# Jenny and Kevin have triplets
triple = (k+j)*3
print(triple)