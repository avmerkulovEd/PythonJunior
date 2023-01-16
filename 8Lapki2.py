'''Дан список чисел. Выведите все различные числа в нем на экран в порядке возрастания

Sample Input:

8 11 1 15
Sample Output:

1 8 11 15'''
numbers = map(int, input().split())
mnog = set(numbers)
print(*sorted(mnog))
