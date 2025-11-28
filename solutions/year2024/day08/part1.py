"""Solution for https://adventofcode.com/2024/day/8."""
from collections import defaultdict

from util import read


def read_grid():
  content = read.read_input()
  grid = []
  for row in content.split("\n"):
    grid.append(list(row))
  return grid


def get_valid_antinode_count(grid, nodes):
  antinodes = set()
  for coords in nodes.values():
    for coord_a in coords:
      for coord_b in coords:
        if coord_a == coord_b:
          continue
        i_a, j_a = coord_a
        i_b, j_b = coord_b
        new_i = i_a + (i_a - i_b)
        new_j = j_a + (j_a - j_b)
        if is_valid(grid, new_i, new_j):
          antinodes.add((new_i, new_j))
  return len(antinodes)


def is_valid(grid, i, j):
  return all([
      i >= 0,
      i < len(grid),
      j >= 0,
      j < len(grid[0]),
  ])


def get_common_nodes(grid):
  nodes = defaultdict(set)
  for i, row in enumerate(grid):
    for j, val in enumerate(row):
      if val != ".":
        nodes[val].add((i, j))
  return nodes


def solution():
  """Solve the problem."""
  grid = read_grid()
  nodes = get_common_nodes(grid)
  count = get_valid_antinode_count(grid, nodes)
  return count
