from input_helper import *


def solve():
    input_list = read_input('input.txt')

    increases = 0

    i = 0
    while i < (len(input_list) - 1):

        previous_element = input_list[i]
        next_element = input_list[i+1]

        # print("From %d to %d ", previous_element, next_element)

        if previous_element < next_element:
            increases += 1

        i += 1

    print("Depth Increased "+str(increases)+" times")


if __name__ == "__main__":
    solve()
