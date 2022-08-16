# Import dependencies
import random as rnd


def inside(item: str, iterable: tuple) -> bool:
    if item in iterable:
        return True
    else:
        return False


def randomize(iterable: tuple) -> str:
    return rnd.choice(iterable)


play_options = ('rock', 'paper', 'scissor')
entered = 'Rock'
print(inside(entered.lower(), play_options), randomize(play_options))
