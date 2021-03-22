#python debugger module
import pdb
first = "F"
second = "S"
pdb.set_trace()
result = first + second
third = "T"
result += third
print(result)

# put: pdb.set_trace()
#into line of code that is giving you an error and see which line is giving you the problem

#Common PDB command:
# l (list)
# n (next line)
# p (print)
# c (continue - finished debugging and runs throug the rest of the code)
