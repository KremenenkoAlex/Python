list = []
n = int(input("Введите длинну массива : "))

for i in range(0, n):
       list.append(i)
print(list)

j = 0
for i in range(int(len(list) / 2)):
    list[j], list[j + 1] = list[j + 1], list[j]
    j += 2

print(list)