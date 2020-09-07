Some classes to use as dice rollers.
Main use: `python main.py -roll 1-10d8s6e2`
- 1-10d8: roll 1 to 10 die of 8 sides.
- s6: success threshold of 6+
- e2: count 1 success more for each +2 over success threshold
Result for previous example:
```
Dice sides: 8   Success threshold: 6    Extra success threshold: 2      Times rolled: 100000
|   # dices |   1+ successes |   2+ successes |   3+ successes |   4+ successes |   5+ successes |
|-----------+----------------+----------------+----------------+----------------+----------------|
|         1 |         37.531 |         12.67  |          0     |          0     |          0     |
|         2 |         61.2   |         29.895 |          7.752 |          1.577 |          0     |
|         3 |         75.386 |         46.245 |         20.067 |          6.675 |          1.348 |
|         4 |         84.8   |         60.434 |         33.33  |         14.917 |          4.985 |
|         5 |         90.464 |         71.497 |         46.698 |         25.097 |         10.92  |
|         6 |         93.864 |         79.609 |         58.132 |         36.116 |         18.769 |
|         7 |         96.167 |         85.807 |         68.255 |         47.447 |         28.15  |
|         8 |         97.726 |         90.241 |         76.008 |         57.463 |         38.02  |
|         9 |         98.56  |         93.395 |         82.479 |         66.405 |         47.611 |
|        10 |         99.096 |         95.501 |         87.268 |         73.96  |         56.851 |
```