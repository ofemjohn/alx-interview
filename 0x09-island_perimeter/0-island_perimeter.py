#!/usr/bin/python3

def island_perimeter(grid):
    '''
    Args:
      grid: A list of list of integers.

    Returns:
      The perimeter of the island.
    '''

    island_perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                island_perimeter += 4
                if i > 0 and grid[i - 1][j] == 1:
                    island_perimeter -= 2
                if j > 0 and grid[i][j - 1] == 1:
                    island_perimeter -= 2

    return island_perimeter
