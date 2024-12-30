"""Solution for https://adventofcode.com/2024/day/11."""
from util import read


def read_stones():
  content = read.read_file("day11/input1.txt")
  return [int(val) for val in content.split(" ")]


def blink(stones: list[int]) -> list[int]:
  new_stones = []
  for stone in stones:
    new_stones.extend(modify(stone))
  return new_stones


def modify(stone: int) -> list[int]:
  if stone == 0:
    return [1,]
  if len(str(stone)) % 2 == 0:  # even number of digits.
    num_str = str(stone)
    midpoint = int(len(num_str) / 2)
    return [int(num_str[:midpoint]), int(num_str[midpoint:])]
  return [stone * 2024,]


def do_blinks(stones, blinks):
  for i in range(blinks):
    print(f"BLINK: {i}")
    print(len(stones))
    stones = blink(stones)
  return stones


def solution():
  """Solve the problem."""
  stones = read_stones()
  stones = do_blinks(stones, 25)
  return len(stones)
