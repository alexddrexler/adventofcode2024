"""Solution for https://adventofcode.com/2025/day/2#part2."""

import re

from util import read


_REGEX = r"^(?P<g1>\d+)(?P=g1)+$"


def read_ranges():
  data = read.read_input()
  # data = _TEST
  span_strs = data.split(",")
  spans = []
  for s in span_strs:
    first, last = s.split("-")
    spans.append((int(first), int(last)))
  return spans


def solution():
  """Solve the problem."""
  ranges = read_ranges()
  ans = 0
  for low, high in ranges:
    for i in range(low, high+1):
      num_str = str(i)
      if re.match(_REGEX, num_str):
        ans += i
  return ans
