'''На вход программе подается база продаж канцелярского магазина в виде

Название товара	Продано единиц	Цена
Бумага	12	400
Ручка	44	20
Конверт	22	6
После этого вводится название товара. Выведите, сколько магазин заработал на продажах этого товара в виде целого числа.

Sample Input:

3
Бумага 12 400
Ручка 44 20
Конверт 22 6
Ручка
Sample Output:

880'''

x = input()

trade = {}
for i in range(int(x)):
    kans = input().split()
    trade[kans[0]] = kans[1::]
pen = input()
for k, v in trade.items():
    if k == pen:
        print(int(v[0]) * int(v[1]))