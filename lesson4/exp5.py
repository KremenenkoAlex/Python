from functools import reduce

list = [el for el in range(100, 1000 + 1) if el % 2 == 0]
print(f'четные числа от 100 до 1000 - {list}')

sum_all = reduce(lambda x, y: x + y, list, 1)

list = [el for el in range(100, 1000) if el % 2 == 0]
print(f'четные числа от 100 до 1000 - {list}')

sum_all = reduce(lambda x, y: x + y, list)


print(sum_all)