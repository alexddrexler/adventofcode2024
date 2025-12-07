"""Solution for https://adventofcode.com/2025/day/6#part2."""

import math

from util import read


_TEST = ("123 328  51 64 \n"
       + " 45 64  387 23 \n"
       + "  6 98  215 314\n"
       + "*   +   *   +  ")


def solution():
  """Solve the problem."""
  ans = 0
  data = read.read_input()
  # data = _TEST
  rows = [list(s) for s in data.split("\n")]
  signs_row = rows.pop()
  signs_row = rows.pop()
  print(signs_row)
  nums = []
  while signs_row:
    num = ""
    for row in rows:
      num += row.pop().strip()
    if num:
      nums.append(int(num))

    sign = signs_row.pop().strip()
    if sign:
      if sign == "+":
        ans += sum(nums)
      else:
        ans += math.prod(nums)
      nums = []

  return ans
