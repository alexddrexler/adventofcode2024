"""Solution for https://adventofcode.com/2023/day/3#part2."""

from util import read


def _has_digit(grid: list[list[str]], j: int, i: int) -> bool:
  if j < 0 or j >= len(grid):
    return False
  if i < 0 or i >= len(grid[j]):
    return False
  return grid[j][i].isnumeric()


def _get_rooted_num(grid: list[list[str]], j: int, i: int) -> tuple[tuple[int, int], int]:
  root = (j, i)
  num_str = ""
  x = i
  while _has_digit(grid, j, x):
    num_str = grid[j][x] + num_str
    root = (j, x)
    x -= 1
  x = i + 1
  while _has_digit(grid, j, x):
    num_str += grid[j][x]
    x += 1

  return root, int(num_str)



def _get_part_nums(grid: list[list[str]], j: int, i: int) -> list[int]:
  coords = [
    (j-1, i-1), (j-1, i), (j-1, i+1),
    (j, i-1), (j, i+1),
    (j+1, i-1), (j+1, i), (j+1, i+1),
  ]

  rooted_nums = {}
  for y, x in coords:
    if _has_digit(grid, y, x):
      root, num = _get_rooted_num(grid, y, x)
      rooted_nums[root] = num

  return list(rooted_nums.values())


def solution():
  """Solve the problem."""
  grid = read.read_input_grid()
  ans = 0

  for j, row in enumerate(grid):
    for i, val in enumerate(row):
      if val == "*":
        nums = _get_part_nums(grid, j, i)
        if len(nums) != 2:
          continue
        ans += nums[0] * nums[1]

  return ans
