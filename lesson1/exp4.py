n = int(input("Введите целое положительное число "))
max = n % 10
while n >= 1:
    n = n // 10
    if n > max:
        max = n
    else:
        print("Максимальное цифра в числе ", max)
        break