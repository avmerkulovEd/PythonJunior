'''На вход программы подается список имён и возрастов участников соревнований в формате:

4
Николай 20
Наталья 17
Дарья 22 
Сергей 19
Где 4 -- число строк с данными участников, которые последуют дальше.

Напишите функцию, которая вернет имя и возраст самого младшего участника. 

Sample Input:

4
Николай 20
Наталья 17
Дарья 22 
Сергей 19
Sample Output:

Наталья 17'''

k = int(input())
slovar = {}
for i in range(0, k): 
    name, age = input().split()
    slovar[age] = name
    
def get_youngest(fslovar):
    list_slov = sorted(fslovar)
    min_age = list_slov[0]
    min_name = slovar[min_age]
    return min_name, min_age
    
x, y = get_youngest(slovar)
print(x, y)
