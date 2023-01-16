'''Напишите функцию in_interval, которая принимает на вход три числа a, b, c и возвращает True, если число c находится в промежутке от a до b:

c \in [a, b]c∈[a,b]

В ином случае функция должна возвращать False.

Sample Input:

8 11 10
Sample Output:

True'''
a, b, c = map(int, input().split())

def in_interval(x, y, z):
    if (z >= x) and (z <= y):
        sum_list = 'True'
    else:
        sum_list = 'False'
    return sum_list

print(in_interval(a, b, c))
