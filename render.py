import pygame
from settings import CELL_SIZE, COLS, ROWS


def draw(screen, grid):
    screen.fill((0, 0, 0))

    for x in range(COLS):
        for y in range(ROWS):
            rect = pygame.Rect(
                x * CELL_SIZE,
                y * CELL_SIZE,
                CELL_SIZE,
                CELL_SIZE
            )

            if grid[x][y] == 1:
                pygame.draw.rect(screen, (255, 255, 255), rect)

            pygame.draw.rect(screen, (0, 0, 0), rect, 1)
