"""Solution for https://adventofcode.com/2024/day/13."""
import re

from util import read


# Each problem is a tuple of:
#   ax_mod
#   ay_mod
#   bx_mod
#   by_mod
#   target_x
#   target_y.


TEST = """Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279"""


def read_problems(content=None):
  regex = r"Button A: X\+(\d*), Y\+(\d*)\nButton B: X\+(\d*), Y\+(\d*)\nPrize: X=(\d*), Y=(\d*)"
  if content is None:
    content = read.read_input()
  matches = re.findall(regex, content)
  problems = []
  for match in matches:
    problems.append(tuple(int(i) for i in match))
  return problems


def get_min_cost(problem):
  ax_mod, ay_mod, bx_mod, by_mod, target_x, target_y = problem
  min_cost = None
  a_count = 0
  while a_count <= 100 and (min_cost is None or (a_count * 3) < min_cost):
    target_bx = target_x - (ax_mod * a_count)
    target_by = target_y - (ay_mod * a_count)
    if target_bx < 0 or target_by < 0:
      return min_cost
    if target_bx % bx_mod != 0:
      a_count += 1
      continue
    b_count = int(target_bx / bx_mod)
    if b_count * by_mod == target_by:
      cost = (a_count * 3) + b_count
      if min_cost is None or cost < min_cost:
        min_cost = cost
    a_count += 1
  return min_cost


def solution():
  """Solve the problem."""
  problems = read_problems()
  tot_min_cost = 0
  for p in problems:
    min_cost = get_min_cost(p)
    if min_cost is not None:
      tot_min_cost += min_cost
  return tot_min_cost
