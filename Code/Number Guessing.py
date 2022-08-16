# Import dependencies
import random as rnd


def randomize(range_):
    range_list = list(range(range_))
    return rnd.choice(range_list)


class Validator:
    def __init__(self, validator):
        self.validator = validator

    def equal(self, item: int) -> bool:
        if item == self.validator:
            return True
        else:
            return False

    def greater(self, item: int) -> bool:
        if item > self.validator:
            return True
        else:
            return False


# Chose a random number
rnd_number = Validator(randomize(10))
guess_limiter = 0

while True:
    guess_limiter += 1
    guess: int = int(input("Enter guess: "))

    # checking the parameters to continue the loop or not
    if guess_limiter == 6:
        print('You tried.')
        break
    elif rnd_number.equal(guess):
        print('Correct')
        break
    elif rnd_number.greater(guess):
        print('Greater Than')
    else:
        print('Less Than')
