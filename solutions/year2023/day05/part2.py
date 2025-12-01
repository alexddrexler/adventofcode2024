"""Solution for https://adventofcode.com/2023/day/5#part2."""

from util import read


_TEST = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""


def read_data():
  data = read.read_input()
  # data = _TEST
  strs = data.split("\n\n")
  if len(strs) != 8:
    raise ValueError(f"Unexpected data format")

  seeds_str = strs[0][7:]
  seeds = [int(seed) for seed in seeds_str.split(" ")]
  seeds.reverse()
  new_seeds = []
  while seeds:
    new_seeds.append((seeds.pop(), seeds.pop()))


  maps = [_parse_map_str(map_str) for map_str in strs[1:]]

  return new_seeds, maps


def _parse_map_str(map_str: str) -> list[tuple[int, int, int]]:
  # Split into rows and trim label.
  str_list = map_str.split("\n")[1:]
  # Parse dest source and range (span).
  map_list = []
  for row in str_list:
    dest, source, span = [int(val) for val in row.split(" ")]
    map_list.append((dest, source, span))

  return map_list


def _update_vals(
    vals: list[tuple[int, int]],
    map_list: list[tuple[int, int, int]]
) -> list[tuple[int, int]]:
  out_vals = []
  for dest, source, span in map_list:
    rem_vals = []
    for v_start, v_span in vals:
      # No overlap.
      if v_start > source + span or v_start + v_span < source:
        rem_vals.append((v_start, v_span))
        continue

      # Pass any lower vals into rem_vals.
      if v_start < source:
        diff = source - v_start
        rem_vals.append((v_start, diff))
        v_start = source
        v_span -= diff

      # Pass any higher vals into rem_vals.
      v_end = v_start + v_span
      m_end = source + span
      if v_end > m_end:
        diff = v_end - m_end
        rem_vals.append((m_end, diff))
        v_span -= diff

      # Convert any overlapping vals and pass to out_vals.
      offset = v_start - source
      out_start = dest + offset
      out_vals.append((out_start, v_span))
    vals = rem_vals
  out_vals.extend(rem_vals)
  return out_vals


def solution():
  """Solve the problem."""
  vals, maps = read_data()

  for map_list in maps:
    vals = _update_vals(vals, map_list)

  return min([val[0] for val in vals])
