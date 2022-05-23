import abc

import constants


class Actor(abc.ABC):
    def __init__(self, x: float, y: float, r: float, health: int):
        self.x = x
        self.y = y
        self.r = r
        self.health = health

    @abc.abstractmethod
    def move(self):
        pass

    @abc.abstractmethod
    def show(self, screen):
        pass

    @abc.abstractmethod
    def hit(self, other):
        pass

