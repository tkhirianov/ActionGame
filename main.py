import pygame
import random
from constants import *


def mainloop():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("TANKS")
    clock = pygame.time.Clock()
    game_over = False
    while not game_over:
        dt = clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

        pygame.display.flip()


if __name__ == '__main__':
    pygame.init()
    mainloop()
    pygame.quit()
