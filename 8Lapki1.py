'''Дан список чисел. Определите, сколько чисел в нем различны. Подсказка: многие задачи этого модуля решаются в одну строку:)

Sample Input:

8 11 1 8
Sample Output:

3'''
numbers = set(input().split())
print(len(numbers))
