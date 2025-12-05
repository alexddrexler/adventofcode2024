"""Solution for https://adventofcode.com/2025/day/4."""

from util import read


def _has_symbol(grid: list[list[str]], j: int, i: int, symbol: str) -> bool:
  if j < 0 or j >= len(grid):
    return False
  if i < 0 or i >= len(grid[j]):
    return False
  return grid[j][i] == symbol


def solution():
  """Solve the problem."""
  grid = read.read_input_grid()
  ans = 0

  for j, row in enumerate(grid):
    for i, val in enumerate(row):
      if val != "@":
        continue
      adjacents = [
          (j-1, i-1), (j-1, i), (j-1, i+1),
          (j, i-1), (j, i+1),
          (j+1, i-1), (j+1, i), (j+1, i+1),
      ]
      tot = 0
      for y, x in adjacents:
        if _has_symbol(grid, y, x, "@"):
          tot += 1
      if tot < 4:
        ans +=1
  return ans
