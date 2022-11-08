'''Задайте натуральное число N. Напишите программу, которая составит 
список простых множителей числа N.'''

N = int (input('Введите число: '))
lst = []

for i in range(1, N + 1):
    if N % 2 == 0:
        lst = lst + [2]
        N = N // 2
        # print(N, lst) 
    elif N % 3 == 0:
        lst = lst + [3]
        N = N // 3
        # print(N, lst) 
    elif N % 5 == 0:
        lst = lst + [5]
        N = N // 5
        # print(N, lst) 
    elif N % 7 == 0:
        lst = lst + [7]
        N = N // 7
        # print(N, lst)
    else:
        lst = lst + [N]
        print(f'Простые множители числа {N} равны {lst}')
        break