"""Solution for https://adventofcode.com/2025/day/6."""

import math
import re

from util import read


_TEST = """123 328  51 64
 45 64  387 23
  6 98  215 314
*   +   *   + """


def solution():
  """Solve the problem."""
  data = read.read_input()
  # data = _TEST
  rows = data.split("\n")
  num_groups = []
  sign_row = rows.pop()
  signs = [match[0] for match in re.finditer(r"[+*]", sign_row)]
  for row in rows:
    i = 0
    for match in re.finditer(r"\d+", row):
      if len(num_groups) < i + 1:
        num_groups.append([])
      num_groups[i].append(int(match[0]))
      i += 1

  ans = 0
  for i, sign in enumerate(signs):
    nums = num_groups[i]
    if sign == "+":
      ans += sum(nums)
    else:
      ans += math.prod(nums)

  return ans
