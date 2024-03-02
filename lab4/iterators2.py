# d = [5, 1, 4, 6, 7]

# it = iter(d)
# it2 = iter(d)
# print(next(it))
# print(next(it2))
# print(next(it))
# print(next(it))
# print(next(it2))


# def get_list():
#     for x in [1, 2, 3, 4]:
#         yield x

# a = get_list()
# print(next(a))
# print(next(a))


# mylist = [1,2,3,4,5]
# it = iter(mylist)
# for i in it:
#     print(i)


n = int(input())
b = (x**2 for x in range(n))
for i in b:
    print(i)