"""Solution for [insert link]."""
import copy
from day6 import problem1


def solution():
  """Solve the problem."""
  maze = problem1.read_map()
  path = problem1.run_maze(copy.deepcopy(maze))
  # Drop start and first coord.
  path = path[1:]
  coords = set(path)
  count = 0
  tot = 0
  for i, j in coords:
    print(f"Adding object at ({i}, {j}).")
    tot += 1
    new_maze = copy.deepcopy(maze)
    new_maze[i][j] = "#"
    new_coords = problem1.run_maze(new_maze)
    if len(new_coords) == 0:
      count += 1
    print(f"TOT: {tot}. LOOPS: {count}")
  return count