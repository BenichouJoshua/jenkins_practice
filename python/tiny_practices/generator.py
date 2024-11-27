
def Square():
    for x in range(1,10):
        yield x * x

squares = [{x:x*x*x} for x in range(1,11)]
str = "je ne suis pas qui tu crois poto, assied toi et laisse moi t'expliquer ya hmar"
vowels = "AaeEeIiOoUu"
found_vowels = {letter for letter in str if letter in vowels}

for x in found_vowels:
    print(x)