# create an infinite generator

# # Not what we want, we only want one at a time, and a very large list will take up a lot of space
# def current_beat():
#     max = 100
#     nums = (1,2,3,4)
#     i = 0
#     result = []
#     while len(result) < max:
#         if i >= len(nums): i = 0 # i goes back to zero
#         result.append(nums[i])
#         i += 1
#     return result

# print(current_beat())

# Better way to create the infinite generator
def current_beat():
    nums = (1,2,3,4)
    i = 0
    while True:
        if i >= len(nums): i=0 # reset i back to zero
        yield nums[i]
        i +=1

counter = current_beat()

print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))