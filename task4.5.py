'''Даны два файла, в каждом из которых находится запись многочлена. 
Задача - сформировать файл, содержащий сумму многочленов.'''

import random

A = random.randint(-100, 100)
B = random.randint(-100, 100)
C = random.randint(-100, 100)

A1 = random.randint(-100, 100)
B1 = random.randint(-100, 100)
C1 = random.randint(-100, 100)

k = 2
# 1 СПОСОБ
with open ("Task4_1.txt", "w") as Task_4_1:
    print(f'{A}*x^{k} + {B}*x + {C} = 0', file= Task_4_1)
with open ("Task4_2.txt", "w") as Task_4_2:
    print(f'{A1}*x^{k} + {B1}*x + {C1} = 0', file= Task_4_2)
with open ("Task4_3.txt", "w") as Task_4_3:
    print(f'{A1+A}*x^{k} + {B1+B}*x + {C1+C} = 0', file= Task_4_3)
#  2 СПОСОБ
with open('Task4_1.txt','r') as file:
    Task_4_1 = file.readline()
    list_1 = Task_4_1
with open('Task4_2.txt','r') as file:
    Task_4_2 = file.readline()
    list_2 = Task_4_2

print(f'{list_1} + {list_2}')
sum= list_1 + list_2

with open('Task4_3.txt', 'w', encoding='utf-8') as file:
    file.write(list_1 + list_2)