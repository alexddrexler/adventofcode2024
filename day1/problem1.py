"""Solution for https://adventofcode.com/2024/day/1."""
import os

from util import read


def read_lists() -> tuple[list[int], list[int]]:
  input_content = read.read_file("day1/input1.txt")
  l1 = []
  l2 = []
  for row in input_content.split("\n"):
    num_1, num_2 = row.split("   ")
    l1.append(int(num_1))
    l2.append(int(num_2))
  return l1, l2


def solution():
  """Solve the problem."""
  list_1, list_2 = read_lists()
  list_1.sort()
  list_2.sort()

  diff_sum = 0
  for i in range(len(list_1)):
    diff_sum += abs(list_1[i] - list_2[i])

  return diff_sum