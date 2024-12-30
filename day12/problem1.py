"""Solution for https://adventofcode.com/2024/day/12."""
from util import read


def read_farm():
  content = read.read_file("day12/input1.txt")
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
      area, perim = get_price_for_region(farm, in_region, i, j)
      print(f"{val}: area: {area}, perim: {perim}")
      fence_price += area * perim
  return fence_price


def get_price_for_region(farm, in_region, start_i, start_j):
  area = 0
  perim = 0
  squares = {(start_i, start_j),}
  while squares:
    area += 1
    i, j = squares.pop()
    print(f"Assessing ({i}, {j})")
    in_region[i][j] = True
    val = farm[i][j]
    for new_i, new_j in [(i-1, j), (i+1, j), (i, j-1), (i, j+1),]:
      print(f"({new_i}, {new_j})")
      if new_i < 0 or new_i >= len(farm) or new_j < 0 or new_j >= len(farm[0]):
        print("NOT VALID")
        perim += 1
        continue
      new_val = farm[new_i][new_j]
      if new_val != val:
        print("NOT EQUAL VALUE")
        perim += 1
        continue
      if in_region[new_i][new_j]:
        print("ALREADY COUNTED")
        continue
      print(f"Adding ({new_i}, {new_j})")
      squares.add((new_i, new_j))
  return (area, perim)


def solution():
  """Solve the problem."""
  farm = read_farm()
  return get_fence_price(farm)
