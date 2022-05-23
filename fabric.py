import random

import constants
from actor_worm import Worm


def create_random_actor():
    x = random.randint(Worm._width/2, constants.WIDTH - 1 - Worm._width/2)
    return Worm(x)