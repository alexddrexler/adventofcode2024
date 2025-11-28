"""Solution for https://adventofcode.com/2024/day/5."""
from collections import defaultdict

from util import read


def read_input():
  content = read.read_input()
  rows = content.split("\n")
  rules = defaultdict(set)
  updates = []
  in_rules = True
  for row in rows:
    if in_rules:
      nums = [num for num in row.split("|")]
      if len(nums) != 2:
        in_rules = False
        continue
      num1, num2 = nums
      rules[int(num1)].add(int(num2))
      continue
    pages = [int(num) for num in row.split(",")]
    updates.append(pages)
  return (rules, updates)


def is_valid(update, rules):
  nums = set()
  for num in update:
    bombs = rules[num]
    if set.intersection(nums, bombs):
      return False
    nums.add(num)
  return True


def solution():
  """Solve the problem."""
  rules, updates = read_input()
  middle_sum = 0
  for update in updates:
    if is_valid(update, rules):
      middle_sum += update[int(len(update) / 2)]

  return middle_sum
