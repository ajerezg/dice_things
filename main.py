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
    sides = int(dice_str.split("d")[1].split("s")[0])
    success = int(dice_str.split("d")[1].split("s")[1].split("e")[0])
    extra = int(dice_str.split("d")[1].split("s")[1].split("e")[1])
    print("Dice sides: {}\tSuccess threshold: {}\tExtra success threshold: {}\tTimes rolled: {}".format(
        sides, success, extra, REPEAT))
    header = ["# dices", "1+ successes", "2+ successes", "3+ successes", "4+ successes", "5+ successes"]
    results = []
    for dices in range(q_range[0], q_range[1]+1):
        successes_list = [0 for i in range(5)]
        poll = SuccessesPoll([], success, extra)
        for dice in range(1, dices+1):
            dice = Dice(sides)
            poll.add_dice(dice)
        for i in range(REPEAT):
            poll.roll()
            successes = poll.successes()
            for s in range(1, 6):
                if successes >= s:
                    successes_list[s-1] += 1
        successes_list_percentage = list(map(lambda x: x*100/REPEAT, successes_list))
        successes_list_percentage.insert(0, dices)
        results.append(successes_list_percentage)
    print(tabulate(results, headers=header, tablefmt="orgtbl"))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate percentage of successes for dice rolled")
    parser.add_argument('-roll', help="<dice-range>d<sides>s<success_threshold>e<extra_successes_threshold> -> 1-6d6s6e2")
    args = parser.parse_args()

    dice_roller_twilight_like(args.roll)
