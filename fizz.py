def fizz(n):
    if n % 3 == 0:
        return'fizz'
    else:
        return n
for n in range(1,50):
    print(fizz(n))
