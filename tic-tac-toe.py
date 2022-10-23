import random

players = {
            0: {'symbol': 'X', 'name': 'Игрок X'},
            1: {'symbol': 'O', 'name': 'Игрок О'}
          }


def no_free_space_left(field):
    for i, field_x in enumerate(field):
        if None in field_x:
            return False
    return True


def is_player_won(field):
    """
    return: True/False (is win), player_id
    """
    player_win_id, win = check_x(field)
    if win:
        return True, player_win_id

    player_win_id, win = check_y(field)
    if win:
        return True, player_win_id

    player_win_id, win = check_diag(field)
    if win:
        return True, player_win_id

    return False, None
            

def check_diag(field):
    diag_1 = []
    diag_2 = []

    for x in range(len(field[0])):
        for y in range(len(field[0])):
            if x == y:
                diag_1.append(field[x][y])
                diag_2.append(field[x][len(field[0]) - 1 - y])

    player_win_id, win_diag_1 = if_line_win(diag_1)
    if win_diag_1:
            return player_win_id, win_diag_1

    player_win_id, win_diag_2 = if_line_win(diag_2)
    if win_diag_2:
            return player_win_id, win_diag_2

    return None, False


def check_y(field):
    for y, line in enumerate(field):

        field_size = len(line)

        line_to_check = [field[cell][y] for cell in range(field_size)]

        player_win_id, win = if_line_win(line_to_check)

        if win:
            return player_win_id, win

    return None, False


def check_x(field):
    """
    return player_win_id, True/False (win/not win), line_in_what_was_won
    """
    for x, line in enumerate(field):
            player_win_id, win = if_line_win(line)
            if win:
                return player_win_id, win
    return None, False


def if_line_win(line):
    """
    return: player_win_id, True/False (win/not win)
    """
    if None in line:
        return None, False

    if all(cell == line[0] for cell in line):
        return line[0], True
    else:
        return None, False


def print_field(field):
    lines = []
    header = f'{"*": ^5}'
    for i in range(len(field)):
        header += f'{i: ^5}'

    lines.append(header + '\n')
    
    
    for x, line in enumerate(field): 
        res_line = f'{x: ^5}'

        for cell in line:
            # print(f'Строка {line}: ячейка {cell}')
            res_line += f'{players[cell]["symbol"] if cell is not None else "-": ^5}'
        # print(f'Сформирована стркоа {res_line}')
        res_line += '\n'

        lines.append(res_line)

    for line in lines:
        print(line)



def __main__():
    field_size = [3, 3]

    size = input(f'Введите размер поля (3) ')
    if size == '':
        field_size = [3, 3]
    else:
        field_size = [int(size), int(size)]


    name_0 = None
    name_1 = None
    while not name_0 and not name_1:
        name_0 = input(f'Введите имя игрока за {players[0]["symbol"]}: ')
        players[0]["name"] = name_0

        name_1 = input(f'Введите имя игрока за {players[1]["symbol"]}: ')
        players[1]["name"] = name_1

    print('Начало игры...')
    field = [ [None for x_dimension in range(field_size[0])] for y_dimenstion in range(field_size[1]) ]

    won = False
    print_field(field)

    if random.random() > 0.5:
        playing_player = 0
        waiting_player = 1
    else:
        playing_player = 1
        waiting_player = 0

    while not no_free_space_left or not won:

        print(f'Ход игрока {players[playing_player]["name"]} ({players[playing_player]["symbol"]})')


        coords_correct = False

        while not coords_correct:
            coords = input('Введите координаты через пробел (X, Y): ')
            x = int(coords.split(' ')[0])
            y = int(coords.split(' ')[1])

            if field[x][y]:
                print('Данные координаты уже заняты! Выберите другие.')
                continue

            field[x][y] = playing_player
            coords_correct = True


        print_field(field)

        won, won_player_id = is_player_won(field)
        if won:
            print(f'{players[won_player_id]["name"]} победил!')
            return


        if no_free_space_left(field):
            print('Закончилось свободное место! Игра окончена. Ничья.')
            return

        temp = playing_player
        playing_player = waiting_player
        waiting_player = temp
    
    
__main__()
