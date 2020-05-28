from fizz import fizz
from buzz import buzz

def fizzbuzz(n):
    if n == 0:
        return n
    if n % 3 == 0 and n % 5 ==0:
        return 'fizzbuzz'
    if fizz(n) == 'fizz':
        return 'fizz'
    if buzz(n) == 'buzz':
        return 'buzz'
    return n

