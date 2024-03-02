#Write a program using generator to print the even numbers between 0 and n
#in comma separated form where n is input from console.

n = int(input())
even_nums_gen = (x for x in range(n) if x % 2 == 0)
for i in even_nums_gen:
    print(i)