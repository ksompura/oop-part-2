'''
is_palindrome('testing') # False
is_palindrome('tacocat') # True
is_palindrome('hannah') # True
is_palindrome('robert') # False
is_palindrome('amanaplanacanalpanama') # True
'''

def is_palindrome(words):
	words = words.lower().replace(" ","")
	reverse = words[::-1]
	if reverse == words:
		return True
	return False

print(is_palindrome("testing")) 	
print(is_palindrome("tacocat")) 	
print(is_palindrome("hannah")) 	
print(is_palindrome("robert")) 	
print(is_palindrome("A man a plan a canal panama")) 	


    