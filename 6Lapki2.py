'''Вводится целое положительное число n. Выведите True, если число простое и False, если составное (то есть, имеет делители, отличные от 1 и самого себя).'''
number = int(input())
count = 0
for i in range(1, number):
    if number % i == 0:
        count += 1
    else: count = count    
print(True if count<=2 else False)
