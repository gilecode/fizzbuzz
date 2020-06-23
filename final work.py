from fizz import fizz
from buzz import buzz
from fizzbuzz import fizzbuzz

def final(n):
    if n == 0:
        return n
    fizzbuzz(n)
    fizz(n)
    buzz(n)
    return n

for i in range (1,15):
    print(final(i))