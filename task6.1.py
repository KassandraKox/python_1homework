'''Напишите программу вычисления арифметического выражения заданного строкой. Используйте операции
+,-,/,*. приоритет операций стандартный.
Пример:
2+2 => 4; 1+2*3 => 7; 1-2*3 => -5;
Добавьте возможность использования скобок, меняющих приоритет операций.
Пример:
1+2*3 => 7; (1+2)*3 => 9;'''

from random import randint, choice

sign = ['+', '-', '*', '/', '**']
digits = []
print('Введи количество цифр:')
N = int(input())

def define_veribles(N):
    for i in range(N):
        digits[i] = randint(1, 9)
    return digits

def write_expression(sign, digits):
    for i in range(N):
        expression += digits[i]
        expression += choice(sign)
    return expression

# solution(digit, sign)
define_veribles(N)
print(write_expression(sign, digits))


#def solution(digit, sign):