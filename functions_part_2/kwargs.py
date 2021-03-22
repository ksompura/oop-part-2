## **kwargs makes it into a dictionary, no limit on inputs like *args
# def fav_colors(**kwargs):
# 	# print(kwargs)
# 	for person,color in kwargs.items():
# 		print(f"{person}'s favorite color is {color}")

# fav_colors(keshav="green",shiv="blue",anjali="purple")

# Define combine_words below:
def combine_words(word,**kwargs):
    if kwargs:
        for k,v in kwargs.items():
            if k == "prefix":
                return v + word
            elif k == "suffix":
                return word + v
    return word

print(combine_words("work",suffix="er"))

## have to have the order in the aruments be
# 1) parameter
# 2) *args
# 3) default parameter
# 4) **kwargs