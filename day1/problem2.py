"""Solution for https://adventofcode.com/2024/day/1#part2."""
import os

from day1 import problem1


def solution():
  """Solve the problem."""
  list_1, list_2 = problem1.read_lists()
  list_1.sort()
  list_2.sort()

  similarity_score = 0

  for n1 in list_1:
    count = 0
    for n2 in list_2:
      if n2 > n1:
        break
      if n1 == n2:
        count +=1
    similarity_score += n1 * count

  return similarity_score