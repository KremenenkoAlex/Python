with open("text3.txt", "r") as my_file:
    name = []
    sal = []
    list = my_file.read().split('\n')
    for i in list:
        i = i.split()
        if int(i[1]) < 20000:
            sal.append(i[0])
        name.append(i[1])
print(f'Оклад меньше 20.000 {name}, средний оклад {sum(map(int, sal)) / len(sal)}')