from itertools import cycle

count = 0
for item in cycle('ABCD'):
    if count > 10:
        break
    print(item)
    count += 1