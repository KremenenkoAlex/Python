goods = int(input("Введите количество товара "))
my_list = []
n = 1
while n <= goods:
    my_list.append(
        (dict({
            'название': (input('Введите название: ')),
            'цена': (input('Введите цену: ')),
            'количество': (input('Введите количество: ')),
            'eд': (input('Введите единцы измерения: ')),
        }))
    )
    n += 1
print('список товаров:{}'.format(my_list))