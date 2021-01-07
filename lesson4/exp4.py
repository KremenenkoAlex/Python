from random import randint
list = [randint(0, 10) for i in range(20)]
print("Исходный код: {}".format(list))

new_list = [el for el in list if list.count(el) < 2]
print("Новый код: {}".format(new_list))