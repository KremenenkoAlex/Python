class Store:

    def __init__(self, name, price, quantity, number_of_lists):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.numb = number_of_lists
        self.my_store_full = []
        self.my_store = []
        self.my_unit = {'Модель устройства': self.name, 'Цена за ед': self.price, 'Количество': self.quantity}

    def __str__(self):
        return f'{self.name} цена {self.price} количество {self.quantity}'

    def reception(self):
        try:
            unit = input(f'Введите наименование ')
            unit_price = int(input(f'Введите цену за ед '))
            unit_quantity = int(input(f'Введите количество '))
            unit_all = {'Модель устройства': unit, 'Цена за ед': unit_price, 'Количество': unit_quantity}
            self.my_unit.update(unit_all)
            self.my_store.append(self.my_unit)
            print(f'Текущий список -\n {self.my_store}')
        except:
            return f'Ошибка ввода данных'

        print(f'Для выхода - Q, продолжение - Enter')
        q = input(f'---> ')
        if q == 'Q' or q == 'q':
            self.my_store_full.append(self.my_store)
            print(f'Весь склад -\n {self.my_store_full}')
            return f'Выход'
        else:
            return Store.reception(self)

class Printer(Store):
    def to_print(self):
        return f'to print smth {self.numb} times'

class Scanner(Store):
    def to_scan(self):
        return f'to scan smth {self.numb} times'

class Copier(Store):
    def to_copier(self):
        return f'to copier smth  {self.numb} times'

unit_1 = Printer('hp', 3000, 10, 5)
unit_2 = Scanner('Canon', 2500, 5, 10)
unit_3 = Copier('Xerox', 3500, 4, 15)
print(unit_1.reception())
print(unit_2.reception())
print(unit_3.reception())
print(unit_1.to_print())
print(unit_2.to_scan())
print(unit_3.to_copier())