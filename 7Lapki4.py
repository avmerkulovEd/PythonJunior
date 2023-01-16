'''На вход программы подается несколько стран со списками их городов в формате:

Россия Москва Петербург Новгород Калуга

После вводится еще одна строка, содержащая название города.

Выведите название страны, в которой находится этот город.

Sample Input:

3
Германия Берлин Гамбург Мюнхен Кёльн
Россия Москва Петербург Новгород Калуга 
Марокко Касабланка Рабат Фес 
Петербург
Sample Output:

Россия'''
k = input()
country = {}
for i in range(int(k)):
    slov = input().split()
    country[slov[0]] = slov[1::]
gorod = input()    
for k, v in country.items():
    if gorod in v:
        print(k)
