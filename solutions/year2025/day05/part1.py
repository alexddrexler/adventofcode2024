"""Solution for https://adventofcode.com/2025/day/5."""

from util import read


def parse_data():
  data = read.read_input()
  raw_freshes, raw_foods = data.split("\n\n")
  fresh_ranges = []
  for row in raw_freshes.split("\n"):
    first, last = row.split("-")
    fresh_ranges.append((int(first), int(last)))
  foods = [int(s) for s in raw_foods.split("\n")]
  return fresh_ranges, foods


def solution():
  """Solve the problem."""
  fresh_ranges, foods = parse_data()
  ans = 0
  for f in foods:
    for start, end in fresh_ranges:
      if f >= start and f <= end:
        ans += 1
        break
  return ans
