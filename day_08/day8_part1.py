from timeit import default_timer as timer

from input_helper import *


def solve():
    input_list = read_input('input.txt')
    unique_numbers = 0
    for input in input_list:
        # Get only output as list
        output = input.split("|")[1].split(" ")
        for o in output:
            # print(str(o)+" "+str(len(o)))
            # only finding characters with distinct length
            if len(o) == 2 or len(o) == 3 or len(o) == 4 or len(o) == 7:
                unique_numbers += 1

    print(unique_numbers)


if __name__ == "__main__":
    start = timer()
    solve()
    end = timer()
    elapsed = round((end - start), 5)
    print("solved in {} seconds".format(elapsed))
