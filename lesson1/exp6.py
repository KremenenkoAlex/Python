a = int(input("Введите результаты пробежки первого дня в км "))
b = int(input("Введите общий желаемый результат в км "))
days = 1
km = a
while km < b:
        a = a + 0.1 * a
        days += 1
        km += a
print("На {} день спортсмен достиг результата {} км".format(days, b))