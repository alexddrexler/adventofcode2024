"""Solution for https://adventofcode.com/2024/day/20#part2."""
from collections import defaultdict

from day20 import problem1


def find_shortcuts(distances, min_diff=1):
  shortcuts = defaultdict(int)
  for i, row in enumerate(distances):
    for j, val in enumerate(row):
      if val < min_diff:
        continue
      for ni in range(i-20, i+21):
        if ni < 0:
          continue
        if ni >= len(distances):
          break
        for nj in range(j-20, j+21):
          if nj < 0:
            continue
          if nj >= len(distances[0]):
            break
          cheat_distance = abs(ni-i) + abs(nj-j)
          if cheat_distance > 20:
            continue
          end_val = distances[ni][nj]
          if end_val < 0:
            continue
          diff = val - end_val - cheat_distance
          if diff < min_diff:
            continue
          shortcuts[diff] += 1
  return shortcuts


def solution():
  """Solve the problem."""
  maze = problem1.read_maze()
  distances = problem1.get_distances_from_end(maze)
  shortcuts = find_shortcuts(distances, min_diff=100)
  # for i in sorted(shortcuts.keys()):
  #   print(f"{i}: {shortcuts[i]}")
  return sum(shortcuts.values())
