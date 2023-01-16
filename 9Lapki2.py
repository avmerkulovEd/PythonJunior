'''На вход программы подается число. Напишите функцию, которая возвращает произведение цифр, из которых это число состоит.

Например, число 3279 состоит из цифр 3, 2, 7, 9, их произведение 3*2*7*9 = 378.

Sample Input:

3279
Sample Output:

378'''
number = int(input())        

def product(number):
    sum_so_far = 1
    chis = 1
    number = abs(number)
    while number > 0:
        chis = number % 10
        number = number // 10
        sum_so_far *= chis
    return sum_so_far

result = product(number)
print(result)
