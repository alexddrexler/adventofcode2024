"""Solution for https://adventofcode.com/2024/day/3#part2."""
import re

from util import read


MUL_RE = r"mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\)"
DO = "do()"
DONT = "don't()"


def solution():
  """Solve the problem."""
  data = read.read_file("day3/input1.txt")
  mul_sum = 0
  do = True
  for match in re.finditer(MUL_RE, data):
    if match.group(0) == DO:
      do = True
    elif match.group(0) == DONT:
      do = False
    elif do:
      mul_sum += int(match.group(1)) * int(match.group(2))
  return mul_sum
