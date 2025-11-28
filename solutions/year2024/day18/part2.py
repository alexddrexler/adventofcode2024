"""Solution for https://adventofcode.com/2024/day/18#part2."""
import copy

from solutions.year2024.day18 import part1


def get_path(maze):
  cmaze = copy.deepcopy(maze)
  steps = part1.run_maze(cmaze)
  if steps is None:
    return None
  cur = (70, 70)
  path = {cur, }
  while cur != (0, 0):
    i, j = cur
    for ni, nj in [(i+1, j), (i, j+1), (i-1, j), (i, j-1),]:
      if part1.is_walkable(cmaze, ni, nj) and type(cmaze[ni][nj]) == int:
        if cmaze[ni][nj] < cmaze[i][j]:
          path.add((ni, nj))
          cur = (ni, nj)
          break
  return path


def solution():
  """Solve the problem."""
  grid = []
  path = None
  for _ in range(71):
    grid.append(["."] * 71)
  for (x, y) in part1.read_coords():
    grid[y][x] = "#"
    if path is None or (y, x) in path:
      path = get_path(grid)
      if path is None:
        return (x, y)
