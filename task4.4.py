'''Задана натуральная степень k. Сформировать случайным образом список
коэффициентов (значения от 0 до 100) многочлена и записать в файл 
многочлен степени k.
Пример:
k=2 => 2x^2 + 4x + 5 = 0 или x^2 + 5 = 0 или 10x^2 = 0'''

import random

A = random.randint(0, 100)
B = random.randint(0, 100)
C = random.randint(0, 100)
k = 2

with open("Task4.txt", "w") as Task4:
    print(f'A = {A}, B = {B}, C = {C}', file=Task4)
    if B != 0 or C != 0:
        print(f'{A}*x^{k} + {B}*x + {C} = 0', file=Task4)
    if B == 0 and C != 0:
        print(f'{A}*x^{k} + {C} = 0', file=Task4)
    if B == 0 and C == 0:
        print(f'{A}*x^{k} = 0', file=Task4)