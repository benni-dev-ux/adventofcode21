from timeit import default_timer as timer

from input_helper import *


def solve():
    input_list = read_input('test_input.txt')

    score = 0

    for input in input_list:
        queue = []

        for digit in input:
            exit = False
            illegeal_char = ""
            expected_char = ""

            # Add to queue if opening bracket
            if digit == "(" or digit == "[" or digit == "{" or digit == "<":
                queue.append(digit)



            elif digit == ")":
                if queue[len(queue) - 1] != "(":
                    print("found " + digit + " comparing to " + queue[len(queue) - 1])

                    del queue[len(queue) - 1]

                    score += 3
                    exit = True
                #
            elif digit == "]":
                if queue[len(queue) - 1] != "[":
                    print("found " + digit + " comparing to " + queue[len(queue) - 1])

                    del queue[len(queue) - 1]

                    score += 57
                    exit = True
            elif digit == "}":
                if queue[len(queue) - 1] != "{":
                    print("found " + digit + " comparing to " + queue[len(queue) - 1])

                    del queue[len(queue) - 1]

                    score += 1197
                    exit = True
            elif digit == ">":
                if queue[len(queue) - 1] != "<":
                    print("found " + digit + " comparing to " + queue[len(queue) - 1])

                    del queue[len(queue) - 1]

                    score += 25137
                    exit = True


            print(queue)
            if exit:
                break

    print(score)


if __name__ == "__main__":
    start = timer()
    solve()
    end = timer()
    elapsed = round((end - start), 5)
    print("solved in {} seconds".format(elapsed))
