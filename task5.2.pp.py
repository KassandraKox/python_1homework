'''Создайте программу для игры с конфетами человек против человека. Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая 
ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента 
достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
a) Добавьте игру против бота
b) Подумайте как наделить бота интеллектом'''

from random import randint, choice  # подключить модуль случайных чисел
# условия
greeting = ('''Давай сыграем в игру!" На столе лежат конфеты, за один ход можно взять не более определённого количества. Итак, начнём!''')
# сообщения на выбор      
messages = ['возьми конфеты.', 'сколько конфет возьмешь?', 'твой ход.']
# функция игры 
def start_game(candy, max, player, messages):
    count = 0
    while candy > 0:
        print(f'{player[count%2]}, {choice(messages)}')
        step = int(input())
        if step > candy or step > max:
            print(f'Это слишком много, можно взять не более {max} конфет, у нас всего {candy} конфет.')
            print(f'Попробуй ещё раз.')
            step = int(input())
        candy -= step
        if candy > 0:
            print(f'Осталось {candy} конфет.')
        else: print('Конфет не осталось.')
        count +=1
    return player[not count%2]

print(greeting)

player1 = input('Представься, пожалуйста:  ')
player2 = input('Против кого ты играешь?   ')
player = [player1, player2]

candy = 100
max = 28

winner = start_game(candy, max, player, messages)
print(f'Поздравляю, {winner}! Забирай свои конфеты!')