# Напишите программу для проверки истинности утверждения
#  ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений 
# предикат.
for X in [0, 1]:
    for Y in [0, 1]:
        for Z in [0, 1]:
            print(X, Y, Z)
            if not (X or Y or Z) == (not X and not Y and not Z):
                print('Истина')
            else:
                print('Ложь')