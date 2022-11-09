'''Задайте последовательность чисел. Напишите программу, которая 
выведет список неповторяющихся элементов исходной последовательности.'''

import random

random.seed                                         # количество чисел в массиве
N = random.randint(3, 10)

lst = []
for i in range(N):
    lst.append(random.randint(0, 20))               # числа в массиве от до
print(f'Сгенерирован список: {lst}')

check_lst = []
for i in lst:
    if i in check_lst:
        continue
    else:
        check_lst.append(i)
print(f'Список неповторяющихся элементов: {check_lst}')