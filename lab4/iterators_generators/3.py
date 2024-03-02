#Define a function with a generator which can iterate the numbers, which are divisible by 3 and 4,
#between a given range 0 and n.

n = int(input())

def myfunc(n):
    d = (x for x in range(n) if x % 3 == 0 and x % 4 == 0)
    for i in d:
        print(i)
myfunc(n)
