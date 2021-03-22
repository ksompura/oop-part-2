numbers = dict(first=1,second=2,third=3)

squared_numbers = {key: value **2 for key,value in numbers.items()}

print(squared_numbers) #{'first': 1, 'second': 4, 'third': 9}

#Create new dictionary
new = {num: num**2 for num in [1,2,3,4,5]}
print(new)

#Create dictionary from 2 strings
str1 = "ABC"
str2 = "123"
combo = {str1[i]:str2[i] for i in range(0,len(str1))}
print(combo) #{'A': '1', 'B': '2', 'C': '3'}

#conditional logic with dictionaries
num_list = [1,2,3,4,5,6,7]
num_dict = {num:("even" if num % 2 == 0 else "odd") for num in num_list}
print(num_dict)

############
list1 = ["CA", "NJ", "RI"]
list2 = ["California", "New Jersey", "Rhode Island"]

# make sure your solution is assigned to the answer variable so the tests can work!
# answer = {list1[i]: list2[i] for i in range(0,len(list1))}
# print(answer)

################
# person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]

# use the person variable in your answer
# answer = {i[0]: i[1] for i in person}
# print(answer)

#another solution
# answer = dict(person)
# print(answer)

###################
#dictionary a,e,i,o,u as keys, 0 as values
# answer = {}.fromkeys(["a","e","i","o","u"],0)
# print(answer)

#another way
# answer = {char:0 for char in "aeiou"}
# print(answer)

# make sure your solution is assigned to the answer variable so the tests can work!
answer = {num:chr(num) for num in range(65,91)}
print(answer)