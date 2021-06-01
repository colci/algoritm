from collections import defaultdict 
dd_company = defaultdict(list)
total_profit = 0
n = int(input('Введите количество предприятий'))
for i in range(n):
    name = input(f"Введите наименование {i+1}-й компании: ")
    for k in range(4):
        profit = float(input(f"Введите прибыль за {k+1}-й квартал для компании {name}: "))
        dd_company[name].append(profit)
    dd_company[name].append(sum(dd_company[name]))
    total_profit += dd_company[name][4]
    
    
if n > 0:
    sprofit = total_profit / n
    res1 =[]
    res2 =[]
    print(f'Средняя прибыль по компаниям {sprofit}')
    for key in dd_company:
        if sprofit < dd_company[key][4]:
            res1.append(key)
        else:
            res2.append(key)
    
    print(f'Компании с прибылью выше среднего: ')
    for i in res1:
        print(i)
    
    print(f'Компании с прибылью ниже или равной средней: ')
    for i in res2:
        print(i)
