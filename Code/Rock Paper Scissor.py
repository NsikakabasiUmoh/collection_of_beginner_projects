# Import dependencies
import random as rnd


def inside(item: str, iterable: tuple) -> bool:
    if item in iterable:
        return True
    else:
        return False


def randomize(iterable: tuple) -> str:
    return rnd.choice(iterable)


def processes(iterable: tuple) -> bool:
    temp_dict = {'rock': 1, 'paper': 2, 'scissor': 3}
    win_tuple = (-2, 1)

    # Extract their values from temp_dict and subtract it
    identifier = temp_dict[iterable[0]] - temp_dict[iterable[1]]
    if identifier in win_tuple:
        return True
    else:
        return False


play_options = ('rock', 'paper', 'scissor')
play = input('Enter choice: ').lower()
if inside(play, play_options):
    input_tuple = (play, randomize(play_options))
    if processes(input_tuple):
        print('You win.')
    else:
        print('Computer beats you.')
