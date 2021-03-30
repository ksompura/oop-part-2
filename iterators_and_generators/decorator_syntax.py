def be_polite(fn):
    def wrapper():
        print("What a pleasure to meet you!")
        fn()
        print("Have a great day!")
    return wrapper

# decorator syntax @
@be_polite
def greet():
    print("My name is Keshav.")


greet()

# dont need:
# greet = be_polite(greet) 
# because of the decorator