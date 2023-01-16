'''На вход программы подается список чисел. Напишите функцию, которая вычисляет произведение чисел этого списка и возвращает ответ.

Sample Input:

8 11 4 5
Sample Output:

1760'''
numbers = map(int, input().split())        

def product(numbers):
    sum_so_far = 1
    for i in numbers:
        sum_so_far *= i
    return sum_so_far 

result = product(numbers)
print(result)
