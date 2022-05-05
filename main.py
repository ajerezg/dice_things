import random
import argparse

from tabulate import tabulate

from dice_classes import Dice, Poll, SuccessesPoll

REPEAT = 100000


def dice_roller_twilight_like(dice_str):
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
    extra = int(dice_str.split("d")[1].split("s")[1].split("e")[1])

    print("Dice sides: {}\tSuccess threshold: {}\tExtra success threshold: {}\tTimes rolled: {}".format(
        sides, success, extra, REPEAT))
    header = ["# dices", "1+ - ones", "2+ - ones", "3+ - ones", "4+ - ones", "5+ - ones", "6+ - ones",
              "7+ - ones", "8+ - ones", "9+ - ones", "10+ - ones"]
    results = []
    for dices in range(q_range[0], q_range[1]+1):
        successes_list = [0 for i in range(10)]
        ones_list = [0 for i in range(10)]
        poll = SuccessesPoll([], success, extra)
        for dice in range(1, dices+1):
            dice = Dice(sides)
            poll.add_dice(dice)
        for i in range(REPEAT):
            poll.roll()
            successes, ones = poll.successes(force=force)
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
    parser.add_argument('-roll', help="<dice-range>d<sides>s<success_threshold>e<extra_successes_threshold> -> 1-6d6s6e2")
    args = parser.parse_args()

    dice_roller_twilight_like(args.roll)
