"""Solution for https://adventofcode.com/2025/day/9#part2."""

from util import read

_TEST = """7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3"""


def is_valid_edge(t1, t2, e1, e2):
  t1_x, t1_y = t1
  t2_x, t2_y = t2
  min_x, max_x = sorted((t1_x, t2_x))
  min_y, max_y = sorted((t1_y, t2_y))

  e1_x, e1_y = e1
  e2_x, e2_y = e2

  if e2_x - e1_x == 0:
    if e2_x <= min_x or e2_x >= max_x:
      return True
    min_e_y, max_e_y = sorted((e1_y, e2_y))
    if min_e_y >= max_y:
      return True
    if max_e_y <= min_y:
      return True
    return False
  if e2_y - e1_y == 0:
    if e2_y <= min_y or e2_y >= max_y:
      return True
    min_e_x, max_e_x = sorted((e1_x, e2_x))
    if min_e_x >= max_x:
      return True
    if max_e_x <= min_x:
      return True
    return False


def is_valid(tile_pair, tiles):
  t1, t2 = tile_pair
  e1 = tiles[-1]
  t = 0
  while t < len(tiles):
    e2 = tiles[t]
    ive = is_valid_edge(t1, t2, e1, e2)
    # print(f"{t1} & {t2}; e: {e1} & {e2}: {ive}")
    if not ive:
      return False
    e1 = e2
    t += 1
  return True


def solution():
  """Solve the problem."""
  data = read.read_input()
  # data = _TEST
  rows = data.split("\n")
  tiles = []
  for row in rows:
    x, y = row.split(",")
    tiles.append((int(x), int(y)))

  areas = {}
  for i, tile_i in enumerate(tiles):
    for j, tile_j in enumerate(tiles[i+1:]):
      i_x, i_y = tile_i
      j_x, j_y = tile_j
      area = ((abs(i_x - j_x) + 1) * (abs(i_y - j_y) + 1))
      # print(f"({i_x},{i_y}) X ({j_x},{j_y}) = {area}")
      if area not in areas:
        areas[area] = []
      areas[area].append((tile_i, tile_j))
  max_areas = sorted(areas.keys())

  while max_areas:
    max_area = max_areas.pop()
    tile_pairs = areas[max_area]
    while tile_pairs:
      pair = tile_pairs.pop()
      if is_valid(pair, tiles):
        return max_area

  return None
