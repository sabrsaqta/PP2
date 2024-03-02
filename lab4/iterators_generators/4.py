#Implement a generator called squares to yield the square of all numbers from (a) to (b). Test it with a "for" loop and print each of the yielded values.
a, b = int(input()), int(input())

def mygen(a, b):
    squares = (x**2 for x in range(a, b))
    for i in squares:
        yield i

d = mygen(a, b)
for i in range(a, b):
    print(next(d))