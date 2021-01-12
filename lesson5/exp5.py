def summary():
    try:
        with open("text5.txt", "w") as my_file:
            line = input("Введите числа \n")
            my_file.writelines(line)
            my_line = line.split()

            print(sum(map(int, my_line)))
    except IOError:
        print('Ошибка в файле')
    except ValueError:
        print('Вы ввели не число')
summary()
