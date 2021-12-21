from input_helper import *
from timeit import default_timer as timer


def solve():
    input_list = read_input('test_input.txt')
    p1_start = int(input_list[0].strip("Player 1 starting position: "))
    p2_start = int(input_list[1].strip("Player 2 starting position: "))



if __name__ == "__main__":
    start = timer()
    solve()
    end = timer()
    elapsed = round((end - start), 5)
    print("solved in {} seconds".format(elapsed))
