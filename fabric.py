import random

import constants
from actor_worm import Worm
from actor_butterfly import Butterfly


def create_random_actor():
    index_of_character = random.randint(0, 1)
    if index_of_character == 0:
        x = random.randint(Worm._width/2, constants.WIDTH - 1 - Worm._width/2)
        return Worm(x)
    else:
        x = random.randint(Butterfly._width/2, constants.WIDTH - 1 - Butterfly._width/2)
        y = random.randint(Butterfly._height/2, constants.WIDTH - 1 - Butterfly._height/2)
        return Butterfly(x, y)
