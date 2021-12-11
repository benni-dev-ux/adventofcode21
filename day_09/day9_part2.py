
from input_helper import *
from timeit import default_timer as timer


def solve():
    input_list = read_input('test_input.txt')
    print(input_list)


if __name__ == "__main__":
    start = timer()
    solve()
    end = timer()
    elapsed = round((end - start), 5)
    print("solved in {} seconds".format(elapsed))
