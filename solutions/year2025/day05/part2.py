"""Solution for https://adventofcode.com/2025/day/5#part2."""

from util import read


_TEST = """3-5
10-14
16-20
12-18

1
5
8
11
17
32"""


def parse_data():
  data = read.read_input()
  # data = _TEST
  raw_freshes, _ = data.split("\n\n")
  fresh_ranges = []
  for row in raw_freshes.split("\n"):
    first, last = row.split("-")
    fresh_ranges.append((int(first), int(last)))
  return fresh_ranges


def _in_range(x, r):
  l, h = r
  return x >= l and x <= h


def solution():
  """Solve the problem."""
  fresh_ranges = parse_data()
  out_ranges = [fresh_ranges[0]]
  for start, end in fresh_ranges:
    for i, o_range in enumerate(out_ranges):
      o_start, o_end = o_range
      if start > o_end:  # New range comes after current range.
        continue
      if end < o_start:  # New range comes fully before current range.
        out_ranges.insert(i, (start, end))
        break
      if start >= o_start and end <= o_end:  # New range fully contained in current range.
        break
      if end <= o_end:
        out_ranges[i] = (start, o_end)
        break
      new_start = min(start, o_start)
      new_end = end
      j = i + 1
      while j < len(out_ranges):
        j_start, j_end = out_ranges[j]
        if new_end < j_start:
          break
        j += 1
        if new_end <= j_end:
          new_end = j_end
          break
      out_ranges = out_ranges[0:i] + [(new_start, new_end)] + out_ranges[j:len(out_ranges)]
      break
    if start > out_ranges[-1][1]:
      out_ranges.append((start, end))

  ans = 0
  for s, e in out_ranges:
    ans += e - s + 1
  return ans
