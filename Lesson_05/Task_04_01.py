from collections import OrderedDict, defaultdict, deque
import random

ip_array_in = []
N = 3000

for i in range(10000):
    ip_array_in.append(f'{random.randint(185, 195)}.{random.randint(165, 175)}.{random.randint(0, 10)}.{random.randint(0, 255)}')

with open('log_file.txt', 'w', encoding='utf-8') as log_file:
    log_file.write('\n'.join(ip_array_in))

with open('log_file.txt', 'r', encoding='utf-8') as log_file:
    log = deque(log_file, N)

print(log)

spam = defaultdict(int)
# Временная переменная
data = OrderedDict()

for item in log:
    ip = item[:-1]

    if not ip.startswith('192.168.'):
        spam[ip] += 1
        data[ip] = 1

print(spam)
print(data)

data.update(spam)
print(data)

with open('data.txt', 'w', encoding='utf-8') as f:
    for key, value in data.items():
        f.write(f'{key} - {value}\n')
