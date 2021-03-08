class GrumpyDict(dict): #make a class from built in dictionary class
    def __repr__(self):
        print("NONE OF YOUR BUSINESS")
        return super().__repr__() #need to include the super to get how dictionaries are supposed to be represented

    def __missing__(self,key):
        print(f"YOU WANT {key}? WELL IT AIN'T HERE!")

    def __setitem__(self,key,value):
        print("YOU WANT TO CHANGE THE DICTIONAIRY?")
        print("OK FINE...")
        super().__setitem__(key,value)

    def __contains__(self,item):
        print(f"NO, {item} AIN'T HERE!")
        return False #even if it does contain it

data = GrumpyDict({"first":"Tom","animal":"cat"})
print(data)
data["city"] = "Tokyo"
print(data)
"city" in data