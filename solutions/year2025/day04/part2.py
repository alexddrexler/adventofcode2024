"""Solution for https://adventofcode.com/2025/day/4#part2."""

from util import read


_TEST = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""


def _has_symbol(grid: list[list[str]], j: int, i: int, symbol: str) -> bool:
  if j < 0 or j >= len(grid):
    return False
  if i < 0 or i >= len(grid[j]):
    return False
  return grid[j][i] == symbol


def solution():
  """Solve the problem."""
  grid = read.read_input_grid()
  nodes = {}
  ans = 0

  for j, row in enumerate(grid):
    for i, val in enumerate(row):
      if val != "@":
        continue
      nodes[(j, i)] = set()
      prevs = [(j-1, i-1), (j-1, i), (j-1, i+1), (j, i-1),]
      for y, x in prevs:
        if _has_symbol(grid, y, x, "@"):
          nodes[(j, i)].add((y, x))
          nodes[(y, x)].add((j, i))

  checks = set(nodes.keys())
  for node, adjs in nodes.items():
    print(f"{node}: {adjs}")
  print(len(checks))
  while checks:
    coord = checks.pop()
    if len(nodes[coord]) < 4:
      #print(f"Popping {coord} with {len(nodes[coord])}")
      ans += 1
      for adj in nodes[coord]:
        nodes[adj].remove(coord)
        checks.add(adj)

  return ans
