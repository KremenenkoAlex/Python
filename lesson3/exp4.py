x = int(input("Введите первое число: "))
y = int(input("Введите второе число: "))

def stepen(x, y):
    return x ** y
stepen(x,y)
print("возведение в степень с помощью оператора: результат ", stepen(x,y))


def x_pow(x, y):
    return x ** y

x_pow(x, y)
print("возведение в степень с помощью без оператора: результат ", x_pow(x, y))