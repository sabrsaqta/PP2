#Create a generator that generates the squares of numbers up to some number N.

n = int(input())
b = (x**2 for x in range(n))
for i in range(n):
    print(next(b))

# #OR
    
# n = int(input())
# squared_nums_gen = (x**2 for x in range(n))
# for i in squared_nums_gen:
#     print(i)