
class CustIterator:
    def __init__(self, squares):
        self.squares = squares
        self.index = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index < len(self.squares):
            x = self.squares[self.index]
            self.index += 1
            return x
        else:
            raise StopIteration    

        
        

def even_num_generator(numbers):
    for x in numbers:
        if x % 2 == 0:
            yield x

even_squares = [x * x for x in even_num_generator(range(1,11))]
obj = CustIterator(even_squares)

for x in obj:
    print(x)