from timeit import default_timer as timer

from input_helper import *


def split_into_digits(number):
    return [str(a) for a in str(number)]


def solve():
    input_list = read_input('test_input.txt')

    # Data Prep
    polymer = split_into_digits((input_list[0]))
    insertion_values = []
    insertion_keys = []
    for i in range(2, len(input_list)):
        pair = (input_list[i].split(" -> "))
        insertion_keys.append(pair[0])
        insertion_values.append(pair[1])

    
    print(insertion_values)


if __name__ == "__main__":
    start = timer()
    solve()
    end = timer()
    elapsed = round((end - start), 5)
    print("solved in {} seconds".format(elapsed))
