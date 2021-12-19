from timeit import default_timer as timer

from tqdm import tqdm

from input_helper import *


def shoot_probe(x_vel, y_vel, x_target, y_target):
    max_y = -99999999999
    x = 0
    y = 0
    pastTarget = False

    while not pastTarget:

        x += x_vel
        y += y_vel
        if y > max_y:
            max_y = y

        if x_target[0] <= x <= x_target[1] and y_target[0] <= y <= y_target[1]:
            return int(max_y)
        elif y_target[0] > y:
            pastTarget = True

        if x_vel > 0:
            x_vel += 1
        elif x_vel < 0:
            x_vel -= 1

        y_vel -= 1

    return -99999999999


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

    max_height = -99999999999
    brute_force_target = 500

    for y in tqdm(range(y_target[0], brute_force_target)):
        for x in range(1, x_target[1] + 1):

            height = shoot_probe(x, y, x_target, y_target)

            if height > max_height:
                print("Setting new height")
                max_height = height
                print(max_height)

    print(max_height)



if __name__ == "__main__":
    start = timer()
    solve()
    end = timer()
    elapsed = round((end - start), 5)
    print("solved in {} seconds".format(elapsed))
