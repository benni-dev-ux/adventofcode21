from timeit import default_timer as timer

import numpy as np

from input_helper import *


def resolve_vent_lines(arr, grid):
    # create empry arr with the shape of input arr
    for line in arr:
        ho_diff = line[0] - line[2]
        ve_diff = line[1] - line[3]

        if ho_diff != 0:
            start = (line[0])
            end = (line[2])

            if (start < end):
                temp = start
                start = end
                end = temp
                ho_diff *= -1
            for i in range(ho_diff + 1):
                grid[line[1], start - i] += 1

        if ve_diff != 0:
            start = (line[1])
            end = (line[3])

            if (start < end):
                temp = start
                start = end
                end = temp
                ve_diff *= -1
            for i in range(ve_diff + 1):
                grid[start - i, line[0]] += 1
    return grid


def count_crossings(grid):
    ans = 0
    for count in grid.flatten():
        ans += count >= 2
    return ans


def solve():
    input_list = read_input('input.txt')
    arr = (np.array(input_list).astype(int))

    # Find the boundaries of the grid
    col_0 = np.max(arr[:, 0])
    col_1 = np.max(arr[:, 1])
    col_2 = np.max(arr[:, 2])
    col_3 = np.max(arr[:, 3])

    max_x =col_0
    if col_2>max_x:
        max_x = col_2

    max_y = col_1
    if col_3 > max_y:
        max_y = col_3

    print(max_x)
    print(max_y)



    grid = np.zeros((max_x+1, max_y+1))


    # only keep vertical and horizontal lines
    # probably not the most efficient way to do this in numpy
    horizontal_lines = arr[arr[:, 0] == arr[:, 2]]
    vertical_lines = arr[arr[:, 1] == arr[:, 3]]
    arr = np.append(horizontal_lines, vertical_lines, axis=0)
    # draw lines
    grid = resolve_vent_lines(arr, grid)
    print(grid)
    crossings = count_crossings(grid)
    print(crossings)


if __name__ == "__main__":
    start = timer()
    solve()
    end = timer()
    elapsed = round((end - start), 5)
    print("solved in {} seconds".format(elapsed))
