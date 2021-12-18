from timeit import default_timer as timer

from input_helper import *


def solve():
    input = read_input('input.txt')

    # There is definitely a better way to handle this
    xinput = (str(input).split(" ")[2].strip("x=").strip(",").split(".."))
    y_input = (str(input).split(" ")[3]).strip("y=").strip("']").split("..")
    x_target = []
    y_target = []

    for t in xinput:
        x_target.append(int(t))

    for t in y_input:
        y_target.append(int(t))

    print(x_target)
    print(y_target)


if __name__ == "__main__":
    start = timer()
    solve()
    end = timer()
    elapsed = round((end - start), 5)
    print("solved in {} seconds".format(elapsed))
