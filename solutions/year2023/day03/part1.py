"""Solution for https://adventofcode.com/2023/day/3."""

from util import read


def read_grid():
  data = read.read_input()
  return [list(row) for row in data.split("\n")]


def is_part_num(
    grid: list[list[str]],
    start_j: int,
    start_i: int,
    digits: str) -> bool:
  coords = [(start_j - 1, i) for i in range(start_i - 1, start_i + len(digits) + 1)]
  coords.extend([(start_j, start_i - 1), (start_j, start_i + len(digits))])
  coords.extend([(start_j + 1, i) for i in range(start_i - 1, start_i + len(digits) + 1)])

  for j, i in coords:
    if j < 0 or j >= len(grid):
      continue
    if i < 0 or i >= len(grid[j]):
      continue
    val = grid[j][i]
    if val == "." or val.isnumeric():
      continue
    return True
  return False


def solution():
  """Solve the problem."""
  grid = read_grid()
  ans = 0
  for j, row in enumerate(grid):
    i = 0
    digits = ""
    for i, char in enumerate(row):
      if char.isnumeric():
        digits += char
      elif digits:
        if is_part_num(grid, j, i - len(digits), digits):
          ans += int(digits)
        digits = ""
    if digits and is_part_num(grid, j, len(row) - len(digits), digits):
      ans += int(digits)
  return ans
