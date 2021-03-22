import keyword

def contains_keyword(*args):
	lst = [keyword.iskeyword(a) for a in args]
	if True in lst:
		return True
	return False

print(contains_keyword("pizza","import"))