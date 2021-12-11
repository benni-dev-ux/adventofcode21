from timeit import default_timer as timer

from input_helper import *


def solve():
    input_list = read_input('input.txt')

    increases = 0
    previous_sum = 0

    i = 1
    while i < (len(input_list) - 2):
        first = input_list[i]
        second = input_list[i + 1]
        third = input_list[i + 2]

        sum = first + second + third

        if sum > previous_sum:
            increases += 1
        previous_sum = sum
        i += 1

    print("Depth Increased " + str(increases) + " times")


if __name__ == "__main__":
    start = timer()
    solve()
    end = timer()
    elapsed = round((end - start), 5)
    print("solved in {} seconds".format(elapsed))
