from timeit import default_timer as timer

from input_helper import *


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def split_into_digits(number):
    return [int(a) for a in str(number)]


def print_debug(grid, steps):
    print("Grid after " + str(steps) + " steps.")
    for line in grid:
        print(str(line))


def reset_flashed(grid, amount):
    counter = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] > 9:
                counter += 1
                grid[row][col] = 0

    return counter >= amount


def flash(grid):
    flashes = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):

            to_visit = []
            to_visit.append(Point(row, col))

            while len(to_visit) > 0:
                point = to_visit[0]
                to_visit.remove(point)
                grid[point.x][point.y] += 1

                if grid[point.x][point.y] == 10:
                    flashes += 1
                    add_neighbours(grid, point.x, point.y, to_visit)

    return flashes


def add_neighbours(grid, row, col, to_visit):
    row_size = len(grid)
    col_size = len(grid[0])

    # # Add Neighbouring  Octopi
    # left
    if col > 0:
        to_visit.append(Point(row, col - 1))
    # right
    if col < col_size - 1:
        to_visit.append(Point(row, col + 1))
    # up
    if row > 0:
        to_visit.append(Point(row - 1, col))
    # low
    if row < row_size - 1:
        to_visit.append(Point(row + 1, col))

    # Top left
    if row > 0 and col > 0:
        to_visit.append(Point(row - 1, col - 1))
    # Top Right
    if col < col_size - 1 and row > 0:
        to_visit.append(Point(row - 1, col + 1))

    # Down left
    if col > 0 and row < row_size - 1:
        to_visit.append(Point(row + 1, col - 1))

    # Down Right
    if col < col_size - 1 and row < row_size - 1:
        to_visit.append(Point(row + 1, col + 1))

    return to_visit


def solve():
    input_list = read_input('input.txt')

    # Prepate grid
    grid = []
    for input in input_list:
        grid.append(split_into_digits(input))

    steps = 1000
    flashes = 0
    octopus_amount = len(grid) * len(grid[0])
    synch_step = 0

    for i in range(steps):
        flashes += flash(grid)
        synch = reset_flashed(grid, octopus_amount)
        if synch:
            synch_step = i + 1
            break

    print(f"Synchronized flash at {synch_step} ")


if __name__ == "__main__":
    start = timer()
    solve()
    end = timer()
    elapsed = round((end - start), 5)
    print("solved in {} seconds".format(elapsed))
