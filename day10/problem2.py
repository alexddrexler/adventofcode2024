"""Solution for [insert link]."""
from collections import defaultdict

from util import read


def read_grid():
  content = read.read_file("day10/input1.txt")
  grid = []
  for row in content.split("\n"):
    height_row = []
    for char in row:
      if char == ".":
        height_row.append(-1)
      else:
        height_row.append(int(char))
    grid.append(height_row)
  return grid


def find_trailheads(grid):
  trailheads = []
  for i, row in enumerate(grid):
    for j, height in enumerate(row):
      if height == 0:
        trailheads.append((i, j))
  return trailheads


def take_next_step(grid, ongoing_paths):
  trail_sum = 0
  while ongoing_paths:
    position = list(ongoing_paths.keys())[0]
    count = ongoing_paths.pop(position)
    i, j = position
    if grid[i][j] == 9:
      trail_sum += count
    else:
      next_steps = get_next_steps(grid, position)
      for next_step in next_steps:
        ongoing_paths[next_step] += count
  return trail_sum


def get_next_steps(grid, position):
  curr_i, curr_j = position
  new_positions = [
      (curr_i - 1, curr_j),  # UP.
      (curr_i + 1, curr_j),  # DOWN.
      (curr_i, curr_j - 1),  # LEFT.
      (curr_i, curr_j + 1),  # RIGHT.
  ]
  next_steps = []
  target_height = grid[curr_i][curr_j] + 1
  for new_position in new_positions:
    if is_valid(grid, new_position, target_height):
      next_steps.append(new_position)
  return next_steps


def is_valid(grid, position, target_height):
  i, j = position
  if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
    return False
  return grid[i][j] == target_height


def solution():
  """Solve the problem."""
  grid = read_grid()
  trailheads = find_trailheads(grid)
  ongoing_paths = defaultdict(int)
  for position in trailheads:
    ongoing_paths[position] += 1
  return take_next_step(grid, ongoing_paths)
