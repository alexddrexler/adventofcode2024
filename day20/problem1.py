"""Solution for https://adventofcode.com/2024/day/20."""
from collections import defaultdict

from util import read


TEST = """###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############"""


def read_maze(content=None):
  if content is None:
    content = read.read_file("day20/input1.txt")
  maze = []
  for row in content.split("\n"):
    maze.append(list(row))
  return maze


def find_point(maze, marker):
  for i, row in enumerate(maze):
    for j, char in enumerate(row):
      if char == marker:
        return (i, j)
  return None


def get_adjacent_paths(maze, i, j):
  nexts = []
  for ni, nj in [(i+1, j), (i, j+1), (i-1, j), (i, j-1),]:
    if ni < 0 or ni >= len(maze) or nj < 0 or nj >= len(maze[0]):
      continue
    if maze[ni][nj] == "#":
      continue
    nexts.append((ni, nj))
  return nexts


def get_distances_from_end(maze):
  distances = []
  for row in maze:
    distances.append([-1] * len(row))
  ei, ej = find_point(maze, "E")
  distances[ei][ej] = 0
  nexts = [(ei, ej),]
  while nexts:
    i, j = nexts.pop(0)
    adjs = get_adjacent_paths(maze, i, j)
    min_prev = None
    for ai, aj in adjs:
      dist = distances[ai][aj]
      if dist < 0:
        nexts.append((ai, aj))
        continue
      if min_prev is None:
        min_prev = dist
        continue
      min_prev = min(min_prev, dist)
    if min_prev is not None:
      distances[i][j] = min_prev + 1
  return distances


def find_shortcuts(maze, distances, min_diff = 1):
  shortcuts = defaultdict(int)
  for i, row in enumerate(maze):
    if i == 0 or i == len(maze) - 1:
      continue  # No shortcuts on edges.
    for j, char in enumerate(row):
      if j == 0 or j == len(maze[0]) - 1:
        continue  # No shortcuts on edges.
      if char != "#":
        continue  # Not a wall.
      adjs = get_adjacent_paths(maze, i, j)
      if len(adjs) < 2:
        continue  # No connection.
      for ind, (ai, aj) in enumerate(adjs):
        d1 = distances[ai][aj]
        for bi, bj in adjs[ind:]:
          d2 = distances[bi][bj]
          diff = abs(d2-d1) - 2
          if diff >= min_diff:
            shortcuts[diff] += 1
  return shortcuts



def solution():
  """Solve the problem."""
  maze = read_maze()
  # p.print_char_grid(maze)
  distances = get_distances_from_end(maze)
  shortcuts = find_shortcuts(maze, distances, min_diff=100)
  # for i in sorted(shortcuts.keys()):
  #   print(f"{i}: {shortcuts[i]}")
  return sum(shortcuts.values())