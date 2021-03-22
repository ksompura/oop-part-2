def list_manipulation(lst,command,loc,value=None):
    if command == "remove" and value == None:
        if loc == "end":
            return lst.pop()
        return lst.pop(0)
    if command == "add":
        if loc == "beginning":
        	lst.insert(0,value)
        	return lst
        else:
        	lst.append(value)
        	return lst

print(list_manipulation([1,2,3,4],"add","end",47))