import statistics
from timeit import default_timer as timer

from input_helper import *
from tqdm import tqdm


def calculate_lowest_fuel_consumption(input_list, median):
    ## Right value has to be next to the be round number at or next to median
    test_vals = range(min(input_list), max(input_list))
    fuel_cons = [0] * len(test_vals)
    for idx, val in tqdm(enumerate(test_vals)):
        for input in input_list:
            steps = int(abs(input - val))
            cost = 0
            for i in range(steps + 1):
                cost += i

            fuel_cons[idx] += cost
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
