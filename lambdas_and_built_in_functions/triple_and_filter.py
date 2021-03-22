'''
filters out all numbers not divisible by 4 and multiply them by 3
triple_and_filter([1,2,3,4]) # [12]
triple_and_filter([6,8,10,12]) # [24,36]
'''

def triple_and_filter(lst):
	return list(map(
		lambda i: i * 3,
		filter(lambda n: n % 4 ==0,lst))
	)
    

print(triple_and_filter([1,2,3,4])) # [12]
print(triple_and_filter([6,8,10,12])) # [24,36]