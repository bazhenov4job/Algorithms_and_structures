from collections import ChainMap, deque, namedtuple


n = int(input('Введите количество предприятий: '))

company = namedtuple('company', 'name, profit', defaults=['', 0])
company_1 = company('', 0)
company_chain = ChainMap(company_1)
sum = 0

for i in range(n):
    name = input('Введите название предприятия: ')
    profit = int(input('Введите прибыль предприятия за 4 квартала: '))
    sum += profit
    company_chain = company_chain.new_child(company_1._replace(name=name, profit=profit))

average_profit = sum / n
above_average = deque()
below_average = deque()

for i in range(n):
    if company_chain.maps[i].profit >= average_profit:
        above_average.append(company_chain.maps[i].name)
    else:
        below_average.append(company_chain.maps[i].name)

print(f'Предприятия с прибылью выше среднего: {list(above_average)}')
print(f'Предприятия с прибылью ниже среднего: {list(below_average)}')
