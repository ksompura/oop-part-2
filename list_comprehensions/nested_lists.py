# nested_list = [[1,2,3],[4,5,6],[7,8,9]]

# nested_list[0][2] #3
# nested_list[2][0] #7

# for lst in nested_list:
# 	for val in lst:
# 		print(val)

# #The same but with list comprehension
# [[print(val) for val in lst] for lst in nested_list]

board = [[num for num in range(1,4)] for val in range(1,4)]
print(board)

new_board = [["X" if num % 2 != 0 else "O" for num in range(1,4)]for val in range(1,4)]
print(new_board)

## create [[1,2,3],[1,2,3],[1,2,3]] with list comprehension
answer = [[x for x in range(3)] for lst in range(3)]
print(answer)

## create 10x10 nested list, each row containing numbers 0-9
answer2 = [[x for x in range(10)] for lst in range(10)]
print(answer2)