my_func = open("text2.txt", "r")
content = my_func.readlines()
print("Количество строк в файле - {}".format(len(content)))

my_func = open("text2.txt", "r")
content = my_func.read()
content = content.split()
print("Общее количество слов - {}".format(len(content)))
my_func.close()