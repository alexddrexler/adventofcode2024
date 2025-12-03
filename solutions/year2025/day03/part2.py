"""Solution for https://adventofcode.com/2025/day/3#part2."""

from util import read


def get_joltage(inp: str, size: int) -> int:
  digits = []
  while len(digits) < size:
    maxd = 0
    maxpos = 0
    for i in range(len(inp) - (size - len(digits)) + 1):
      val = int(inp[i])
      if val > maxd:
        maxd = val
        maxpos = i
    digits.append(str(maxd))
    inp = inp[maxpos + 1:]
  return int("".join(digits))


def solution():
  """Solve the problem."""
  data = read.read_input()
  bats = data.split("\n")
  ans = 0
  for bat in bats:
    ans += get_joltage(bat, 12)
  return ans
