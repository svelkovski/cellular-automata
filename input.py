import pygame
from settings import CELL_SIZE, COLS, ROWS


def handle_events(running_simulation):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False, running_simulation, "quit"

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                running_simulation = not running_simulation

            if event.key == pygame.K_c:
                return True, running_simulation, "clear"

    return True, running_simulation, None


def handle_mouse(grid, running_simulation):
    if running_simulation:
        return

    mouse = pygame.mouse.get_pressed()
    mx, my = pygame.mouse.get_pos()

    gx = mx // CELL_SIZE
    gy = my // CELL_SIZE

    if 0 <= gx < COLS and 0 <= gy < ROWS:
        if mouse[0]:
            grid[gx][gy] = 1
        if mouse[2]:
            grid[gx][gy] = 0
