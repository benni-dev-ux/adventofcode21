from timeit import default_timer as timer

from input_helper import *


def solve():
    input_list = read_input('input.txt')
    input_seperated = []
    # split into digits
    for i in input_list:
        x = [int(a) for a in str(i)]
        input_seperated.append(x)

    gamma_rate = binary_most_common_column(input_seperated)
    gamma_str = ''.join(map(str, gamma_rate))
    epsilon_rate = invert_binary(gamma_rate)
    epsilon_str = ''.join(map(str, epsilon_rate))
    print(gamma_str)
    print(epsilon_str)

    # Cast do decimal and multiply
    solution = (int(gamma_str, 2)) * (int(epsilon_str, 2))
    print(solution)


def invert_binary(input):
    output = ([])
    for d in input:
        if d == 0:
            output.append(1)
        else:
            output.append(0)
    return output


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
        # Check if 1 occurs more than half the time
        if ones > (input_length / 2):
            output.append(1)
        else:
            output.append(0)

        digit += 1

    return output


if __name__ == "__main__":
    start = timer()
    solve()
    end = timer()
    elapsed = round((end - start), 5)
    print("solved in {} seconds".format(elapsed))
