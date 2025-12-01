"""Solution for https://adventofcode.com/2023/day/6#part2."""
"""Solution for https://adventofcode.com/2023/day/6."""

import math
from util import read


def read_races():
  data = read.read_input()
  time_str, dist_str = data.split("\n")
  time = _parse_int(time_str)
  dist = _parse_int(dist_str)
  return [(time, dist)]


def _parse_int(inp: str) -> list[int]:
  cur_num = ""
  for c in inp:
    if c.isnumeric():
      cur_num += c
  return int(cur_num)


def get_winning_times(race):
  time, record = race
  count = 0
  for t in range(time):
    dist = t * (time - t)
    if dist > record:
      count += 1
  return count



def solution():
  """Solve the problem."""
  races = read_races()
  return math.prod([get_winning_times(r) for r in races])
