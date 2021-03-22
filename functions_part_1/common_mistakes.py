def sum_odd_numbers(numbers):
	total = 0
	for num in numbers:
		if num % 2 != 0:
			total += num
	return total

print(sum_odd_numbers([1,2,3,4,5,6,7]))
## Mistake
# def sum_odd_numbers(list):
# 	total = 0
# 	for num in numbers:
# 		if num % 2 != 0:
# 			total += num
# 		return total

def is_num_odd(num):
	if num % 2 !=0:
		return True
	return False

# don't need to include extra line
# def is_num_odd(num):
# 	if num % 2 !=0:
# 		return True
# 	else:
# 		return False
