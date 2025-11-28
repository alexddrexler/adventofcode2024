"""Solution for https://adventofcode.com/2024/day/13#part2."""
import fractions

from solutions.year2024.day13 import part1


def read_problems(content=None):
  o_problems = part1.read_problems(content)
  problems = []
  for p in o_problems:
    ax_mod, ay_mod, bx_mod, by_mod, target_x, target_y = p
    problems.append((
        ax_mod,
        ay_mod,
        bx_mod,
        by_mod,
        target_x + 10000000000000,
        target_y + 10000000000000
    ))
  return problems


def get_min_cost(problem):
  ax_mod, ay_mod, bx_mod, by_mod, target_x, target_y = problem
  b = fractions.Fraction(target_x * ay_mod - target_y * ax_mod, bx_mod * ay_mod - by_mod * ax_mod)
  b = b.limit_denominator()
  if b.denominator != 1:
    return None
  b = int(b)
  a = fractions.Fraction(target_y - by_mod * b, ay_mod)
  a = a.limit_denominator()
  if a.denominator != 1:
    return None
  a = int(a)
  return 3 * a + b



def solution():
  """Solve the problem."""
  problems = read_problems()
  tot_min_cost = 0
  for p in problems:
    min_cost = get_min_cost(p)
    old_min_cost = part1.get_min_cost(p)
    if min_cost != old_min_cost:
      ax_mod, ay_mod, bx_mod, by_mod, target_x, target_y = p
    if min_cost is not None:
      tot_min_cost += min_cost
  return tot_min_cost
