"""Solution for https://adventofcode.com/2023/day/5."""

from util import read


def read_data():
  data = read.read_input()
  strs = data.split("\n\n")
  if len(strs) != 8:
    raise ValueError(f"Unexpected data format")

  seeds_str = strs[0][7:]
  seeds = [int(seed) for seed in seeds_str.split(" ")]

  maps = [_parse_map_str(map_str) for map_str in strs[1:]]

  return seeds, maps


def _parse_map_str(map_str: str) -> list[tuple[int, int, int]]:
  # Split into rows and trim label.
  str_list = map_str.split("\n")[1:]
  # Parse dest source and range (span).
  map_list = []
  for row in str_list:
    dest, source, span = [int(val) for val in row.split(" ")]
    map_list.append((dest, source, span))

  return map_list


def _convert_val(val: int, map_list: list[tuple[int, int, int]]) -> int:
  for dest, source, span in map_list:
    diff = val - source
    if diff > 0 and diff < span:
      return dest + diff
  return val


def solution():
  """Solve the problem."""
  seeds, maps = read_data()
  min_loc = None

  for val in seeds:
    for map_list in maps:
      val = _convert_val(val, map_list)

    if min_loc is None:
      min_loc = val
    else:
      min_loc = min(val, min_loc)

  return min_loc
