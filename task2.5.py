# Реализуйте алгоритм перемешивания списка.

import random
list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f'Первоначальный список: {list}')
random.shuffle(list)
print(f'Список после перемешивания: {list}')