'''Задана натуральная степень k. Сформировать случайным образом список
коэффициентов (значения от 0 до 100) многочлена и записать в файл 
многочлен степени k.
Пример:
k=2 => 2x^2 + 4x + 5 = 0 или x^2 + 5 = 0 или 10x^2 = 0'''

import random

random.seed
k = int(input('Введите степень k:'))
if k<0:
    print('Некорректный ввод')
else:

    lst = []
    for i in range(k+1):
        lst.append(random.randint(1, 101))
    print(f'Сгенерирован список коэффициентов: {lst}')
    for i in range(k,0,-1):
        print(f'{lst[i]}*x**{i} + ', end='')
    print(f'{lst[0]}')

    with open('task4.txt','w') as data:
        for i in range(k,0,-1):
            data.write(f'{lst[i]}*x**{i} + ')
        data.write(f'{lst[0]}\n')