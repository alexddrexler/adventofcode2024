"""Solution for https://adventofcode.com/2024/day/3."""
import re

from util import read


MUL_RE = r"mul\((\d{1,3}),(\d{1,3})\)"


def solution():
  """Solve the problem."""
  data = read.read_input()
  mul_sum = 0
  for match in re.finditer(MUL_RE, data):
    mul_sum += int(match.group(1)) * int(match.group(2))
  return mul_sum
