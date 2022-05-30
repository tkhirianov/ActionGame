import pygame.draw

import constants
import actor


class Worm(actor.Actor):
    _default_radius = 20
    _default_health = 10
    _color = (160, 160, 0)
    _width = 24
    _height = 8
    _rect_radius = 3

    def __init__(self, x: float):
        y = constants.HEIGHT - Worm._height / 2
        super().__init__(x, y, Worm._default_radius, Worm._default_health)

    def move(self, dt: float):
        self.x += 1

    def show(self, screen):
        rect = pygame.Rect(self.x - self._width/2, self.y - self._height/2,
                           self._width, self._height)
        pygame.draw.rect(screen, Worm._color, rect, border_radius=self._rect_radius)

    def hit(self, other):
        """ Worm is a harmless creature... """
        pass
