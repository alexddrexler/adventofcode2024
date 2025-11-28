"""Solution for https://adventofcode.com/2024/day/7."""
from util import read


def read_equations():
  content = read.read_input()
  equations = []
  for row in content.split("\n"):
    test, nums = row.split(": ")
    equations.append((int(test), [int(num) for num in nums.split(" ")]))
  return equations


def is_valid(test, nums):
  outs = [nums[0]]
  for num in nums[1:]:
    new_outs = []
    for out in outs:
      new_outs.extend([out + num, out * num])
    outs = new_outs
  return test in outs



def solution():
  """Solve the problem."""
  equations = read_equations()
  score = 0
  for test, nums in equations:
    if is_valid(test, nums):
      score += test
  return score
