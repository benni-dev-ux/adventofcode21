from timeit import default_timer as timer

from input_helper import *
import numpy as np


def solve():
    input_list = read_input('test_input.txt')

    score = 0

    for input in input_list:
        queue = []
        char_counter = [0, 0, 0, 0]
        for digit in input:
            print(digit)

            match digit:
                case"(":
                    char_counter[0] += 1
                case"[":
                    char_counter[1] += 1
                case"{":
                    char_counter[2] += 1
                case"<":
                    char_counter[3] += 1
                case")":
                    char_counter[0] -= 1
                    if char_counter[0] < 0:
                        print("found ) ")
                        score += 3
                        # break
                case"]":
                    char_counter[1] -= 1
                    if char_counter[1] <= 0:
                        print("found ] ")
                        score += 57
                       # break
                case"}":
                    char_counter[2] -= 1
                    if char_counter[2] <= 0:
                        print("found} ")
                        score += 1197
                       # break
                case">":
                    char_counter[3] -= 1
                    if char_counter[3] <= 0:
                        print("found> ")
                        score += 25137
                       # break

    print(score)


if __name__ == "__main__":
    start = timer()
    solve()
    end = timer()
    elapsed = round((end - start), 5)
    print("solved in {} seconds".format(elapsed))
