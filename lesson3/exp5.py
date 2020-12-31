def func_sum ():
    sum_result = 0
    a = False
    while a == False:
        number = input("Введите числа через пробел, в случае выхода нажмите !  ").split()
        result = 0
        for i in range(len(number)):
            if number[i] == "!":
                a = True
                break
            else:
                result = result + int(number[i])
        sum_result = sum_result + result
        print("Сумма чисел равна -  {} ".format(sum_result))
    print("Конечная сумма чисел равна -  {} ".format(sum_result))
func_sum()