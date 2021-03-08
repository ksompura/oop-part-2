class Human:
    def __init__(self,first,last,age):
        self.first = first
        self.last = last
        if age >= 0:
            self._age = age #make it _age to signify people shouldn't touch it
        else:
            self._age = 0

    # def get_age(self):
    #     return self._age

    # def set_age(self, new_age):
    #     if new_age >= 0:
    #         self._age = new_age
    #     else:
    #         self._age = 0

    #is a way to get the age witout needing "()" like a method, makes it a proxy for ._age
    @property
    def age(self):
        return self._age

    #make a setter to set the age
    @age.setter
    def age(self,value):
        if value >= 0:
            self._age = value
        else:
            raise ValueError("age can't be negative!")

    @property
    def full_name(self):
        return f"{self.first} {self.last}"

    # kinda sketchy way to make a full name setter
    @full_name.setter
    def full_name(self,name):
        self.first,self.last = name.split(" ") #split it on the space


# Properties will prevent us from altering age right off the bat
jane = Human("Jane","Goodall",23)
# print(jane.get_age()) # 0 
# jane.set_age(86)
# print(jane.get_age())
print(jane.age)
jane.age = 86
print(jane.age)
print(jane.full_name)
jane.full_name = "Rick Danger"
print(jane.__dict__)