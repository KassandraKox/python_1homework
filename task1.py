#Напишите программу, которая принимает на вход цифру, обозначающую день
# недели, и проверяет, является ли этот день выходным.
#Пример:
#- 6 -> да
#- 7 -> да
#- 1 -> нет
print("Введи цифру, обозначающую день недели:")
n = int(input())
if n >= 6:
    print("Выходной")
else:
    print("Не выходной")