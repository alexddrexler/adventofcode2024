"""Solution for https://adventofcode.com/2023/day/2#part2."""

import re

from util import read


ROW_RE = r"Game (\d*): (.*)"

RED_RE = r"(\d*) red"
GREEN_RE = r"(\d*) green"
BLUE_RE = r"(\d*) blue"


def parse_pull(pull: str) -> tuple[int, int, int]:
  red_match = re.search(RED_RE, pull)
  green_match = re.search(GREEN_RE, pull)
  blue_match = re.search(BLUE_RE, pull)

  r = 0
  g = 0
  b = 0

  if red_match is not None:
    r = int(red_match.group(1))

  if green_match is not None:
    g = int(green_match.group(1))

  if blue_match is not None:
    b = int(blue_match.group(1))

  return r, g, b


def solution():
  """Solve the problem."""
  data = read.read_input()
  ans = 0
  for row in data.split("\n"):
    match = re.match(ROW_RE, row)
    if match is None:
      raise ValueError("Invalid game format.")
    pulls = match.group(2)
    max_r = 0
    max_g = 0
    max_b = 0
    for pull in pulls.split("; "):
      r, g, b = parse_pull(pull)
      max_r = max(max_r, r)
      max_g = max(max_g, g)
      max_b = max(max_b, b)

    ans += (max_r * max_g * max_b)

  return ans
