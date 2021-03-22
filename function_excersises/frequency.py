'''
frequency([1,2,3,4,4,4], 4) # 3
frequency([True, False, True, True], False) # 1
'''

def frequency(list,val):
	return list.count(val)
    
print(frequency([1,2,3,4,4,4], 4)) # 3
print(frequency([True, False, True, True], False))