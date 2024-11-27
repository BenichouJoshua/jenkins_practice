
def Factorial(number):
    if number < 0:
        raise RuntimeError("Negative Input")
    if number == 0:
        return 1;
    return number * Factorial(number - 1)

for x in range(1, 5):
    print(Factorial(x))