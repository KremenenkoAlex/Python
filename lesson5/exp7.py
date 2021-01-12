import json
profit = {}
pr = {}
prof = 0
prof_aver = 0
i = 0
with open('text7.txt', 'r') as file:
    for line in file:
        name, firm, earning, damage = line.split()
        profit[name] = int(earning) - int(damage)
        if profit.setdefault(name) >= 0:
            prof = prof + profit.setdefault(name)
            i += 1
    if i != 0:
        prof_aver = prof / i
        print('Прибыль средняя - {}'.format(prof_aver))
    else:
        print('Прибыль средняя - отсутсвует. Все работают в убыток')
    pr = {'средняя прибыль': round(prof_aver)}
    profit.update(pr)
    print('Прибыль каждой компании - {}'.format(profit))

with open('file7.json', 'w') as write_js:
    json.dump(profit, write_js)
    js_str = json.dumps(profit)
    print('Создан файл с расширением json со следующим содержимым: \n {}'.format(js_str))
