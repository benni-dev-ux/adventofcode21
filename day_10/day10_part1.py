from timeit import default_timer as timer

from input_helper import *


def solve():
    input_list = read_input('input.txt')

    score = 0

    for input in input_list:
        # print(len(input_list))
        stack = []
        for idx, digit in enumerate(input):
            exit = False
            match digit:
                case "(":
                    stack.append(digit)

                case "[":
                    stack.append(digit)

                case "{":
                    stack.append(digit)

                case "<":
                    stack.append(digit)

                case ")":
                    obj = stack[-1]
                    if obj != '(':
                        print("expected ( at " + str(idx) + " in line " + str(input))
                        score += 3
                        exit = True
                    del stack[-1]

                case "]":
                    obj = stack[-1]
                    if obj != '[':
                        print("expected [ at " + str(idx) + " in line " + str(input))
                        score += 57
                        exit = True
                    del stack[-1]

                case "}":
                    obj = stack[-1]
                    if obj != '{':
                        print("expected { at " + str(idx) + " in line " + str(input))
                        score += 1197
                        exit = True
                    del stack[-1]

                case ">":
                    obj = stack[-1]
                    if obj != '<':
                        print("expected < at " + str(idx) + " in line " + str(input))
                        score += 25137
                        exit = True
                    del stack[-1]

            if exit:
                input_list.remove(input)
                break
    print(score)


if __name__ == "__main__":
    start = timer()
    solve()
    end = timer()
    elapsed = round((end - start), 5)
    print("solved in {} seconds".format(elapsed))
