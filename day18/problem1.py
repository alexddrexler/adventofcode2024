"""Solution for https://adventofcode.com/2024/day/18."""
from util import read


def read_coords(n=None):
  content = read.read_file("day18/input1.txt")
  rows = content.split("\n")
  if n is None:
    n = len(rows)
  for i in range(n):
    row = rows[i]
    x, y = row.split(",")
    yield (int(x), int(y))


def run_maze(maze):
  maze[0][0] = 0
  nexts = [(0, 0), ]
  while nexts:
    i, j = nexts.pop(0)
    steps = maze[i][j]
    if i == j == 70:
      return steps
    for ni, nj in [(i+1, j), (i, j+1), (i-1, j), (i, j-1),]:
      if not is_walkable(maze, ni, nj):
        continue
      nsteps = maze[ni][nj]
      if type(nsteps) == int:
        continue
      maze[ni][nj] = steps + 1
      nexts.append((ni, nj))
  print_maze(maze)
  return None


def is_walkable(maze, i, j):
  if i < 0 or i >= len(maze) or j < 0 or j >= len(maze[0]):
    return False
  return maze[i][j] != "#"


def print_maze(maze):
  print("+" + "-"*71 + "+")
  for row in maze:
    row_str = "|"
    for char in row:
      if type(char) == int:
        row_str += "?"
      else:
        row_str += str(char)
    print(row_str + "|")
  print("+" + "-"*71 + "+")


def solution():
  """Solve the problem."""
  grid = []
  for _ in range(71):
    grid.append(["."] * 71)
  for (x, y) in read_coords(1024):
    grid[y][x] = "#"
  steps = run_maze(grid)
  return steps