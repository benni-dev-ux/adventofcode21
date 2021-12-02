from timeit import default_timer as timer

from input_helper import *


def solve():
    input_list = read_input('input.txt')
    ## X and Z coordinates
    coord = [0, 0]

    for i in input_list:

        input = i.split()
        direction = input[0]
        value = int(input[1])

        if direction == "forward":
            coord[0] += value
        elif direction == "up":
            coord[1] -= value
        elif direction == "down":
            coord[1] += value

    print(coord)
    print(coord[0] * coord[1])


if __name__ == "__main__":
    start = timer()
    solve()
    end = timer()
    elapsed = round((end - start), 5)
    print("solved in {} seconds".format(elapsed))
