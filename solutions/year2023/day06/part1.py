"""Solution for https://adventofcode.com/2023/day/6."""

import math
from util import read


def read_races():
  data = read.read_input()
  time_str, dist_str = data.split("\n")
  times = _parse_ints(time_str)
  dists = _parse_ints(dist_str)
  return list(zip(times, dists))


def _parse_ints(inp: str) -> list[int]:
  ints = []
  cur_num = ""
  for c in inp:
    if c.isnumeric():
      cur_num += c
    elif cur_num:
      ints.append(int(cur_num))
      cur_num = ""
  if cur_num:
    ints.append(int(cur_num))
  return ints


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
