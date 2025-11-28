"""Solution for https://adventofcode.com/2024/day/16."""
from util import read


UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3


def read_maze():
  content = read.read_input()
  return [list(row) for row in content.split("\n")]


def get_memo(maze) -> list[list[list[int]]]:
  memo = []
  for row in maze:
    memo_row = []
    for _ in row:
      memo_row.append([-1, -1, -1, -1])
    memo.append(memo_row)
  return memo


def fill_memo(memo, pos, direction, cost):
  i, j = pos
  cost_mods = (0, 1000, 2000, 1000)
  for cost_mod in cost_mods:
    new_cost = cost + cost_mod
    prev_cost = memo[i][j][direction]
    if prev_cost < 0 or new_cost < prev_cost:
      memo[i][j][direction] = new_cost
    direction = (direction + 1) % 4


def can_and_should_go(maze, memo, pos, direction, cost):
  i, j = pos
  if maze[i][j] == "#":
    return False  # Wall.
  old_cost = memo[i][j][direction]
  return old_cost < 0 or old_cost > cost


def find_start(maze, memo):
  for i, row in enumerate(maze):
    for j, char in enumerate(row):
      if char == "S":
        start = (i, j)
        fill_memo(memo, start, RIGHT, 0)
        return start


def get_next_pos(pos, direction):
  i, j = pos
  if direction == UP:
    return (i-1, j)
  elif direction == RIGHT:
    return (i, j+1)
  elif direction == DOWN:
    return (i+1, j)
  else:  # LEFT.
    return (i, j-1)


def explore(maze, memo, pos):
  i, j = pos
  nexts = []
  for direction in [UP, RIGHT, DOWN, LEFT]:
    next_pos = get_next_pos(pos, direction)
    cost = memo[i][j][direction] + 1
    if not can_and_should_go(maze, memo, next_pos, direction, cost):
      continue
    fill_memo(memo, next_pos, direction, cost)
    nexts.append(next_pos)
  return nexts

def get_end_cost(maze, memo):
  for i, row in enumerate(maze):
    for j, char in enumerate(row):
      if char == "E":
        return min(memo[i][j])


def run_maze(maze):
  memo = get_memo(maze)
  nexts = [find_start(maze, memo),]
  while nexts:
    pos = nexts.pop()
    nexts.extend(explore(maze, memo, pos))
  return memo


def solution():
  """Solve the problem."""
  maze = read_maze()
  memo = run_maze(maze)
  return get_end_cost(maze, memo)
