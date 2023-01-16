'''Во входной строке записана последовательность чисел через пробел. Для каждого числа выведите слово yes, если это число уже встречалось в последовательности или no, если не встречалось.

Sample Input:

5 3 5 4
Sample Output:

no no yes no'''
numbers = map(int, input().split())
mnog = set()
otvet = []
for i in numbers:
    n = int(i)
    if n in mnog:
        otvet.append("yes")
    else:
        otvet.append("no")
    mnog.add(n)
print(*otvet)
