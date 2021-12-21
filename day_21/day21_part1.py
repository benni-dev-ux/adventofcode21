from timeit import default_timer as timer

from input_helper import *


def roll(position, dice, dice_rolls):
    for i in range(3):
        dice += 1
        if dice == 100 + 1:
            dice = 1
        position += dice

        # TIL You can do this in python
        position = position % 10 or 10

    return position, dice, dice_rolls + 3


def solve():
    input_list = read_input('input.txt')
    p1_pos = int(input_list[0].split(" ")[-1])
    p2_pos = int(input_list[1].split(" ")[-1])

    p1_score = 0
    p2_score = 0

    dice = 0
    dice_rolls = 0

    while True:

        p1_pos, dice, dice_rolls = roll(p1_pos, dice, dice_rolls)
        p1_score += p1_pos
        # print(f"P1  rolling {dice - 2} {dice - 1} {dice} to {p1_pos} for {p1_score}")

        if p1_score >= 1000:
            print(f"P1 {p1_score} P2 {p2_score}")
            print(f"Dice Rolled * P2 =   {p2_score * dice_rolls}")

            break

        p2_pos, dice, dice_rolls = roll(p2_pos, dice, dice_rolls)
        p2_score += p2_pos
        # print(f"P2  rolling {dice - 2} {dice - 1} {dice} to {p2_pos} for {p2_score}")

        if p2_score >= 1000:
            print(f"P1 {p1_score} P2 {p2_score}")
            print(f"Dice Rolled * P1 =   {p1_score * dice_rolls}")

            break


if __name__ == "__main__":
    start = timer()
    solve()
    end = timer()
    elapsed = round((end - start), 5)
    print("solved in {} seconds".format(elapsed))
