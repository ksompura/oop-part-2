# create a counter iterable, similar to range

class Counter:
    def __init__(self,low,high):
        self.current = low
        self.high = high
    
    def __iter__(self):
        return self #makes self an iterable to be worked with

    def __next__(self):
        if self.current < self.high:
            num = self.current
            self.current += 1
            return num
        raise StopIteration

for x in Counter(543, 754):
    print(x)
