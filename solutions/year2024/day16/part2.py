"""Solution for https://adventofcode.com/2024/day/16#part2."""
from solutions.year2024.day16 import part1


UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3
DIRECTIONS = [UP, RIGHT, DOWN, LEFT]


def get_end_tile(maze):
  for i, row in enumerate(maze):
    for j, char in enumerate(row):
      if char == "E":
        return (i, j)


def get_end_vals(maze, memo):
  i, j = get_end_tile(maze)
  cost = min(memo[i][j])
  return [((i, j), d) for d in DIRECTIONS if memo[i][j][d] == cost]


def get_neighbor(pos, d):
  i, j = pos
  if d == UP:
    return (i-1, j)
  elif d == RIGHT:
    return (i, j+1)
  elif d == DOWN:
    return (i+1, j)
  else:  # LEFT.
    return (i, j-1)

def get_nexts(maze, memo, pos, d):
  nexts = []
  i, j = pos
  print(memo[i][j])
  if maze[i][j] == "S":
    print("AT START")
    return []
  cost = memo[i][j][d]
  for d_mod, cost_mod in [(0, 0), (-1, -1000), (1, -1000)]:
    new_d = (d + d_mod) % 4
    ec = cost + cost_mod
    print(f"NEW D: {new_d}, EC: {ec}")
    if memo[i][j][new_d] != ec:
      continue
    ni, nj = get_neighbor(pos, (new_d + 2) % 4)
    print(f"NEIGHBOR: ({ni}, {nj}): {memo[ni][nj][new_d]}")
    if memo[ni][nj][new_d] == ec - 1:
      print(f"ADDING ({ni}, {nj})")
      nexts.append(((ni, nj), new_d))
  return nexts


def get_best_paths(maze, memo):
  tiles = set()
  nexts = get_end_vals(maze, memo)
  while nexts:
    pos, d = nexts.pop()
    print(f"{pos}, {d}")
    tiles.add(pos)
    nexts.extend(get_nexts(maze, memo, pos, d))
  return tiles


def solution():
  """Solve the problem."""
  maze = part1.read_maze()
  memo = part1.run_maze(maze)
  return len(get_best_paths(maze, memo))
