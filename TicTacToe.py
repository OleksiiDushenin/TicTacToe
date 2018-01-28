def play():
    board = create_board()
    player = 'One'
    while True:
        if make_action(board, player):
            print_board(board)
            return
        player = switch_player(player)


def make_action(board, player):
    print_board(board)
    print()
    print('Player {}! It is your turn.'.format(player))

    while True:
        row = read_position('Insert row > ')
        column = read_position('Insert column > ')
        row_position = int(row) - 1
        column_position = int(column) - 1

        if validate_availability(row_position, column_position, board):
            board[row_position][column_position] = get_player_mark(player)
            return is_final(board, player, row_position, column_position)


def is_final(board, player, row_position, column_position):
    mark = get_player_mark(player)
    if is_final_rows(board, row_position, mark):
        print('Player {} won!'.format(player))
        return True

    if is_final_columns(board, column_position, mark):
        print('Player {} won!'.format(player))
        return True

    if is_final_diagonals(board, row_position, column_position, mark):
        print('Player {} won!'.format(player))
        return True

    if is_final_draw(board):
        print('It is a draw!')
        return True

    return False


def is_final_draw(board):
    for row in board:
        for mark in row:
            if mark == ' ':
                return False

    return True


def is_final_rows(board, row_position, mark):
    row_marks = [x for x in board[row_position] if x == mark]
    if len(row_marks) == 3:
        return True
    else:
        return False


def is_final_columns(board, column_position, mark):
    column_marks = [x for x in range(0, 3) if board[x][column_position] == mark]
    if len(column_marks) == 3:
        return True
    else:
        return False


def is_final_diagonals(board, row_position, column_position, mark):
    if (column_position + row_position) % 2 != 0:
        return False

    diagonal_check = True
    inverse_diagonal_check = True

    for i in range(0, 3):
        if board[i][i] != mark:
            diagonal_check = False
        if board[i][2 - i] != mark:
            inverse_diagonal_check = False

    return diagonal_check or inverse_diagonal_check


def get_player_mark(player):
    if player == 'One':
        return 'X'
    else:
        return 'O'


def switch_player(player):
    if player == 'One':
        return 'Two'
    else:
        return 'One'


def read_position(message):
    while True:
        position = input(message)
        if validate(position):
            return position


def validate_availability(row, column, board):
    if board[row][column] != ' ':
        print('Position {} - {} is unavailable.'.format(row + 1, column + 1))
        return False
    else:
        return True


def validate(position):
    if not position.isnumeric() or int(position) < 1 or int(position) > 3:
        print('Invalid position. Must be between 1 and 3')
        return False
    return True


def print_board(board):
    print()
    row_number = 0
    for row in board:
        print_board_row(row, row_number)
        row_number += 1


def print_board_row(row, row_number):
    print('   |   |   ')
    print(' {} | {} | {} '.format(row[0], row[1], row[2]))
    if row_number != 2:
        print('___|___|___')
    else:
        print('   |   |   ')


def create_board():
    return [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]


if __name__ == "__main__":
    play()
