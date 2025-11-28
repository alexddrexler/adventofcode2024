"""Solution for https://adventofcode.com/2023/day/1."""

from util import read


def get_val(row: str) -> int:
  start_idx = 0
  first = None
  while first is None and start_idx < len(row):
    char = row[start_idx]
    if char.isnumeric():
      first = char
    else:
      start_idx += 1

  if first is None:
    raise ValueError("No digits in row!")

  end_idx = len(row) - 1
  last = None
  while last is None and end_idx >= start_idx:
    char = row[end_idx]
    if char.isnumeric():
      last = char
    else:
      end_idx -= 1

  return int(first + last)


def solution():
  """Solve the problem."""
  data = read.read_input()
  rows = data.split("\n")
  tot = 0
  for row in rows:
    tot += get_val(row)

  return tot
