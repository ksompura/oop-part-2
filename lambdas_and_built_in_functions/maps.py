## maps are a common use for lambda, they take in a function and an input
nums = [1,2,3,4,5]

doubles = list(map(lambda x: x*2, nums))
print(doubles) #[2, 4, 6, 8, 10]

names = [{"first":"Morty", "last":"Sompura"}, {"first":"Murphy", "last":"Sompura"},{"first":"Keshav", "last":"Sompura"}]
first_names = list(map(lambda x: x["first"],names))
print(first_names) #['Morty', 'Murphy', 'Keshav']