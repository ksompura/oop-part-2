class Animal:
    cool = True

    def make_sound(self,sound):
        print(f"this animal says {sound}")

#The Cat class inherits all the this that are in the Animal class
class Cat(Animal):
    pass

jeb = Cat()
jeb.make_sound("meow")
print(jeb.cool)
print(Cat.cool)
print(Animal.cool)

# check if jeb is an instance of an Animal
print(isinstance(jeb, Animal)) 
# check if jeb is an instance of a Cat
print(isinstance(jeb, Cat)) 

larry = Cat()