#Implement a generator that returns all numbers from (n) down to 0.

n = int(input())
mygen = (x for x in range(n, -1, -1))
for i in mygen:
    print(i)