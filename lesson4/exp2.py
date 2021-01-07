from random import randint
list = [randint(0, 100) for i in range(10)]
print("Исходный код: {}".format(list))

list_new = []

for i in range(1,len(list)):
    if list[i] > list[i-1]:
        list_new.append(list[i])

print("Код после сравнения: {}".format(list_new))