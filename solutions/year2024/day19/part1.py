"""Solution for https://adventofcode.com/2024/day/19."""
from util import read


_MEMO = {}


def add_to_memo(pattern, is_valid):
  global _MEMO
  _MEMO[pattern] = is_valid
  return is_valid


def read_input():
  content = read.read_input()
  towels_str, patterns_str = content.split("\n\n")
  towels = [towel.strip() for towel in towels_str.split(",")]
  patterns = patterns_str.split("\n")
  return towels, patterns

def is_valid_pattern(pattern, towels):
  ans = _MEMO.get(pattern)
  if ans is not None:
    return ans
  if len(pattern) == 0:
    return add_to_memo(pattern, True)
  for t in towels:
    if pattern.startswith(t):
      if is_valid_pattern(pattern[len(t):], towels):
        return add_to_memo(pattern, True)
  return add_to_memo(pattern, False)

def solution():
  """Solve the problem."""
  towels, patterns = read_input()
  count = 0
  for p in patterns:
    if is_valid_pattern(p, towels):
      count += 1
  return count
