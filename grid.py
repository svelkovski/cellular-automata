from settings import COLS, ROWS, ALIVE_CELL, DEAD_CELL


def create_grid():
    grid = []

    for x in range(COLS):
        column = []
        for y in range(ROWS):
            column.append(0)
        grid.append(column)

    return grid


def count_neighbors(grid, x, y):
    total = 0

    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if i == 0 and j == 0:
                continue

            nx = x + i
            ny = y + j

            if 0 <= nx < COLS and 0 <= ny < ROWS:
                total += grid[nx][ny]

    return total


def update_grid(grid):
    new_grid = create_grid()

    for x in range(COLS):
        for y in range(ROWS):

            neighbors = count_neighbors(grid, x, y)

            if grid[x][y] == ALIVE_CELL and (neighbors == 2 or neighbors == 3):
                new_grid[x][y] = ALIVE_CELL

            elif grid[x][y] == 0 and neighbors == 3:
                new_grid[x][y] = ALIVE_CELL

            else:
                new_grid[x][y] = DEAD_CELL

    return new_grid
