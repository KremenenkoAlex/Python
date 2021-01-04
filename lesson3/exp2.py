name = str(input("Введите имя: "))
surename = str(input("Введите фамилию: "))
year_born = int(input("Введите год рождения: "))
town_born = str(input("Введите город рождения: "))
email = str(input("Введите email: "))
tel = int(input("Введите телефон: "))

def user (*arg):
    print("Данных о пользователе: {}, {}, {}, {}, {}, {}".format(name, surename, year_born, town_born, email, tel))

user()