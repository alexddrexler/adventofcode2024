"""Solution for https://adventofcode.com/2024/day/6."""
from util import read


UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3
DIRECTIONS = [UP, RIGHT, DOWN, LEFT]
DIR_CHARS = ["^", ">", "V", "<"]


def read_map():
  content = read.read_input()
  map_grid = []
  for row in content.split("\n"):
    map_grid.append(list(row))
  return map_grid


def run_maze(maze):
  i, j, direction = get_start_pos(maze)
  path = list()
  while i is not None:
    path.append((i, j))
    if type(maze[i][j]) == str:
      maze[i][j] = list()
    if direction in maze[i][j]:
      return list()
    maze[i][j].append(direction)
    i, j, direction = step(maze, i, j, direction)
  return path


def get_start_pos(maze) -> tuple[int, int, int]:
  for i, row in enumerate(maze):
    for j, char in enumerate(row):
      if char == "^":
        return (i, j, UP)


def step(maze, i, j, direction):
  next_i, next_j = get_next_pos(i, j, direction)
  while not is_valid(maze, next_i, next_j):
    direction = DIRECTIONS[(direction + 1) % 4]
    next_i, next_j = get_next_pos(i, j, direction)
  if is_edge(maze, next_i, next_j):
    return None, None, None
  return next_i, next_j, direction


def get_next_pos(i, j, direction):
  if direction == UP:
    return (i-1, j)
  elif direction == RIGHT:
    return (i, j+1)
  elif direction == DOWN:
    return (i+1, j)
  else:  # LEFT.
    return (i, j-1)


def is_edge(maze, i, j):
  return i < 0 or i >= len(maze) or j < 0 or j >= len(maze[i])


def is_valid(maze, i, j):
  if is_edge(maze, i, j):
    return True
  return maze[i][j] != "#"


def print_maze(maze):
  print("+" + "-" * len(maze[0]) + "+")
  for row in maze:
    pr_row = "|"
    for char in row:
      if type(char) == list:
        pr_row += DIR_CHARS[char[-1]]
      elif char == ".":
        pr_row += " "
      else:
        pr_row += char
    pr_row += "|"
    print(pr_row)
  print("+" + "-" * len(maze[0]) + "+")


def solution():
  """Solve the problem."""
  maze = read_map()
  count_distinct = len(set(run_maze(maze)))
  print_maze(maze)
  return count_distinct
