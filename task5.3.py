'''Создайте программу для игры в ""Крестики-нолики""'''

# Нарисовать доску
board = list(range(1,10))

def draw_board(board):
   print("-------------")
   for i in range(3):
      print("|", board[0 + i * 3], "|", board[1 + i * 3], "|", board[2 + i * 3], "|")
      print("-------------")

# Сделать ход 
def X_or_O(step):
   while True:
      answer = int(input("Куда поставить " + step + "? "))
      if 1 <= answer <= 9:
         if(str(board[answer - 1]) not in "XO"):
            board[answer - 1] = step
            return True
         else:
            print("Эта клетка занята.")

# Проверка на выигрыш
def win_check(board):
   win_coordinate = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
   for each in win_coordinate:
       if board[each[0]] == board[each[1]] == board[each[2]]:
          return board[each[0]]
   return False

# Запуск игры
def start(board):
    counter = 0
    while True:
        draw_board(board)
        if counter % 2 == 0:
           X_or_O("X")
        else:
           X_or_O("O")
        counter += 1
        if counter > 4:
           tmp = win_check(board)
           if tmp:
              print(tmp, "выиграл!")
              return True
              break
        if counter == 9:
            print("Ничья!")
            break
start(board)