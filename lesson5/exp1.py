my_func = open('text.txt', 'w')
line = input("Введите текст \n")
while line:
    my_func.write(line)
    line = input("Введите текст \n")
    if not line:
        break
my_func.close()

my_func = open('text.txt', 'r')
content = my_func.readlines()
print(content)
my_func.close()