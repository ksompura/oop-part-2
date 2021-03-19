# Create a custom For Loop

# for num in [1,2,3]
# for char in "hi there"

def my_for(iterable, func):
    iterator = iter(iterable)
    while True:
        try:
            i = (next(iterator))
        except StopIteration:
            print("End of iterator!")
            break
        else:
            func(i)

def square(x):
    print(x*x)
    
my_for("hello", print) 
my_for([1,2,3,4,5], square)
my_for([1235,25,12], square)
