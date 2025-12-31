import random
import argparse

from tabulate import tabulate

from dice_classes import Dice, Pool, SuccessesPool, SuccessesPool2

REPEAT = 100000


def general_success_dice_roller(dice_str):
    quantity = dice_str.split("d")[0]
    q_range = []
    if '-' in quantity:
        q1 = int(quantity.split("-")[0])
        q2 = int(quantity.split("-")[1])
        q_range = [q1, q2]
    else:
        raise ValueError()
    force = True if dice_str[-1] == "f" else False
    if force:
        dice_str = dice_str[:-1]
    sides = int(dice_str.split("d")[1].split("s")[0])
    success = int(dice_str.split("d")[1].split("s")[1].split("e")[0])

    print(f"Dice sides: {sides}\tSuccess threshold: {success}\tTimes rolled: {REPEAT}")
    header = ["# dices", "1+ - failures", "2+ - failures", "3+ - failures", "4+ - failures", "5+ - failures", "6+ - failures",
              "7+ - failures", "8+ - failures", "9+ - failures", "10+ - failures"]
    results = []
    for dices in range(q_range[0], q_range[1]+1):
        successes_list = [0 for i in range(10)]
        ones_list = [0 for i in range(10)]
        pool = SuccessesPool2([], success)
        for dice in range(1, dices+1):
            dice = Dice(sides)
            pool.add_dice(dice)
        for i in range(REPEAT):
            pool.roll()
            successes, ones = pool.successes(force=force)
            for s in range(1, 11):
                if successes >= s:
                    successes_list[s-1] += 1
                ones_list[s-1] += ones
        successes_list_percentage = list(map(lambda x, y: f"{round(x*100/REPEAT, 2)}% - {round(y/REPEAT, 2)}",
                                             successes_list, ones_list))
        successes_list_percentage.insert(0, dices)
        results.append(successes_list_percentage)
    print(tabulate(results, headers=header, tablefmt="orgtbl"))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate percentage of successes for dice rolled")
    parser.add_argument('-roll', help="<dice-range>d<sides>s<success_threshold><f> -> 1-6d6s6 or 1-6d6s6f")
    args = parser.parse_args()

    general_success_dice_roller(args.roll)
