'''На вход программы подаются kk пар слов: слово на русском и его перевод на испанский. Последней строкой подается еще одно слово на русском. Выведите перевод последнего слова.

Формат входных данных:

число kk
kk пар слов
слово, перевод которого нужно вывести
Sample Input:

3
коза cabra
кошка gato
мышь ratón
кошка
Sample Output:

gato'''
k = int(input())
vocabulary = {}
for i in range(0, k): 
    ru, sp = input().split()
    vocabulary[ru] = sp
slovo = input()    
print(vocabulary.get(slovo))   
