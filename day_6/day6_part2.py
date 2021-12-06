from timeit import default_timer as timer

import numpy as np

from input_helper import *


def initialize_fish_counter(input_list):
    counter = np.zeros(9)
    for f in input_list:
        counter[f] += 1
    return counter


def solve():
    input_list = read_input('input.txt')

    fish_counter = initialize_fish_counter(input_list)
    days = 256

    for _ in range(days):
        fish_at_timer_zero = fish_counter[0]
        for d in range((len(fish_counter))):
            if d < 8:
                fish_counter[d] = fish_counter[d + 1]

        fish_counter[6] += fish_at_timer_zero
        fish_counter[8] = fish_at_timer_zero

    print(f"Fish amount after {days} days: {np.sum(fish_counter)}")


if __name__ == "__main__":
    start = timer()
    solve()
    end = timer()
    elapsed = round((end - start), 5)
    print("solved in {} seconds".format(elapsed))
