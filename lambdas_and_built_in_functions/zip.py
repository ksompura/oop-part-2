# ## zip() pair up two list, see example

# list1 = [1,2,3,4,5]
# list2 = [6,7,8,9,10]
# newlist = zip(list1,list2)
# print(newlist)
# newlist = list(zip(list1,list2))
# print(newlist)

# dictionary = dict(zip(list1,list2))
# print(dictionary)

# #limits it to 4 because its the shortest
# words = ["hi","lol","spotify","pandora"]
# zip_three = list(zip(words,list1,list2))
# print(zip_three)
# # print(dict(zip(words,list1,list2))) # dict will throw an error, more than just key and value pair
# unzipped = list(zip(*zip_three))
# print(unzipped)

##more complex examples, more real life
midterms = [80, 91, 78]
finals = [98,89,53]
students = ['Renaud',"Victor","Monika"]

# Want the highest grades:
# final_grades = {"Renaud":98,"Victor":91,"Monika":78}

#with list/dictionairy comprehension
# final_grades = {pair[0]:max(pair[1], pair[2]) for pair in zip(students, midterms, finals)}
# print(final_grades)

#with lambda and map
final_grades = dict(
	zip(students,
		map(
			lambda p: max(p),
			zip(midterms, finals)
		)
	)	
)	
print(f"Final grades:{final_grades}")

avg_grades = dict(
	zip(students,
		map(
			lambda p: ((p[0] + p[1])/2),
			zip(midterms, finals)
		)
	)	
)
print(f"Average grades:{avg_grades}")