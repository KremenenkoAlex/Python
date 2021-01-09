my_list = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_list = []
with open("text4.txt", "r") as my_file:
    for i in my_file:
        i = i.split(' ', 1)
        new_list.append(my_list[i[0]] + ' ' + i[1])
    print(new_list)

with open("text4.txt", "w") as my_file:
    my_file.writelines(new_list)
