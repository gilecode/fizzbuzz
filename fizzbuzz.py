from fizz import fizz
from buzz import buzz

def fizzbuzz(n):
    if fizz(n) == 'fizz' and buzz(n) == 'buzz':
        return 'fizzbuzz'
    else:
        return n

