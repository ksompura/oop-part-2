# double and single quotes, "" ''
# they are pretty much the same

#cannot do
# msg = "they said, "hello"" # will give error

#can do
msg = "they said, 'hello'"
# or
msg = 'they said, "hello"'


# escape sequences
# \n creates a new line
msg2 = "hello \n world"
print(msg2)

# need two backslashes to write a backslash
backslash = "this is a backslash\\"
print(backslash)

# if you need double quotes in a string
str = "he said \"ha ha\" "
print(str)

###########
str1 = "your"
str2 = "face"
print(str1 + " "+ str2)

str3 = "ice"
str3 += "cream"
print(str3) #"icecream"



############
# F-strings
#can interject a different data type into a string with f
x= 100
print(f"I told you {x*10} times to go to sleep.")


############
#Indexing
str6 = "Murphy"
print(str6[0])
print(str6[1])
print(str6[-1])
print(str6[-2])