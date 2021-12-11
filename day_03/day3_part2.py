from timeit import default_timer as timer

from input_helper import *


def solve():
    input_list = read_input('input.txt')
    input_seperated = []
    # split into digits
    for i in input_list:
        x = [int(a) for a in str(i)]
        input_seperated.append(x)
    input_seperated_copy = input_seperated.copy()
    oxygen_most_common = binary_most_common_column(input_seperated)
    oxygen_reduced = reduce_by_bit_criteria(input_seperated, oxygen_most_common)

    co2_most_common = invert_binary(binary_most_common_column(input_seperated_copy))
    co2_reduced = reduce_by_bit_criteria(input_seperated_copy, co2_most_common)

    ox_str = ''.join(map(str, oxygen_reduced[0]))
    co2_str = ''.join(map(str, co2_reduced[0]))

    print(ox_str)
    print(co2_str)

    solution = (int(ox_str, 2)) * (int(co2_str, 2))
    print(solution)


def reduce_by_bit_criteria(input, bit_criteria):
    # print(bit_criteria)

    input_copy = input.copy()
    for x in range(len(bit_criteria)):
        input_copy = input.copy()
        digit = bit_criteria[x]
        remove_counter = 0

        for element in input_copy:
            if element[x] != digit:
                if len(input) > 1:
                    input.remove(element)
                    remove_counter += 1

    return input


def binary_most_common_column(input):
    line_length = 12
    input_length = len(input)
    digit = 0
    output = ([])

    # Iterate over maximum number of digits in a line
    while digit < line_length:
        current_digit = ([])

        # Add each element to current digit array
        for element in input:
            current_digit.append(element[digit])

        ones = current_digit.count(1)
        # print(current_digit)
        # Check if 1 occurs more than half the time
        if ones >= (input_length / 2):
            output.append(1)
        else:
            output.append(0)

        digit += 1

    return output


def invert_binary(input):
    output = ([])
    for d in input:
        if d == 0:
            output.append(1)
        else:
            output.append(0)
    return output


if __name__ == "__main__":
    start = timer()
    solve()
    end = timer()
    elapsed = round((end - start), 5)
    print("solved in {} seconds".format(elapsed))
