"""Solution for https://adventofcode.com/2024/day/14."""
import math
import re

from util import read


def read_robots():
  # Each robot is represented by a single tuple:
  # (px, py, vx, vy)
  regex = r"p=(-?\d*),(-?\d*) v=(-?\d*),(-?\d*)"
  content = read.read_file("day14/input1.txt")
  matches = re.findall(regex, content)
  return [tuple(map(int, match)) for match in matches]


def get_pos(robot, seconds):
  px, py, vx, vy = robot
  new_x = (vx * seconds + px) % 101
  new_y = (vy * seconds + py) % 103
  return (new_x, new_y)  


def get_quadrant(robot, seconds):
  new_x, new_y = get_pos(robot, seconds)
  if new_x == 50 or new_y == 51:
    return None
  if new_x < 50:
    if new_y < 51:
      return 0
    return 1
  if new_y < 51:
    return 2
  return 3


def solution():
  """Solve the problem."""
  robots = read_robots()
  quadrants = [0, 0, 0, 0]
  for robot in robots:
    quadrant = get_quadrant(robot, 100)
    if quadrant is not None:
      quadrants[quadrant] += 1
  return math.prod(quadrants)
