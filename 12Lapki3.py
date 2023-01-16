'''Напишите свой первый класс Triangle, в котором есть поля
angle_1, angle_2, angle_3
и который при инициализации проверяет, что все введенные числа положительные и что сумма углов треугольника равна 180°.
В случае, если треугольник может существовать, конструктор класса должен напечатать текст Triangle initialized, а если такой треугольник существовать не может, то Initialization failed'''
class Triangle:

    def __init__(self, ugol1, ugol2, ugol3):
        self.an1 = ugol1
        self.an2 = ugol2
        self.an3 = ugol3
        
    def proverka(self):
        ugol1 = angles[0]
        ugol2 = angles[1]
        ugol3 = angles[2]
        if (ugol1 + ugol2 + ugol3) == 180 and (ugol1 > 0) and (ugol2 > 0) and (ugol3 > 0):
            print('Triangle initialized')
        else:
            print('Initialization failed')
        
angles = list(map(int, input().split()))

otvet = Triangle(angles[0], angles[1], angles[2])
otvet.proverka()
