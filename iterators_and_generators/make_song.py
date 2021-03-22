'''
kombucha_song = make_song(5, "kombucha")
next(kombucha_song) # '5 bottles of kombucha on the wall.'
next(kombucha_song) # '4 bottles of kombucha on the wall.'
next(kombucha_song) # '3 bottles of kombucha on the wall.'
next(kombucha_song) # '2 bottles of kombucha on the wall.'
next(kombucha_song) # 'Only 1 bottle of kombucha left!'
next(kombucha_song) # 'No more kombucha!'
next(kombucha_song) # StopIteration

default_song = make_song()
next(default_song) # '99 bottles of soda on the wall.'
'''

def make_song(num=99, subject="soda"):
    while True:
        if num > 0:
            yield print(f"{num} bottles of {subject} on the wall.")
            num -=1
        else:
            print(f"No more {subject}!")
            raise StopIteration
            break

# def make_song(num=99, subject="soda"):
#     while True:
#         if num > 0:
#             yield print("{} bottles of {} on the wall.".format(num, subject))
#             num -=1
#         else:
#             print("No more {}!".format(subject))
#             raise StopIteration
#             break

# Three different ways to create the same function
# def make_song(verses=99, beverage="soda"):
#     for num in range(verses, -1, -1):
#         if num > 1:
#             yield "{} bottles of {} on the wall.".format(num, beverage)
#         elif num == 1:
#             yield "Only 1 bottle of {} left!".format(beverage)
#         else:
#             yield "No more {}!".format(beverage)

kombucha_song = make_song(beverage="kombucha")
next(kombucha_song) # '5 bottles of kombucha on the wall.'
next(kombucha_song) # '4 bottles of kombucha on the wall.'
next(kombucha_song) # '3 bottles of kombucha on the wall.'
next(kombucha_song) # '2 bottles of kombucha on the wall.'
next(kombucha_song)
next(kombucha_song)
next(kombucha_song)
next(kombucha_song)

    