"""Solution for https://adventofcode.com/2025/day/3."""

from util import read


def solution():
  """Solve the problem."""
  data = read.read_input()
  bats = data.split("\n")
  ans = 0
  for bat in bats:
    pos1 = 0
    val1 = 0
    for i in range(len(bat) - 1):
      val = int(bat[i])
      if val > val1:
        val1 = val
        pos1 = i
    val2 = 0
    for j in range(pos1 + 1, len(bat)):
      val = int(bat[j])
      if val > val2:
        val2 = val
    ans += (val1 * 10) + val2
  return ans
