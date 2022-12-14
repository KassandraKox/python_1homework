'''Напишите программу вычисления арифметического выражения заданного 
строкой. Используйте операции +,-,/,*. приоритет операций стандартный.
Пример:
2+2 => 4; 1+2*3 => 7; 1-2*3 => -5;
Добавьте возможность использования скобок, меняющих приоритет операций.
Пример:
1+2*3 => 7; (1+2)*3 => 9;'''

sign = {'+': (1, lambda x, y: x + y), '-': (1, lambda x, y: x - y),       # операторы математических выражений
        '*': (2, lambda x, y: x * y), '/': (2, lambda x, y: x / y)}

def eval_(formula_string):

    def parse(formula_string):
        number = ''
        for s in formula_string:
            if s in '1234567890.': # если символ - цифра, то собираем число
                number += s  
            elif number: # если символ не цифра, то выдаём собранное число и начинаем собирать заново
                yield float(number) 
                number = ''
            if s in sign or s in "()": # если символ - оператор или скобка, то выдаём как есть
                yield s 
        if number:  # если в конце строки есть число, выдаём его
            yield float(number)  

    def shunting_yard(parsed_formula):
        stack = []  # в качестве стэка используем список
        for token in parsed_formula:
            '''если элемент - оператор, то отправляем дальше все операторы из стека, 
            чей приоритет больше или равен пришедшему, до открывающей скобки или опустошения стека.
            здесь мы пользуемся тем, что все операторы право-ассоциативны'''
            if token in sign: 
                while stack and stack[-1] != "(" and sign[token][0] <= sign[stack[-1]][0]:
                    yield stack.pop()
                stack.append(token)
            elif token == ")":
                '''если элемент - закрывающая скобка, выдаём все элементы из стека, до открывающей скобки,
                а открывающую скобку выкидываем из стека.'''
                while stack:
                    x = stack.pop()
                    if x == "(":
                        break
                    yield x
            elif token == "(":
                # если элемент - открывающая скобка, просто положим её в стек
                stack.append(token)
            else:
                # если элемент - число, отправим его сразу на выход
                yield token
        while stack:
            yield stack.pop()

    def calc(polish):
        stack = []
        for token in polish:
            if token in sign:  # если приходящий элемент - оператор,
                y, x = stack.pop(), stack.pop()  # забираем 2 числа из стека
                stack.append(sign[token][1](x, y)) # вычисляем оператор, возвращаем в стек
            else:
                stack.append(token)
        return stack[0] # результат вычисления - единственный элемент в стеке

    return calc(shunting_yard(parse(formula_string)))
