from timeit import default_timer as timer

import numpy as np

from input_helper import *


def solve():
    input_list = read_input('input.txt')
    input_list

    fish_counter = np.zeros(9)
    print(input_list)
    days = 80
    for _ in range(days):
        for f in range(len(input_list)):
            if input_list[f] > 0:
                input_list[f] -= 1

            elif input_list[f] == 0:
                input_list[f] = 6
                input_list.append(8)

    print(f"Fish amount after {days} days: {len(input_list)}")


if __name__ == "__main__":
    start = timer()
    solve()
    end = timer()
    elapsed = round((end - start), 5)
    print("solved in {} seconds".format(elapsed))
