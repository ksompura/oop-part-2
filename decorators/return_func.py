from random import choice
# return funcs from other funcs
def make_laugh_func():
    def get_laugh():
        l = choice(("HAHAHA","lol","jajajaja"))
        return l
    return get_laugh

laugh = make_laugh_func()
print(laugh())