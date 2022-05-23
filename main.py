import pygame
import random

from constants import *
import fabric


def mainloop():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("TANKS")
    clock = pygame.time.Clock()
    game_over = False
    list_of_actors = [fabric.create_random_actor() for i in range(10)]
    while not game_over:
        dt = clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
        # move all actors on the screen
        for actor in list_of_actors:
            actor.move(dt)

        screen.fill(BLACK)
        # show all actors on the screen
        for actor in list_of_actors:
            actor.show(screen)
        pygame.display.flip()


if __name__ == '__main__':
    pygame.init()
    mainloop()
    pygame.quit()
