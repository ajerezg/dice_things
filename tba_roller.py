import itertools
import random
import argparse

from tabulate import tabulate

from dice_classes import Dice, Poll, SuccessesPoll, TBAPoll

REPEAT = 100000

RANK_LIST = "0EDCBA"
RANK_SIDE_DICT = {"0": 0, "E": 4, "D": 6, "C": 8, "B": 10, "A": 12}

MASTER_LIST = ["E0", "EE", "ED", "EC", "EB", "EA", "D0", "DD", "DC", "DB", "DA", "C0", "CC", "CB", "CA", "B0", "BB", "BA", "A0", "AA"]

def tba_roller(dice_str):
    explode = False
    if "e" == dice_str[-1]:
        explode = True
        dice_str = dice_str[:-1]

    """rank_start1 = dice_str[0]
    rank_start2 = dice_str[1]
    rank_end1 = dice_str[3]
    rank_end2 = dice_str[4]"""

    print(f"Rank list: {dice_str}, Explode: {explode}, Times rolled: {REPEAT}")
    header = ["Ranks", "AVG", "1+ - ones", "2+ - ones", "3+ - ones", "4+ - ones", "5+ - ones", "6+ - ones",
              "7+ - ones", "8+ - ones", "9+ - ones", "10+ - ones", "11+ - ones", "12+ - ones"]
    results = []

    all_rank_pairs = itertools.permutations(RANK_LIST, 2)

    results_for_order = dict()

    for pair in MASTER_LIST:
        result_list = [0 for i in range(12)]
        ones_list = [0 for i in range(12)]
        results_for_avg = list()
        poll = TBAPoll([Dice(RANK_SIDE_DICT[pair[0]]), Dice(RANK_SIDE_DICT[pair[1]])])
        for i in range(REPEAT):
            successes, ones = poll.roll()
            results_for_avg.append(successes)
            for s in range(1, 13):
                if successes >= s:
                    result_list[s-1] += 1
                ones_list[s-1] += ones
        successes_list_percentage = list(map(lambda x, y: f"{round(x*100/REPEAT, 2)}% - {round(y/REPEAT, 2)}",
                                             result_list, ones_list))
        successes_list_percentage.insert(0, pair)
        key = sum(results_for_avg)/len(results_for_avg)
        successes_list_percentage.insert(1, key)
        results_for_order[key] = successes_list_percentage

    keys = results_for_order.keys()
    keys = sorted(keys)

    for key in keys:
        results.append(results_for_order[key])

    print(tabulate(results, headers=header, tablefmt="orgtbl"))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate percentage of successes for dice rolled")
    parser.add_argument('-roll', help="<dice-rank-start1><dice-rank-start2>-<dice-rank-end1><dice-rank-end1> -> E0-AA")
    args = parser.parse_args()

    tba_roller(args.roll)
