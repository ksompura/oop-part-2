#Slicing in a list works like this: [start:end:step]

lst1 = [1,2,3,4]

lst1[1:] #[2,3,4]

lst1[3:] #[4]

lst1[-1] #[4]

lst1[-3] #[2,3,4]

lst1[0:] #aka lst1[:] just creates a copy of that list

# note the end is non inclusive

# step works the same as with range
# note
print(lst1[2::-1]) # [3,2,1]

#Tricks with slices
string = "This is fun!"
print(string[::-1]) #!nuf si sihT

numbers = [1,2,3,4,5]
numbers[1:3] = ["a","b","c"]
print(numbers) #[1, 'a', 'b', 'c', 4, 5]