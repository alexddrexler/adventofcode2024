"""Solution for https://adventofcode.com/2023/day/1#part2."""

from util import read


SPELLED_NUMS = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]

def is_spelled_num(row, idx):
  for val_minus_one, num in enumerate(SPELLED_NUMS):
    if len(row) - idx < len(num):
      continue
    is_num = True
    for i, num_char in enumerate(num):
      if row[idx + i] != num_char:
        is_num = False
        break
    if is_num:
      return str(val_minus_one + 1)
  return None



def get_val(row: str) -> int:
  start_idx = 0
  first = None
  while first is None and start_idx < len(row):
    char = row[start_idx]
    if char.isnumeric():
      first = char
    else:
      val = is_spelled_num(row, start_idx)
      if val is None:
        start_idx += 1
      else:
        first = val

  if first is None:
    raise ValueError("No digits in row!")

  end_idx = len(row) - 1
  last = None
  while last is None and end_idx >= start_idx:
    char = row[end_idx]
    if char.isnumeric():
      last = char
    else:
      val = is_spelled_num(row, end_idx)
      if val is None:
        end_idx -= 1
      else:
        last = val

  return int(first + last)


def solution():
  """Solve the problem."""
  data = read.read_input()
  rows = data.split("\n")
  tot = 0
  for row in rows:
    tot += get_val(row)

  return tot
