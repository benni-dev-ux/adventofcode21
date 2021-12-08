from timeit import default_timer as timer

from input_helper import *
import statistics


def calculate_lowest_fuel_consumption(input_list, median):
    fuel_cons = [0, 0, 0, 0, 0]
    ## Right value has to be next to the be round number at or next to median
    test_vals = [median - 2, median - 1, median, median + 1, median + 2]
    for idx, val in enumerate(test_vals):
        for input in input_list:
            fuel_cost = abs(input - val)
            fuel_cons[idx] += fuel_cost
    return min(fuel_cons)


def solve():
    input_list = read_input('input.txt')

    # Calculate mean as rounded int
    median = statistics.median(input_list)
    consumption = calculate_lowest_fuel_consumption(input_list, median)


    print(f"Lowest possible fuel consumption {consumption}")


if __name__ == "__main__":
    start = timer()
    solve()
    end = timer()
    elapsed = round((end - start), 5)
    print("solved in {} seconds".format(elapsed))
