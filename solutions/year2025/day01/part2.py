"""Solution for https://adventofcode.com/2025/day/1#part2."""

from util import read


_TEST = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82"""


def solution():
  """Solve the problem."""
  data = read.read_input()
  # data = _TEST
  pos = 50
  ans = 0
  for inst in data.split("\n"):
    print(inst)
    d = inst[0]
    diff = int(inst[1:])
    ans += int(diff / 100)
    diff = diff % 100
    if d == "R":
      pos += diff
      if pos >= 100:
        ans += 1
    elif d == "L":
      # Ensure we don't double count 0
      if pos == 0:
        pos = 100
      pos -= diff
      if pos <= 0:
        ans += 1
    else:
      raise ValueError("Invalid direction")

    pos = pos % 100

    print(f"count: {ans}, pos: {pos}")

  return ans
