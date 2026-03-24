import pygame
import sys

from settings import WIDTH, HEIGHT, FPS
from grid import create_grid, update_grid
from input import handle_events, handle_mouse
from render import draw

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

grid = create_grid()
running_simulation = False

while True:
    running, running_simulation, action = handle_events(running_simulation)

    if not running:
        pygame.quit()
        sys.exit()

    if action == "clear":
        grid = create_grid()

    handle_mouse(grid, running_simulation)

    if running_simulation:
        grid = update_grid(grid)
        clock.tick(FPS)
    else:
        clock.tick(60)

    draw(screen, grid)
    pygame.display.flip()
