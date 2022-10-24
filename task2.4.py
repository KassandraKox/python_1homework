'''Задайте список из N элементов, заполненных числами из промежутка
 [-N, N]. Найдите произведение элементов на указанных позициях. 
 Позиции хранятся в файле file.txt в одной строке одно число.'''

from itertools import product
from random import randint  # подключить модуль случайных чисел
numbers = []
N = int(input('Введите число: '))
for i in range(N):
    numbers.append(randint (-N,N))  # заполнить массив случайными числами
print(numbers)

x = randint (0, N)
input(f'Позиция первого элемента: {x}')
y = randint (0, N)
input(f'Позиция второго элемента: {y}')

for i in range(len(numbers)):
    product = numbers[x] * numbers[y]
print(f'Произведение элементов: {numbers[x]} * {numbers[y]} =', product)