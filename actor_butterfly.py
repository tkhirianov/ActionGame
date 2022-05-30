import pygame.draw

import constants
import actor


class Butterfly(actor.Actor):
    _default_radius = 20
    _default_health = 25
    _color = (210, 60, 50)
    _width = 30
    _height = 30
    _rect_radius = 15

    def __init__(self, x: float, y: float):
        super().__init__(x, y, Butterfly._default_radius, Butterfly._default_health)

    def move(self, dt: float):
        self.x += 1
        self.y -= 1

    def show(self, screen):
        rect = pygame.Rect(self.x - self._width/2, self.y - self._height/2,
                           self._width, self._height)
        pygame.draw.rect(screen, Butterfly._color, rect, border_radius=self._rect_radius)

    def hit(self, other):
        """ Butterfly is a harmless creature... """
        pass
