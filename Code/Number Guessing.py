# Import dependencies
import random as rnd


def randomize(range_):
    range_list = list(range(range_))
    return rnd.choice(range_list)


class Validator:
    def __init__(self, validator):
        self.validator = validator

    def equal(self, item):
        if item == self.validator:
            return True
        else:
            return False

    def greater(self, item):
        if item > self.validator:
            return True
        else:
            return False


# Chose a random number
rnd_number = Validator(randomize(10))
guess = 5


if rnd_number.equal(guess):
    print('Correct')
elif rnd_number.greater(guess):
    print('Greater Than')
else:
    print('Less Than')
