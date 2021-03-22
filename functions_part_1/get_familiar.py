# def print_square_of_7():
# 	print(7**2)

# print_square_of_7()

# #Return is VERY important, how we get data out of the function
# def square_of_7():
# 	print("I AM BEFORE THE RETURN")
# 	return 7**2
# 	print("I AM AFTER THE RETURN")


# result = square_of_7()
# print(result)

# #Define a function called generate_evens
# #It should return a list of even numbers between 1 and 50(not including 50)
# def generate_evens():
#     return [x for x in range(1,50) if x % 2 == 0]

# print(generate_evens())

# print([x for x in range(1,50) if x % 2 == 0])

# Define speak below:
def speak(animal="dog"):
    if animal == "dog":
        return "woof"
    elif animal == "pig":
        return "oink"
    elif animal == "duck":
        return "quack"
    elif animal == "cat":
        return "meow"
    return "?"

print(speak("lion"))