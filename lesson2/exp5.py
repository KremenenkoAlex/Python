my_list = [7, 5, 3, 3, 2]
print(my_list)
number = int(input("Введите число: (Для выхода нажмити 0)"))
for i in my_list:
    if number == 0:
         break
    my_list.append(number)
    my_list.sort()
    my_list.reverse()
    print("текущий список - {}".format(my_list))
    number = int(input("Введите число "))








       # my_list.append(number)
       # my_list.sort()
      #  my_list.reverse()
      #  break
   # print(my_list)
