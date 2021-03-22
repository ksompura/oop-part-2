'''
days = week()
next(days) # 'Monday'
next(days) # 'Tuesday'
next(days) # 'Wednesday'
next(days) # 'Thursday'
next(days) # 'Friday'
next(days) # 'Saturday'
next(days) # 'Sunday'
next(days) # StopIteration
'''

# def week():
#     i = ["Monday","Tuesday","Wednesday", "Thursday","Friday","Saturday","Sunday"]
#     n = 0
#     while n<7:
#         yield i[n]
#         n += 1
                    
 # another way to make a week generator    
def week():
    i = ["Monday","Tuesday","Wednesday", "Thursday","Friday","Saturday","Sunday"]
    for j in i:
        yield j

week = week()
print(next(week))
print(next(week))
print(next(week))
print(next(week))
print(next(week))
print(next(week))
print(next(week))
print(next(week))
