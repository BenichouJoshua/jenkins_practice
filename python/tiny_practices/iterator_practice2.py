
list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

myIter = iter(list)

while 1:
    try:
        print(next(myIter))
    except StopIteration:
        break    
        
myIter = iter(list)
while 1:
    try:
        print(next(myIter))
    except StopIteration:
        break    