#only allow certain pets, as a type of check
class Pet:
	allowed = ["dog","cat","fish","chicken"]
	def __init__(self, name, species):
		if species not in Pet.allowed:
			raise ValueError (f"{species} not allowed as a pet!")
		self.name = name
		self.species = species
	def set_species(self,species):
		if species not in Pet.allowed:
			raise ValueError (f"{species} not allowed as a pet!")
		self.species = species

cat = Pet("Blue", "cat")
dog = Pet("Morty", "dog")
# tiger = Pet("Tony", "tiger") #will raise an error

Pet.allowed.append("pig")
print(Pet.allowed)
cat.set_species("pig")
print(cat.species)