"""Solution for https://adventofcode.com/2024/day/12#part2."""
from util import read


def read_farm():
  content = read.read_input()
  out = []
  for row in content.split("\n"):
    out.append(list(row))
  return out


def get_fence_price(farm):
  fence_price = 0
  in_region = []
  for _ in range(len(farm)):
    row = []
    for _ in range(len(farm[0])):
      row.append(False)
    in_region.append(row)
  for i, row in enumerate(farm):
    for j, val in enumerate(row):
      if in_region[i][j]:
        continue
      area, corners = get_price_for_region(farm, in_region, i, j)
      print(f"{val}: area: {area}, edges: {corners}")
      fence_price += area * corners
  return fence_price


def is_in_region(farm, i, j, val):
  if i < 0 or i >= len(farm) or j < 0 or j >= len(farm[0]):
    return False
  new_val = farm[i][j]
  if new_val != val:
    return False
  return True


def get_price_for_region(farm, in_region, start_i, start_j):
  area = 0
  corners = 0
  squares = {(start_i, start_j),}
  while squares:
    area += 1
    i, j = squares.pop()
    print(f"Assessing ({i}, {j})")
    in_region[i][j] = True
    val = farm[i][j]
    dirs = [
        (-1, 0),  # UP.
        (0, 1),   # RIGHT.
        (1, 0),   # DOWN.
        (0, -1),  # LEFT.
    ]
    dir_bools = []
    for new_i, new_j in [(i + i_mod, j + j_mod) for (i_mod, j_mod) in dirs]:
      if not is_in_region(farm, new_i, new_j, val):
        dir_bools.append(False)
        continue
      dir_bools.append(True)
      if in_region[new_i][new_j]:
        continue
      squares.add((new_i, new_j))
    for n, dir_bool in enumerate(dir_bools):
      next_dir_bool = dir_bools[(n + 1) % 4]
      if not dir_bool and not next_dir_bool:
        corners += 1
        continue
      if dir_bool and next_dir_bool:
        i_mod, j_mod = dirs[n]
        i_mod_2, j_mod_2 = dirs[(n + 1) % 4]
        if not is_in_region(farm, i + i_mod + i_mod_2, j + j_mod + j_mod_2, val):
          corners += 1

  return (area, corners)


def solution():
  """Solve the problem."""
  farm = read_farm()
  return get_fence_price(farm)
