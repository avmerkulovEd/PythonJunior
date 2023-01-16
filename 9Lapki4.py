'''Напишите функцию mult_list, которая принимает на вход два списка и возвращает список, состоящий из произведения элементов исходных. Гарантируется, что длины списков, поданных на вход, равны. 

Sample Input:

1 4 5
3 10 2
Sample Output:

3 40 10'''
first = list(map(int, input().split()))
second = list(map(int, input().split()))

def mult_list(first, second):
    sum_list = []
    for i in range(len(first)):
        element = first[i] * second[i]
        sum_list.append(element)
    return sum_list

result = mult_list(first, second)
print(*result)
