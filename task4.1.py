'''Вычислить число c заданной точностью d
Пример:
при d = 0.001, π = 3.142 10^(-1) ≤ d ≤10^(-10)'''

count = int(input('Сколько знаков после запятой вывести из числа Пи? '))
pi = 0.0
sign = 1
for i in range(0, 100000001):
    pi += 4.0 * sign / (1 + 2 * i)
    # print(i, sum)
    sign = -sign

print(round(pi, count))