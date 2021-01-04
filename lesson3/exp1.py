arg_1 = int(input("Введите первое число: "))
arg_2 = int(input("Введите второе число: "))

def del_arg(arg_1, arg_2):

    if arg_1 == 0 or arg_2 == 0:
        print("На ноль делить нельзя")
    else:
        result = arg_1 / arg_2
        print('{0:.2f}'.format(result))

del_arg(arg_1, arg_2)


