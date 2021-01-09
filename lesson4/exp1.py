work_hour = int(input("Введите время работы в часах: "))
hourly_rate = int(input("Введите ставку в час: "))
prize = int(input("Введите премию: "))
def my_func():
    salary = work_hour * hourly_rate
    return salary + prize
print("Размер зарплаты: {}".format(my_func()))
