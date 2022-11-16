'''Дана последовательность чисел. Получить список уникальных элементов заданной последовательности, список 
повторяемых и убрать дубликаты из заданной последовательности.
Пример:
[1, 2, 3, 5, 1, 5, 3, 10] => [2, 10] и [1, 3, 5] и [1, 2, 5, 3, 10]'''

from random import randint

N = 10
init_numbers = [randint(1, N) for i in range(10)]
print(f'Сформирована последовательность: {init_numbers}')
print('Из них уникальные:', [n for n in set(init_numbers) if init_numbers.count(n) == 1])
print('Из них повторяемые:', [n for n in set(init_numbers) if init_numbers.count(n) > 1])
print('Список дубликатов:', list(set(init_numbers)))