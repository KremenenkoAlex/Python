rev = int(input("Введите выручку фирмы "))
cost = int(input("Введите издержки фирмы "))
if rev > cost:
    profit = rev / cost * 100
    print("Фирма работает с прибылью. Рентабельность выручки составила {} %".format(profit))
    workers = int(input("Введите количество сотрудников фирмы "))
    rev_work = rev / workers
    print("Прибыль в расчете на одного сторудника сотавила {}".format(rev_work))
else:
    print("Фирма работает в убыток")