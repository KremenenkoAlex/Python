def fact(n):
    a = 1
    for i in range(1, n + 1):
        a *= i
        yield a

n = int(input("Факториал какого числа Вы хотели бы узнать? "))
for el in fact(n):
    print(el)