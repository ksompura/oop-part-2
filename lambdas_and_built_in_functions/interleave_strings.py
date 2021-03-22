#interleave("hi","ha") #hhia
def interleave(string1,string2):
	z = list(zip(string1,string2))
	# a = "".join(z[0])
	# b = "".join(z[1])
	#do with list comprehension
	aa = ["".join(a) for a in z]
	bb = "".join(aa)
	
	return bb

# Another way
def interleave(str1,str2):
    return ''.join(''.join(x) for x in (zip(str1,str2)))

print(interleave("hi","ha"))