## if nothing is writen in power argument, the default exponent will be 2
def exponent(num,power=2):
	""" Raises num to the specifed number specifed by "power". """
	return num ** power

def add(a,b):
	return a+b

#functions can take other functions, but default functions have to go on the end
def math(a,b, fn=add):
	return fn(a,b)

def subtract(a,b):
	return a-b

#if you know the argument name, order can change if you do like below
print(exponent(power=6,num=9))

## Can see the docstring of a function with .__doc__
print(exponent(2).__doc__)