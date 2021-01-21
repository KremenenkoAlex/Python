class Exception:
    def __init__(self, *args):
        self.my_list = []

    def my_input(self):
        while True:
            try:
                arg = int(input("Введите число - "))
                self.my_list.append(arg)
                print(f"Текущий список - {self.my_list} \n")
            except:
                print(f"Вы ввели не число")
                attempt = input("Попробовать еще? y/n ")
                if attempt == "Y" or attempt == "y":
                    print(new_try.my_input())
                elif attempt == "N" or attempt == "n":
                    return ("Вы вышли")
                else:
                    return ("Вы вышли")

new_try = Exception(1)
print(new_try.my_input())