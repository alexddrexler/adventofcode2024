"""Solution for [insert link]."""
from day4 import problem1


def find_all_xs(grid):
  count = 0
  for i in range(len(grid)):
    for j in range(len(grid[0])):
      if grid[i][j] == "A" and is_x(grid, i, j):
        count += 1
  return count


def is_x(grid, i, j):
  if i - 1 < 0 or i + 1 == len(grid):
    return False
  if j - 1 < 0 or j + 1 == len(grid[0]):
    return False
  ul = grid[i-1][j-1]
  dl = grid[i+1][j-1]
  ur = grid[i-1][j+1]
  dr = grid[i+1][j+1]

  if not any([
      ul == "M" and dr == "S",
      dr == "M" and ul == "S"
  ]):
    return False

  return any([
      ur == "M" and dl == "S",
      dl == "M" and ur == "S"
  ])


def solution():
  """Solve the problem."""
  grid = problem1.read_grid()
  return find_all_xs(grid)
