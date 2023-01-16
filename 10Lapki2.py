'''На вход программы подаются числа. Напишите функцию mean, которая принимает все переданные числа и возвращает сначала их все, а потом их среднее. 
Sample Input:

9 13 2
Sample Output:

9 13 2 8.0'''
values = tuple(map(int, input().split()))

def mean (fvalues):
    sred = 0
    for n in range(len(fvalues)):
        sred += fvalues[n]
    sred /= len(fvalues)
    return(*fvalues, sred)

print(*mean(values))
