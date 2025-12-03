"""Solution for https://adventofcode.com/2025/day/2."""

import re

from util import read


_REGEX = r"^(?P<g1>\d+)(?P=g1)$"


_TEST = "11-12"


def read_ranges():
  data = read.read_input()
  # data = _TEST
  span_strs = data.split(",")
  spans = []
  for s in span_strs:
    first, last = s.split("-")
    spans.append((int(first), int(last)))
  return spans


def regex_solution():
  ranges = read_ranges()
  ans = 0
  for low, high in ranges:
    for i in range(low, high+1):
      num_str = str(i)
      if re.match(_REGEX, num_str):
        print(i)
        ans += i
  return ans


def original_solution():
  ranges = read_ranges()
  ans = 0
  for low, high in ranges:
    for i in range(low, high+1):
      places = len(str(i))
      if places % 2 != 0:
        continue
      half_places = int(places / 2)
      div = pow(10, half_places)
      first = int(i / div)
      last = i % div
      print(f"{i}: {first}, {last}")
      if first == last:
        ans += i
  return ans



def solution():
  """Solve the problem."""
  return regex_solution()