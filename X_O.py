mainboard = {0: {0: '-', 1: '-', 2: '-'}, 1: {0: '-', 1: '-', 2: '-'}, 2: {0: '-', 1: '-', 2: '-'}}
def draw_board(mainboard):
   print("  0 1 2")
   print(f"0 {mainboard[0][0]} {mainboard[0][1]} {mainboard[0][2]}")
   print(f"1 {mainboard[1][0]} {mainboard[1][1]} {mainboard[1][2]}")
   print(f"2 {mainboard[2][0]} {mainboard[2][1]} {mainboard[2][2]}")

def turn(player_token):
    valid = False
    while not valid:
        print("Ход", player_token)
        vert = input("Введите номер столбца")
        gor = input("Введите номер строки")
        try:
            vert = int(vert)
            gor = int(gor)
        except:
            print("Некорректный ввод. Вы уверены, что ввели число?")
            continue
        if gor in range(3) and vert in range(3):
            if mainboard[gor][vert] == "-":
                mainboard[gor][vert] = player_token
                valid = True
            else:
                print("Эта клетка уже занята!")
        else:
            print("Некорректный ввод. Введите число от 0 до 2.")

def check_win(mainboard):
    a, b, c = dict.values(mainboard)
    board = (*dict.values(a), *dict.values(b), *dict.values(c))
    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for each in win_coord:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False

def main(mainboard):
    counter = 0
    win = False
    while not win:
        draw_board(mainboard)
        if counter % 2 == 0:turn("X")
        else:turn("O")
        counter += 1
        if counter > 4:
            tmp = check_win(mainboard)
            if tmp:
                print(tmp, "выиграл!")
                win = True
                break
        if counter == 9:
            print("Ничья!")
            break
    draw_board(mainboard)
main(mainboard)
input("Нажмите Enter для выхода!")