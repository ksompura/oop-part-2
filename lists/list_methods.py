data = [1,2,3,4]
print(data)
data.append(5) #add 5 to the end of the list
print(data)

#to add in more than just one value, use extend method
data.extend([6,8])
print(data)

# insert into the middle of a list
data.insert(3,"marshmellow") #which position to insert and what to insert
print(data)

#remove everything from list with .clear()
# data.clear()
# print(data)

# .pop() removes the specified index, or the last object if () is empty
# can store a popped item
#[1, 2, 3, 'marshmellow', 4, 5, 6, 8]
number = data.pop(2) #pops out 3 from the list
print(data)
print(number)

#.remove() removes the value that is put in () wherever it is in the list.
#only removes the first time it sees that value
lst1 = [1,2,2,2,3,4,5]
print(lst1)
lst1.remove(5)
print(lst1)
lst1.remove(2)
print(lst1)

##.index tells you which index a value is at
lst2 = [4,6,8,4,8,3,1,9,3,0,2]
print(lst2.index(0)) # 9th index
print(lst2.index(4,1)) # first number is what we are looking for, second is starting point of search
print(lst2.index(3,1,6)) # first number is what we are looking for, second is starting point of search, third is ending point of search (remember its exlusive in the end point)

#.count counts how many times it shows up in a lust
print(lst2.count(8)) #shows up 2 times
print(lst2)
#.reverse() reverses the order

#.sort() makes it it order
lst2.sort()
print(lst2)

#.join converts a list into a string
lst3 = ["coding","is","fun"]
str1 = ' '.join(lst3)
print(str1)