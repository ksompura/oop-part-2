#list comprehensions are like a short hand for for loops. They are used to make a new list that is tweaked from an existing one
num10 = [num*10 for num in range(1,6)]
print(num10) #[10,20,30,40,50,60]

name = 'keshav'
name_upper = [letter.upper() for letter in name]
print(name_upper)


#list comprehension vs looping
numbers = [1,2,3,4,5]
doubled_numbers = []

for num in numbers:
	doub_num = num*2
	doubled_numbers.append(doub_num)

print(doubled_numbers)

#can be done in one line
d_num2 = [num*2 for num in numbers]
print(d_num2)

#boolean example
[bool(val) for val in [0,"",[]]] #[False,False,False]

#make list of numbers into a string
string_list = [str(num) for num in numbers]
print(string_list)

###########
#with conditional logic
evens = [num for num in numbers if num % 2 == 0]
odds = [num for num in numbers if num % 2 != 0]
print(evens)
print(odds)

#########
with_vowels = "Papa john's or dominos?"
no_vowels = ''.join(char for char in with_vowels if char not in "aeiou")
print(no_vowels)

# names = ["Elie","Tim","Matt"]
# answer = [char[0] for char in names]
# print(answer)
# numbers = [1,2,3,4,5,6]
# answer2 = [num for num in numbers if num % 2 == 0]
# print(answer2)

#find the intersection
# answer = [num for num in [1,2,3,4] if num in [3,4,5,6]]
# print(answer)

# #reverse and in lower case
# answer2 = [char[::-1].lower() for char in ["Elie","Tim","Matt"]]
# print(answer2)

# for numbers 1-100 (including 100), create a var that is a list w/all nums divisible by 12
# answer = [num for num in range(1,101) if num % 12 == 0]
# print(answer)

#list containing all letters from "amazing" but not the vowels
answer = [char for char in "amazing" if char not in "aeiou"]
print(answer)