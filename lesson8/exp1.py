class Date:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def extract(cls, day_month_year):
        my_date = []
        for i in day_month_year.split():
            if i != "-": my_date.append(i)

        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def valid(day, month, year):
        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2021 >= year >= 0:
                    return f"Дата корректна"
                else:
                    return f"Не корректный год"
            else:
                return f"Не корректный месяц"
        else:
            return f"Не корректный день"

    def __str__(self):
        return f'Текущая дата {Date.extract(self.day_month_year)}'


today = Date('19 - 1 - 2021')
print(today)
print(Date.valid(1, 12, 2010))
print(Date.valid(19, 1, 2022))
print(today.valid(19, 13, 2021))
print(today.valid(32, 12, 2021))
print(Date.extract('19 - 1 - 2021'))
print(today.extract('19 - 1 - 2021'))


