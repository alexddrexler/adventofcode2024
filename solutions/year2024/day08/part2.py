"""Solution for https://adventofcode.com/2024/day/8#part2."""
import math

from solutions.year2024.day08 import part1


def get_antinodes(grid, nodes):
  antinodes = set()
  for coords in nodes.values():
    for coord_a in coords:
      for coord_b in coords:
        if coord_a == coord_b:
          continue
        i_a, j_a = coord_a
        i_b, j_b = coord_b
        diff_i = i_a - i_b
        diff_j = j_a - j_b
        gcd = math.gcd(diff_i, diff_j)
        diff_i = diff_i / gcd
        diff_j = diff_j / gcd
        new_i = i_a
        new_j = j_a
        while part1.is_valid(grid, new_i, new_j):
          antinodes.add((new_i, new_j))
          new_i += diff_i
          new_j += diff_j
        new_i = i_a
        new_j = j_a
        while part1.is_valid(grid, new_i, new_j):
          antinodes.add((new_i, new_j))
          new_i -= diff_i
          new_j -= diff_j
  return antinodes




def solution():
  """Solve the problem."""
  grid = part1.read_grid()
  nodes = part1.get_common_nodes(grid)
  return len(get_antinodes(grid, nodes))
