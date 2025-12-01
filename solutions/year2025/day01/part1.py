"""Solution for https://adventofcode.com/2025/day/1."""

from util import read


def solution():
  """Solve the problem."""
  data = read.read_input()
  pos = 50
  ans = 0
  for inst in data.split("\n"):
    d = inst[0]
    diff = int(inst[1:])
    if d == "R":
      pos += diff
    elif d == "L":
      pos -= diff
    else:
      raise ValueError("Invalid direction")
    pos = pos % 100

    if pos == 0:
      ans += 1
  return ans
