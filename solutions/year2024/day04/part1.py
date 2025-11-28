"""Solution for https://adventofcode.com/2024/day/4."""
from util import read


def find_all(grid, word):
  chars = list(word)
  matches = 0
  for i in range(len(grid)):
    for j in range(len(grid[0])):
      if grid[i][j] == chars[0]:
        matches += search(grid, chars, i, j)
  return matches



def search(grid, chars, i, j):
  i_incs = range(-1, 2)
  j_incs = range(-1, 2)
  count = 0
  for i_inc in i_incs:
    for j_inc in j_incs:
      if search_in_dir(grid, chars, i, j, i_inc, j_inc):
        count += 1
  return count


def search_in_dir(grid, chars, i, j, i_inc, j_inc):
  min_i = 0
  max_i = len(grid) - 1
  min_j = 0
  max_j = len(grid[0]) - 1
  for pos, c in enumerate(chars):
    new_i = i + (pos * i_inc)
    if new_i < min_i or new_i > max_i:
      return False
    new_j = j + (pos * j_inc)
    if new_j < min_j or new_j > max_j:
      return False
    grid_char = grid[new_i][new_j]
    if grid_char != c:
      return False
  return True


def read_grid():
  content = read.read_input()
  return [list(row) for row in content.split("\n")]


def solution():
  """Solve the problem."""
  grid = read_grid()
  return find_all(grid, "XMAS")
