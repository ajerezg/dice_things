import random


class Dice:
    def __init__(self, sides=6):
        self.sides = sides
        self.result = None

    def roll(self):
        if self.sides == 0:
            self.result = 0
        else:
            self.result = random.randint(1, self.sides)
        return self.result

    def reset_roll(self):
        self.result = None


class Pool:
    def __init__(self, dices_list=[]):
        self.pool = dices_list

    def roll(self):
        for dice in self.pool:
            dice.roll()
        return self.pool

    def reset_roll(self):
        for dice in self.pool:
            dice.reset_roll()

    def add_dice(self, dice):
        self.pool.append(dice)


class TBAPool(Pool):
    def roll(self):
        super(TBAPool, self).roll()
        max = 0
        ones = 0
        for dice in self.pool:
            if dice.result > max :
                max = dice.result
            if dice.result == 1:
                ones += 1
        return max, ones


class SuccessesPool(Pool):
    def __init__(self, dices_list=[], success_threshold=6, extra_success_threshold=0):
        self.success_threshold = success_threshold
        self.extra_success_threshold = extra_success_threshold
        super(SuccessesPool, self).__init__(dices_list)

    def _check_die_successes(self, dice: Dice):
        successes = 0
        if dice.result >= self.success_threshold:
            successes += 1
            if self.extra_success_threshold:
                new_success_threshold = self.success_threshold + self.extra_success_threshold
                while new_success_threshold <= dice.sides:
                    if dice.result >= new_success_threshold:
                        successes += 1
                    new_success_threshold += self.extra_success_threshold
        return successes

    def successes(self, force=False):
        successes = 0
        ones = 0
        for dice in self.pool:
            successes += self._check_die_successes(dice)
            if force and 1 < dice.result < self.success_threshold:
                dice.roll()
                successes += self._check_die_successes(dice)
            if 1 == dice.result:
                ones += 1
        return successes, ones


class SuccessesPool2(SuccessesPool):
    def successes(self, force=False):
        successes = 0
        failures = 0
        for dice in self.pool:
            successes += self._check_die_successes(dice)
            if force and dice.result < self.success_threshold:
                dice.roll()
                successes += self._check_die_successes(dice)
            if dice.result < self.success_threshold:
                failures += 1
        return successes, failures

