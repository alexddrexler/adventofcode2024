"""Solution for https://adventofcode.com/2024/day/19#part2."""
from util import read


_MEMO = {}


def add_to_memo(pattern, count):
  global _MEMO
  _MEMO[pattern] = count
  return count


def read_input():
  content = read.read_file("day19/input1.txt")
  towels_str, patterns_str = content.split("\n\n")
  towels = [towel.strip() for towel in towels_str.split(",")]
  patterns = patterns_str.split("\n")
  return towels, patterns

def get_possible_combos(pattern, towels):
  ans = _MEMO.get(pattern)
  if ans is not None:
    return ans
  if len(pattern) == 0:
    return add_to_memo(pattern, 1)
  count = 0
  for t in towels:
    if pattern.startswith(t):
      count += get_possible_combos(pattern[len(t):], towels)
  return add_to_memo(pattern, count)

def solution():
  """Solve the problem."""
  towels, patterns = read_input()
  count = 0
  for p in patterns:
    count+= get_possible_combos(p, towels)
  return count
