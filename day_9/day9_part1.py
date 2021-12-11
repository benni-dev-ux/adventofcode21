from timeit import default_timer as timer

from input_helper import *


def split_number_into_digits(number):
    return [int(a) for a in str(number)]


def check_neighbours(grid, num, row_idx, num_idx, col_size, row_size):
    # set to 9 if at edge
    upper = 9
    lower = 9
    left = 9
    right = 9
    if num_idx > 0:
        left = grid[row_idx][num_idx - 1]
    if num_idx < col_size - 1:
        right = grid[row_idx][num_idx + 1]
    if row_idx > 0:
        upper = grid[row_idx - 1][num_idx]
    if row_idx < row_size - 1:
        lower = grid[row_idx + 1][num_idx]

    return left > num and right > num and upper > num and lower > num

    # print("num " + str(num) + " up " + str(upper) + "low " + str(lower))


def solve():
    input_list = read_input('input.txt')
    # Prepare Input as 2-Dimensional list
    grid = []
    for input in input_list:
        grid.append(split_number_into_digits(input))

    col_size = len(grid[0])
    row_size = len(grid)

    risk_sum = 0

    # Traverse grid
    for row_idx, row in enumerate(grid):
        for num_idx, num in enumerate(grid[row_idx]):
            if check_neighbours(grid, num, row_idx, num_idx, col_size, row_size):
                risk_sum = risk_sum + 1 + num

    print(f"risk sum {risk_sum}")


if __name__ == "__main__":
    start = timer()
    solve()
    end = timer()
    elapsed = round((end - start), 5)
    print("solved in {} seconds".format(elapsed))
