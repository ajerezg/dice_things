import itertools
import random
import argparse

from tabulate import tabulate

from dice_classes import BestOfPool, Dice, Pool, SuccessesPool, TBAPool

REPEAT = 100000


def parse_dice_str(dice_str:str):
    # 1-4d6 -> ([1, 4], 6)
    quantity_range = [
        int(dice_str.split('-')[0]),
        int(dice_str.split('-')[1].split('d')[0]),
    ]
    dice_sides = int(dice_str.split('d')[1])
    return quantity_range, dice_sides

def set_pool(dice_quantity:int, dice_sides:int):
    pool = BestOfPool([])
    for index in range(1, dice_quantity+1):
        dice = Dice(dice_sides)
        pool.add_dice(dice)
    return pool

def roller(dice_str="1-4d6vs1-4d6"):
    attacker_str = dice_str.split("vs")[0]
    defender_str = dice_str.split("vs")[1]
    quantity_range_1, dice_sides_1 = parse_dice_str(attacker_str)
    quantity_range_2, dice_sides_2 = parse_dice_str(defender_str)
    
    print(f"Attacker: {attacker_str}\tDefender: {defender_str}")
    header = ["ATK vs DEF", "ATK WIN %"]
    results = []
    for atk_dice_quantity in range(quantity_range_1[0], quantity_range_1[1]+1):
        atk_pool = set_pool(atk_dice_quantity, dice_sides_1)
        for def_dice_quantity in range(quantity_range_2[0], quantity_range_2[1]+1):
            def_pool = set_pool(def_dice_quantity, dice_sides_2)
            atk_win_count = 0
            for i in range(REPEAT):
                atk_pool.roll()
                def_pool.roll()
                if atk_pool.get_result() > def_pool.get_result():
                    atk_win_count += 1
            atk_win_percentage = round(atk_win_count*100/REPEAT,1)
            results.append([
                f"{atk_dice_quantity}d{dice_sides_1}vs{def_dice_quantity}d{dice_sides_2}",
                f"{atk_win_percentage}%",
                ])
    print(tabulate(results, headers=header, tablefmt="tsv"))


if __name__ == "__main__":
    roller()
