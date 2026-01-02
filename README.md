Some classes to use as dice rollers.



## General Success Roller general_success_roller
This command rolls a general version of the success system rolling pools of the same side dice.

Main use: `python general_success_roller.py -roll 1-10d6s4e2f`
- 1-10d6: roll 1 to 10 die of 6 sides.
- s4: success threshold of 4+
- e2: count 1 success more for each +2 over success threshold
- f: if its present, the dice other than successes and 1s will be rerolled.

Result for previous example:
```
Dice sides: 6   Success threshold: 4    Extra success threshold: 2      Times rolled: 100000
|   # dices | 1+ - ones     | 2+ - ones     | 3+ - ones     | 4+ - ones     | 5+ - ones     | 6+ - ones     | 7+ - ones     | 8+ - ones     | 9+ - ones     | 10+ - ones    |
|-----------+---------------+---------------+---------------+---------------+---------------+---------------+---------------+---------------+---------------+---------------|
|         1 | 66.67% - 0.22 | 22.27% - 0.22 | 0.0% - 0.22   | 0.0% - 0.22   | 0.0% - 0.22   | 0.0% - 0.22   | 0.0% - 0.22   | 0.0% - 0.22   | 0.0% - 0.22   | 0.0% - 0.22   |
|         2 | 88.74% - 0.44 | 59.17% - 0.44 | 24.69% - 0.44 | 4.88% - 0.44  | 0.0% - 0.44   | 0.0% - 0.44   | 0.0% - 0.44   | 0.0% - 0.44   | 0.0% - 0.44   | 0.0% - 0.44   |
|         3 | 96.19% - 0.67 | 81.33% - 0.67 | 54.37% - 0.67 | 25.68% - 0.67 | 7.68% - 0.67  | 1.07% - 0.67  | 0.0% - 0.67   | 0.0% - 0.67   | 0.0% - 0.67   | 0.0% - 0.67   |
|         4 | 98.79% - 0.89 | 92.26% - 0.89 | 75.76% - 0.89 | 50.74% - 0.89 | 26.02% - 0.89 | 9.58% - 0.89  | 2.23% - 0.89  | 0.24% - 0.89  | 0.0% - 0.89   | 0.0% - 0.89   |
|         5 | 99.61% - 1.11 | 96.98% - 1.11 | 88.41% - 1.11 | 71.26% - 1.11 | 48.38% - 1.11 | 26.24% - 1.11 | 10.85% - 1.11 | 3.23% - 1.11  | 0.59% - 1.11  | 0.06% - 1.11  |
|         6 | 99.86% - 1.33 | 98.77% - 1.33 | 94.65% - 1.33 | 84.49% - 1.33 | 67.49% - 1.33 | 46.09% - 1.33 | 26.07% - 1.33 | 11.71% - 1.33 | 4.01% - 1.33  | 0.98% - 1.33  |
|         7 | 99.95% - 1.56 | 99.49% - 1.56 | 97.52% - 1.56 | 91.93% - 1.56 | 80.84% - 1.56 | 63.58% - 1.56 | 43.62% - 1.56 | 25.46% - 1.56 | 12.22% - 1.56 | 4.65% - 1.56  |
|         8 | 99.99% - 1.78 | 99.83% - 1.78 | 99.05% - 1.78 | 96.33% - 1.78 | 89.77% - 1.78 | 77.86% - 1.78 | 61.09% - 1.78 | 42.24% - 1.78 | 25.3% - 1.78  | 12.69% - 1.78 |
|         9 | 100.0% - 2.0  | 99.93% - 2.0  | 99.6% - 2.0   | 98.24% - 2.0  | 94.59% - 2.0  | 87.03% - 2.0  | 74.88% - 2.0  | 58.38% - 2.0  | 40.78% - 2.0  | 24.95% - 2.0  |
|        10 | 100.0% - 2.22 | 99.97% - 2.22 | 99.83% - 2.22 | 99.2% - 2.22  | 97.37% - 2.22 | 92.9% - 2.22  | 84.69% - 2.22 | 72.18% - 2.22 | 56.35% - 2.22 | 39.55% - 2.22 |

```


## TBA roller tba_roller
This command rolls a dice system like the twilight 2000 but different...

Main use: `python tba_roller.py -roll all`

## Best of Pool roller best_of_pool_roller
This command is an opposed roll of an attacker and a defender, with each one choosing the highest number rolled. Defense wins draws.
The results shows the best of three win percentage of the attacker vs the defender with different "skills":

- WIN%_vs_DEF_: Normal roll for the defense.
- ODD+1: +1 to the dice with odd values.

Main use: `python best_of_pool_roller.py`

Result for previous example:
```
Attacker: 1-4d6 Defender: 1-4d6
ATK vs DEF      WIN%_vs_DEF_    WIN%_vs_DEF_ODD+1
1d6vs1d6        37.7%           26.0%
1d6vs2d6        16.2%           9.1%
1d6vs3d6        8.1%            3.5%
1d6vs4d6        4.3%            1.4%
2d6vs1d6        61.7%           47.2%
2d6vs2d6        33.9%           19.6%
2d6vs3d6        19.3%           8.3%
2d6vs4d6        11.4%           3.6%
3d6vs1d6        73.1%           58.4%
3d6vs2d6        46.0%           27.2%
3d6vs3d6        28.7%           12.2%
3d6vs4d6        18.1%           5.5%
4d6vs1d6        79.3%           64.3%
4d6vs2d6        54.0%           32.0%
4d6vs3d6        35.8%           15.1%
4d6vs4d6        23.4%           7.0%
```
