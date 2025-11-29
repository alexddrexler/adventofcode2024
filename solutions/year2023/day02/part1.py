"""Solution for https://adventofcode.com/2023/day/2."""

import re

from util import read


ROW_RE = r"Game (\d*): (.*)"

RED_RE = r"(\d*) red"
GREEN_RE = r"(\d*) green"
BLUE_RE = r"(\d*) blue"

RED_MAX = 12
GREEN_MAX = 13
BLUE_MAX = 14


def is_valid(pull: str) -> bool:
  red_match = re.search(RED_RE, pull)
  green_match = re.search(GREEN_RE, pull)
  blue_match = re.search(BLUE_RE, pull)

  if red_match is not None:
    red_count = int(red_match.group(1))
    if red_count > RED_MAX:
      return False

  if green_match is not None:
    green_count = int(green_match.group(1))
    if green_count > GREEN_MAX:
      return False

  if blue_match is not None:
    blue_count = int(blue_match.group(1))
    if blue_count > BLUE_MAX:
      return False

  return True


def solution():
  """Solve the problem."""
  data = read.read_input()
  ans = 0
  for row in data.split("\n"):
    match = re.match(ROW_RE, row)
    if match is None:
      raise ValueError("Invalid game format.")
    game_num = int(match.group(1))
    pulls = match.group(2)
    is_valid_game = True
    for pull in pulls.split("; "):
      if not is_valid(pull):
        is_valid_game = False
        break
    if is_valid_game:
      ans += game_num

  return ans
