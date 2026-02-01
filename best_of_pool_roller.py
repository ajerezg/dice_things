import itertools
import random
import argparse

from tabulate import tabulate

from dice_classes import BestOfPool, Dice, Pool, SuccessesPool, TBAPool

REPEAT = 10000
BEST_OF = 3
ROLL_FUNC_NAMES = BestOfPool.get_func_names()
ROLL_FUNC_READABLE_NAMES = list(map(lambda x: "DEF_" + x, BestOfPool.get_func_readable_names()))
DICE_SKILL_SEPARATOR = "|"
DICE_SKILL_ALL = "all"

def parse_dice_str(dice_skill_str:str):
    # 1-4d6 -> ([1, 4], 6)
    skill_list = list(["standar"])
    dice_str = dice_skill_str
    if dice_skill_str.find(DICE_SKILL_SEPARATOR) != -1:
        dice_str = dice_skill_str.split(DICE_SKILL_SEPARATOR)[0]
        skill_str = dice_skill_str.split(DICE_SKILL_SEPARATOR)[1]
        if skill_str == DICE_SKILL_ALL:
            skill_list = BestOfPool.get_func_command_names()
        else:
            skill_list = skill_str.split(",")
    quantity_range = [
        int(dice_str.split('-')[0]),
        int(dice_str.split('-')[1].split('d')[0]),
    ]
    dice_sides = int(dice_str.split('d')[1])
    return quantity_range, dice_sides, skill_list

def set_pool(dice_quantity:int, dice_sides:int):
    pool = BestOfPool(list())
    for index in range(1, dice_quantity+1):
        dice = Dice(dice_sides)
        pool.add_dice(dice)
    return pool

def roller(dice_str=f"1-4d6|allvs1-4d6{DICE_SKILL_SEPARATOR}{DICE_SKILL_ALL}"):
    attacker_str = dice_str.split("vs")[0]
    defender_str = dice_str.split("vs")[1]
    quantity_range_1, dice_sides_1, skill_list_1 = parse_dice_str(attacker_str)
    quantity_range_2, dice_sides_2, skill_list_2 = parse_dice_str(defender_str)

    print(skill_list_1)
    print(skill_list_2)
    
    header = ["ATK vs DEF"]
    
    for skill_1 in skill_list_1:
        skill_str_1 = BestOfPool.get_func_readable_name_by_command(skill_1)
        for skill_2 in skill_list_2:
            skill_str_2 = BestOfPool.get_func_readable_name_by_command(skill_2)
            header.append(f"{skill_str_1}_vs_{skill_str_2}")
    vs_count = len(header) - 1 
    print(header)

    print(f"Attacker: {attacker_str}\tDefender: {defender_str}")
    results = []
    for atk_dice_quantity in range(quantity_range_1[0], quantity_range_1[1]+1):
        atk_pool = set_pool(atk_dice_quantity, dice_sides_1)
        for def_dice_quantity in range(quantity_range_2[0], quantity_range_2[1]+1):
            def_pool = set_pool(def_dice_quantity, dice_sides_2)
            atk_win_count_list = [0 for i in range(vs_count)]
            for i in range(REPEAT):
                atk_roll_win_count_list = [0 for i in range(vs_count)]
                for j in range(BEST_OF):
                    atk_pool.roll()
                    def_pool.roll()
                    vs_counter = 0
                    for func_command_1 in skill_list_1:
                        func_name_1 = BestOfPool.get_func_name_by_command(func_command_1)
                        func_result_1 = getattr(atk_pool, func_name_1)()
                        for func_command_2 in skill_list_2:
                            func_name_2 = BestOfPool.get_func_name_by_command(func_command_2)
                            func_result_2 = getattr(def_pool, func_name_2)()
                            if func_result_1 > func_result_2:
                                atk_roll_win_count_list[vs_counter] += 1
                            vs_counter += 1

                for index in range(vs_count):
                    if atk_roll_win_count_list[index] >= 2:
                        atk_win_count_list[index] += 1

            atk_win_percentage_list = [f"{round(win_count*100/REPEAT,2)}%" for win_count in atk_win_count_list]
            row_results = [f"{atk_dice_quantity}d{dice_sides_1}vs{def_dice_quantity}d{dice_sides_2}"] + atk_win_percentage_list
            results.append(row_results)
    print(tabulate(results, headers=header, tablefmt="tsv"))


if __name__ == "__main__":
    roller()
