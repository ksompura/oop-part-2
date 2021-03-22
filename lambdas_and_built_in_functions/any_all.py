# all() checks if everything follows the conditions
people = ["Charles","Cody","Cathy","Caren"]

print(all(name[0] == "C" for name in people)) #True

people2 = ["Charles","Cody","Cathy","Caren","Kat"]
print(all(name[0] == "C" for name in people2)) #False


# any() returns True if any element of the iterable is truthy. If the iterable is empty, return False

people3 = ["Charles","Cody","Cathy","Caren","Kat"]
print(any(people[0] == "C" for people in people3)) #True
print(any(people[0] == "K" for people in people3)) #True
print(any(people[0] == "H" for people in people3)) #False
