'''
evens = get_multiples(2, 3)
next(evens) # 2
next(evens) # 4
next(evens) # 6
next(evens) # StopIteration

default_multiples = get_multiples()
list(default_multiples) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
'''

def get_multiples(num=1, count=10):
    x = num
    y=1
    while y <= count:
        yield x*y
        y +=1


# evens = get_multiples(2, 3)
# print(next(evens)) # 2
# print(next(evens)) # 2
# print(next(evens)) # 2
# print(next(evens)) # 2


def get_unlimited_multiples(num=1):
    x = num
    y=1
    while True:
        yield x*y
        y +=1

sevens = get_unlimited_multiples(7)
i = [print(next(sevens)) for i in range(15)]
i