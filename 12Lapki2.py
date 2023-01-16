'''Класс User уже объявлен и инициализирован в шаблоне. Добавьте функцию get_orders(), которая вернет список покупок человека в формате:
apple, sandwich, coffee
Sample Input:

Sample Output:

apple, sandwich, coffee'''
class User:
    d = None
    name = None
    order = {}

    def __init__(self, identifier, first_name):
        self.id = identifier
        self.name = first_name

    def total_sum(self):
        purchase = 0
        for item, price in self.order.items():
            purchase += price
        return purchase

    def add_purchase(self, item, price):
        self.order.update({item: price})   

    def get_orders(self):
        forder = self.order
        return forder

maria = User(10, "Maria")

maria.add_purchase("apple", 20)
maria.add_purchase("sandwich", 120)
maria.add_purchase("coffee", 100)

print(", ".join(maria.get_orders()))
