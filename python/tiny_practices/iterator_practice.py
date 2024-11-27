
class Iterator:
    def __init__(self, start):
        self.start = start
        self.end = start + 1000

    def __iter__(self):
        return self

    def __next__(self):
        if not self.start >= self.end:
            x = self.start
            self.start += 2
            return x
        else:
            raise StopIteration

myClass = Iterator(100)
myiter = iter(myClass)

""" for x in myiter:
    print(x)
 """
mc = Iterator(980)
iter = iter(mc)

try:
    print(next(iter))
    print(next(iter))

except StopIteration:
    pass    