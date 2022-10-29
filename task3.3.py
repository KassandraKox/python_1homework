'''Задайте список из вещественных чисел. Напишите программу, которая 
найдёт разницу между максимальным и минимальным значением дробной 
части элементов.
Пример:
- [1.1, 1.2, 3.1, 5, 10.01] => 0.2'''

lst = [1.1, 1.2, 3.1, 5, 10.01]
max_lst = 0
min_lst = lst[0]
for i in range (0, len(lst)):
    if lst[i]- int(lst[i]) < min_lst:
        min_lst = lst[i]- int(lst[i])
    if lst[i]- int(lst[i]) > max_lst:
        max_lst = lst[i]- int(lst[i])
diff = max_lst - min_lst
print(round(diff, 2))
