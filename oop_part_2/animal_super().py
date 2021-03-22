class Animal:
    def __init__(self,name,species):
        self.name = name
        self.species = species

    def __repr__(self):
        return f"{self.name} is a {self.species}"

    def make_sound(self,sound):
        print(f"this animal says {sound}")


class Dog(Animal):
    def __init__(self,name,breed,toy):
        super().__init__(name,species="Dog") #takes name and species from the init of Animal
        self.breed = breed
        self.toy = toy
    
    def play(self):
        print(f"{self.name} plays with {self.toy}")

murphy = Dog("Murphy","Golden Retrevier","Lazer")
print(murphy)
print(murphy.species)
print(murphy.breed)
print(murphy.toy)
murphy.play()