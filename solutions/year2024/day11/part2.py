"""Solution for https://adventofcode.com/2024/day/11#part2."""
from solutions.year2024.day11 import part1


memo = {}


def count_stones(stone, blinks):
  global memo
  cached_value = memo.get((stone, blinks))
  if cached_value:
    return cached_value
  if blinks == 0:
    return 1
  else:
    new_stones = part1.modify(stone)
    value = sum([count_stones(ns, blinks - 1) for ns in new_stones])
  memo[(stone, blinks)] = value
  return value


def solution():
  """Solve the problem."""
  stones = part1.read_stones()
  tot = sum([count_stones(s, 75) for s in stones])
  return tot
