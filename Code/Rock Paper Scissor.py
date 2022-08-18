# Import dependencies
import random as rnd


class Processes:
    def __init__(self, iterable):
        self.iter = iterable

    def inside(self, item: str) -> bool:
        if item in self.iter:
            return True
        else:
            return False

    def randomize(self) -> str:
        return rnd.choice(self.iter)


def winner(iterable: tuple) -> bool:
    temp_dict = {'rock': 1, 'paper': 2, 'scissor': 3}
    win_tuple = (-2, 1)

    # Extract their values from temp_dict and subtract it
    identifier = temp_dict[iterable[0]] - temp_dict[iterable[1]]
    if identifier in win_tuple:
        return True
    else:
        return False


# Setup
play_options = ('rock', 'paper', 'scissor')
game = Processes(play_options)
game_limit = 0

# Playing the game
while True:
    game_limit += 1
    if game_limit == 4:
        print('GAME OVER...')
        break

    play = input('Enter choice: ').lower()

    if game.inside(play):
        input_ = (play, game.randomize())

        if winner(input_):
            print('You win.')
        else:
            print('Computer beats you.')
    else:
        print('END...WRONG INPUT')
        break
