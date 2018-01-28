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
    return [[' '] * 3] * 3


if __name__ == "__main__":
    print_board(create_board())

