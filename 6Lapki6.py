'''Пифагоровой тройкой называют такие целые числа aa, bb и cc, которые удовлетворяют условию 

a^2+b^2=c^2.a 
2
 +b 
2
 =c 
2
 .

На вход программы подается число kk. Найдите все пифагоровы тройки, такие, что c < kc<k и выведите их количество для заданного kk.

Например, если k = 10k=10, то условию удовлетворяет только одна тройка

3^2 + 4^2 = 5^23 
2
 +4 
2
 =5 
2
 

и программа должна вывести 1. 

Sample Input:

10
Sample Output:

1'''
k = int(input())
count = 0
result = []
a = 1
while a <= k:
    b = 1
    while b <= k:
        c = 1
        while c <= k:
            if (a * a + b * b) == (c * c) and c < k:
                if a not in result or b not in result or c not in result:
                    result.append(a)
                    result.append(b)
                    result.append(c)
                    result.append('-')
                    count += 1
            else: count = count
            c += 1
        b += 1
    a += 1
print(result)   
print(int(count))
