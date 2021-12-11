from timeit import default_timer as timer

from input_helper import *


def update_board(board, bingo_number):
    for i, line in enumerate(board):
        for j, (board_value, _) in enumerate(line):
            if board_value == bingo_number:
                board[i][j] = bingo_number, True


def horizontal_match(board):
    for line in board:
        for i, (_, marked) in enumerate(line):
            if not marked:
                break
            if i == 4:
                return True
    return False


def vertical_match(board):
    board_length = 5
    for column in range(board_length):
        for row in range(board_length):
            _, match = board[row][column]
            if not match:
                break
            if row == 4:
                return True

    return False


def check_for_win(board):
    return horizontal_match(board) or vertical_match(board)


def get_unmarked_sum(board):
    total = 0
    for line in board:
        for cell in line:
            if not cell[1]:
                total += cell[0]
    return total





def solve():
    bingo_numbers, bingo_boards = read_bingo_input('test_input.txt')
    for number in bingo_numbers:
        boards_remaining = []
        for board in bingo_boards:
            update_board(board, number)
            winner_found = check_for_win(board)
            if not winner_found:
                boards_remaining.append(board)

        if len(boards_remaining) == 0:
            final_board = bingo_boards[len(bingo_boards) - 1]
            unmarked = get_unmarked_sum(final_board)
            print(f"final value: {number}, unmarked total: {unmarked}, product: {number * unmarked}")
            return


if __name__ == "__main__":
    start = timer()
    solve()
    end = timer()
    elapsed = round((end - start), 5)
    print("solved in {} seconds".format(elapsed))
