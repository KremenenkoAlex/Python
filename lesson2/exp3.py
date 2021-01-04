n = int(input("Введите месяц : "))
list_dict = {1: "январь", 2: "февраль", 3: "март", 4: "апрель", 5: "май", 6: "июнь", 7: "июль", 8: "август", 9: "сентябрь", 10: "октябрь", 11: "ноябрь", 12: "декабрь"}
list = ["зима", "весна", "лето", "осень"]
if n == 1 or n == 2 or n == 12:
    m = list_dict[n]
    s = list[0]
    print("{}-й месяц это {} - {}".format(n, m, s))

elif n == 3 or n == 4 or n == 5:
    m = list_dict[n]
    s = list[1]
    print("{}-й месяц это {} - {}".format(n, m, s))

elif n == 6 or n == 7 or n == 8:
    m = list_dict[n]
    s = list[2]
    print("{}-й месяц это {} - {}".format(n, m, s))

elif n == 9 or n == 10 or n == 11:
    m = list_dict[n]
    s = list[3]
    print("{}-й месяц это {} - {}".format(n, m, s))

else:
    print("Нет такого мусяца")