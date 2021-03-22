'''
gen = yes_or_no()
next(gen) # 'yes'
next(gen) # 'no'
next(gen) # 'yes'
next(gen) # 'no'
'''

def yes_or_no():
    ans = ["yes", "no"]
    s = 0
    while ans:
        if s ==0:
            yield ans[s]
            s += 1
        else:
            yield ans[s]
            s -= 1

# Another way
# def yes_or_no():
#     answer = "yes"
#     while True:
#         yield answer
#         answer = "no" if answer == "yes" else "yes"

yn = yes_or_no()

print(next(yn))
print(next(yn))
print(next(yn))
print(next(yn))