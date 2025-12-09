"""Solution for https://adventofcode.com/2025/day/9."""

from util import read

_TEST = """7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3"""


def solution():
  """Solve the problem."""
  data = read.read_input()
  # data = _TEST
  rows = data.split("\n")
  tiles = []
  for row in rows:
    x, y = row.split(",")
    tiles.append((int(x), int(y)))

  max_area = 0

  for i, tile_i in enumerate(tiles):
    for j, tile_j in enumerate(tiles[i+1:]):
      i_x, i_y = tile_i
      j_x, j_y = tile_j
      area = ((abs(i_x - j_x) + 1) * (abs(i_y - j_y) + 1))
      # print(f"({i_x},{i_y}) X ({j_x},{j_y}) = {area}")
      max_area = max(max_area, area)
  return max_area
